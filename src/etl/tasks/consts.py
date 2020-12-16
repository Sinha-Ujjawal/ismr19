"""Thie scripts contains all the constants common to tasks module
"""
import os
from pathlib import Path

DOCUMENT_URL = "https://www.willistowerswatson.com/-/media/WTW/Insights/2019/11/insurance-marketplace-realities-fall-2019.pdf"
DOWNLOAD_FOLDER = Path("data")
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)
DOWNLOAD_PATH = DOWNLOAD_FOLDER / "insurance-marketplace-realities-fall-2019.pdf"
REPORT_DIR = Path("report")
REPORT_PATH = REPORT_DIR / "report.xlsx"
os.makedirs(REPORT_DIR, exist_ok=True)
