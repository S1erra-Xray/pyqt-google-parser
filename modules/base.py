from PySide6.QtCore import QThread, Signal
from PySide6.QtWidgets import QLabel, QProgressBar, QSpinBox, QStatusBar
from selenium import webdriver

from .messages import ErrorMsg, WarnMsg


class CustomThread(QThread):
    error_sig = Signal(str, str)
    warn_sig = Signal(str, str)

    def __init__(self):
        super().__init__(parent=None)
        self.error_sig.connect(ErrorMsg)
        self.warn_sig.connect(WarnMsg)


class Base(CustomThread):
    status_bar: QStatusBar = None
    lbl_progress: QLabel = None
    driver: webdriver = None
    progress_bar: QProgressBar = None
    sb_pages_count: QSpinBox = None
    path = None
    is_downloadable = None
    get_filename_from_url = None
