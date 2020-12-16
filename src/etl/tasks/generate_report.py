"""This script contain prefect task to generate report from the downloaded document
"""
from typing import Tuple
import datetime
import pdftotext
from prefect import task
import pandas as pd
from .consts import REPORT_PATH, DOWNLOAD_PATH


def transform_page(page: str) -> Tuple[str, str]:
    """Utility function to transform pdf text content

    Args:
        page (str): Text in a pdf page

    Returns:
        Tuple[str, str]: Tuple of line_of_business and predictions
    """
    split_char = "\r\n" if "\r\n" in page else "\n"
    lines = [line for line in page.split(split_char) if line]
    page_title = lines[0]
    x = lines[1].find("Rate predictions")
    if x < 0:
        x = lines[1].find("Price predictions")
    data = []
    for line in lines[1:]:
        if line and line[0] == " ":
            data.append(line[x:].strip())
        else:
            break
    data = "\n".join(data)
    return page_title, data


@task(
    log_stdout=True,
    skip_on_upstream_skip=False,
    max_retries=3,
    retry_delay=datetime.timedelta(minutes=2),
)
def generate_report():
    with open(DOWNLOAD_PATH, "rb") as fp:
        pdf_as_text = pdftotext.PDF(fp)
    pages_with_line_of_business = (
        page for page in pdf_as_text if "Key takeaway" in page
    )

    report_df = pd.DataFrame(
        map(transform_page, pages_with_line_of_business),
        columns=["line_of_business", "rate_or_price_predictions"],
    )
    with pd.ExcelWriter(REPORT_PATH) as xl_writer:
        report_df.to_excel(excel_writer=xl_writer, index=False)
