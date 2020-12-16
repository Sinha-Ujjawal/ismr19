"""This script contain prefect task to download the asked document
"""
from prefect import task
import urllib.request
from .consts import DOCUMENT_URL, DOWNLOAD_PATH

HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) "
    "AppleWebKit/537.11 (KHTML, like Gecko) "
    "Chrome/23.0.1271.64 Safari/537.11",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Charset": "ISO-8859-1,utf-8;q=0.7,*;q=0.3",
    "Accept-Encoding": "none",
    "Accept-Language": "en-US,en;q=0.8",
    "Connection": "keep-alive",
}


@task(log_stdout=True)
def download_document():
    print(f"Downloading the file: {DOCUMENT_URL}, to: {DOWNLOAD_PATH}")
    opener = urllib.request.build_opener()
    opener.addheaders = HEADERS.items()
    urllib.request.install_opener(opener)
    urllib.request.urlretrieve(DOCUMENT_URL, DOWNLOAD_PATH)
