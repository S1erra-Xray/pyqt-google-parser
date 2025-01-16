import os

import requests
from PySide6 import QtWidgets
from PySide6.QtWidgets import QFileDialog

from modules.base import Base
from modules.files import DownloadFilesThread
from modules.messages import ErrorMsg
from modules.photos import ParsingPhotosThread
from modules.urls import ParsingUrlsThread
from ui import Ui_GoogleParser


class connect_buttons(QtWidgets.QMainWindow, Ui_GoogleParser):
    def __init__(self, parent=None) -> None:
        super(connect_buttons, self).__init__(parent=parent)
        self.setupUi(self)

        self.btn_start_parsing.clicked.connect(self.start_parsing)
        self.btn_open_file.clicked.connect(self.file_dialog)
        self.btn_open_folder.clicked.connect(self.folder_dialog)
        self.cb_download.released.connect(self.enabled_or_disabled)

    def is_downloadable(self, url):
        """
        Does the url contain a downloadable resource
        """
        try:
            header = requests.head(url, allow_redirects=True).headers
        except:
            return False

        content_type = header.get('content-type')
        try:
            if 'text' in content_type.lower():
                return False
            if 'html' in content_type.lower():
                return False
        except:
            return False

        return True

    def get_filename_from_url(self, url):
        if not url:
            return None
        fname = url.split('/')[-1]

        return fname

    def enabled_or_disabled(self):
        if self.cb_download.isChecked():
            self.lne_folder_path.setEnabled(True)
            self.lbl_download_folder.setEnabled(True)
            self.btn_open_folder.setEnabled(True)
        else:
            self.lne_folder_path.setEnabled(False)
            self.lbl_download_folder.setEnabled(False)
            self.btn_open_folder.setDisabled(True)

    def file_dialog(self):
        self.file_name = QFileDialog.getSaveFileName(None, 'Введите имя файла для сохранения', '.', '(*.txt)')
        self.lne_file_path.setText(self.file_name[0])

    def folder_dialog(self) -> None:
        self.folder_name = QFileDialog.getExistingDirectory(None, 'Выберите папку для сохранения', '.')
        self.lne_folder_path.setText(self.folder_name)

    def start_parsing(self):
        if self.lne_search_query.displayText() != '' and self.lne_file_path.displayText() != '':
            self.pages_count = self.sb_pages_count.value()
            self.path = self.file_name[0]
            self.urls_count = 0
            self.progress_bar.setValue(0)

            if self.pages_count == 0:
                ErrorMsg('Введите количество страниц')
                return

            try:
                os.remove(self.path)
            except Exception as e:
                print('файла не существует')

            if self.co_select_browser.currentText() == 'Firefox':
                from selenium.webdriver import Firefox
                self.driver = Firefox()

            elif self.co_select_browser.currentText() == 'Chrome':
                from selenium.webdriver import Chrome
                self.driver = Chrome()

            try:
                self.driver.get('https://www.google.com/search?q={0}&filter=0'.format(
                    self.lne_search_query.displayText().replace(' ', '+')))
            except Exception as e:
                ErrorMsg('Нет интернет соединения', e)

            self.ParsingUrlsThread_instance = ParsingUrlsThread()
            self.ParsingPhotosThread_instance = ParsingPhotosThread()

            Base.driver = self.driver
            Base.sb_pages_count = self.sb_pages_count.value()
            Base.lbl_progress = self.lbl_progress
            Base.path = self.path
            Base.progress_bar = self.progress_bar
            Base.status_bar = self.statusBar
            Base.is_downloadable = self.is_downloadable
            Base.get_filename_from_url = self.get_filename_from_url

            if self.rd_urls.isChecked():
                self.ParsingUrlsThread_instance.start()

            elif self.rd_photos.isChecked():
                self.ParsingPhotosThread_instance.start()

            if self.cb_download.isChecked():
                while True:
                    if self.ParsingPhotosThread_instance.isFinished() or self.ParsingUrlsThread_instance.isFinished():
                        self.DownloadThread_instance = DownloadFilesThread()
                        self.DownloadThread_instance.start()
                        break

        else:
            ErrorMsg('Вы не ввели все параметры')


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    cb = connect_buttons()
    cb.show()
    sys.exit(app.exec_())
