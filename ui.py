# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'raw_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect)
from PySide6.QtWidgets import (QCheckBox, QComboBox, QGridLayout,
                               QLabel, QLayout, QLineEdit, QProgressBar, QPushButton, QRadioButton, QSpinBox, QStatusBar, QVBoxLayout, QWidget)


class Ui_GoogleParser(object):
    def setupUi(self, GoogleParser):
        if not GoogleParser.objectName():
            GoogleParser.setObjectName(u"GoogleParser")
        GoogleParser.resize(600, 450)
        self.centralwidget = QWidget(GoogleParser)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 0, 581, 421))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(4, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.lbl_search_query = QLabel(self.verticalLayoutWidget)
        self.lbl_search_query.setObjectName(u"lbl_search_query")

        self.gridLayout.addWidget(self.lbl_search_query, 2, 0, 1, 1)

        self.rd_urls = QRadioButton(self.verticalLayoutWidget)
        self.rd_urls.setObjectName(u"rd_urls")
        self.rd_urls.setChecked(True)
        self.rd_urls.setAutoRepeat(True)

        self.gridLayout.addWidget(self.rd_urls, 3, 0, 1, 1)

        self.cb_download = QCheckBox(self.verticalLayoutWidget)
        self.cb_download.setObjectName(u"cb_download")
        self.cb_download.setCheckable(True)
        self.cb_download.setAutoRepeat(False)

        self.gridLayout.addWidget(self.cb_download, 5, 0, 1, 1)

        self.btn_open_folder = QPushButton(self.verticalLayoutWidget)
        self.btn_open_folder.setObjectName(u"btn_open_folder")
        self.btn_open_folder.setEnabled(False)

        self.gridLayout.addWidget(self.btn_open_folder, 7, 2, 1, 1)

        self.rd_photos = QRadioButton(self.verticalLayoutWidget)
        self.rd_photos.setObjectName(u"rd_photos")

        self.gridLayout.addWidget(self.rd_photos, 3, 1, 1, 1)

        self.lne_search_query = QLineEdit(self.verticalLayoutWidget)
        self.lne_search_query.setObjectName(u"lne_search_query")

        self.gridLayout.addWidget(self.lne_search_query, 2, 1, 1, 2)

        self.co_select_browser = QComboBox(self.verticalLayoutWidget)
        self.co_select_browser.addItem("")
        self.co_select_browser.addItem("")
        self.co_select_browser.setObjectName(u"co_select_browser")

        self.gridLayout.addWidget(self.co_select_browser, 0, 1, 1, 2)

        self.lbl_select_browser = QLabel(self.verticalLayoutWidget)
        self.lbl_select_browser.setObjectName(u"lbl_select_browser")

        self.gridLayout.addWidget(self.lbl_select_browser, 0, 0, 1, 1)

        self.lbl_savefile = QLabel(self.verticalLayoutWidget)
        self.lbl_savefile.setObjectName(u"lbl_savefile")

        self.gridLayout.addWidget(self.lbl_savefile, 16, 0, 1, 1)

        self.lbl_pages_count = QLabel(self.verticalLayoutWidget)
        self.lbl_pages_count.setObjectName(u"lbl_pages_count")

        self.gridLayout.addWidget(self.lbl_pages_count, 14, 0, 1, 1)

        self.lbl_download_folder = QLabel(self.verticalLayoutWidget)
        self.lbl_download_folder.setObjectName(u"lbl_download_folder")
        self.lbl_download_folder.setEnabled(False)

        self.gridLayout.addWidget(self.lbl_download_folder, 7, 0, 1, 1)

        self.lne_folder_path = QLineEdit(self.verticalLayoutWidget)
        self.lne_folder_path.setObjectName(u"lne_folder_path")
        self.lne_folder_path.setEnabled(False)
        self.lne_folder_path.setDragEnabled(False)
        self.lne_folder_path.setReadOnly(True)
        self.lne_folder_path.setClearButtonEnabled(False)

        self.gridLayout.addWidget(self.lne_folder_path, 7, 1, 1, 1)

        self.lne_file_path = QLineEdit(self.verticalLayoutWidget)
        self.lne_file_path.setObjectName(u"lne_file_path")
        self.lne_file_path.setReadOnly(True)

        self.gridLayout.addWidget(self.lne_file_path, 16, 1, 1, 1)

        self.sb_pages_count = QSpinBox(self.verticalLayoutWidget)
        self.sb_pages_count.setObjectName(u"sb_pages_count")

        self.gridLayout.addWidget(self.sb_pages_count, 14, 1, 1, 1)

        self.btn_start_parsing = QPushButton(self.verticalLayoutWidget)
        self.btn_start_parsing.setObjectName(u"btn_start_parsing")

        self.gridLayout.addWidget(self.btn_start_parsing, 18, 0, 1, 3)

        self.btn_open_file = QPushButton(self.verticalLayoutWidget)
        self.btn_open_file.setObjectName(u"btn_open_file")

        self.gridLayout.addWidget(self.btn_open_file, 16, 2, 1, 1)

        self.lbl_progress = QLabel(self.verticalLayoutWidget)
        self.lbl_progress.setObjectName(u"lbl_progress")
        self.lbl_progress.setEnabled(True)

        self.gridLayout.addWidget(self.lbl_progress, 17, 0, 1, 1)

        self.progress_bar = QProgressBar(self.verticalLayoutWidget)
        self.progress_bar.setObjectName(u"progress_bar")
        self.progress_bar.setEnabled(True)
        self.progress_bar.setMaximum(100)
        self.progress_bar.setValue(0)
        self.progress_bar.setTextVisible(True)

        self.gridLayout.addWidget(self.progress_bar, 17, 1, 1, 2)

        self.verticalLayout.addLayout(self.gridLayout)

        GoogleParser.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(GoogleParser)
        self.statusBar.setObjectName(u"statusBar")
        GoogleParser.setStatusBar(self.statusBar)

        self.retranslateUi(GoogleParser)

        QMetaObject.connectSlotsByName(GoogleParser)

    # setupUi

    def retranslateUi(self, GoogleParser):
        GoogleParser.setWindowTitle(
            QCoreApplication.translate("GoogleParser", u"Google Parser", None))
        self.lbl_search_query.setText(QCoreApplication.translate("GoogleParser",
                                                                 u"\u041f\u043e\u0438\u0441\u043a\u043e\u0432\u044b\u0439 \u0437\u0430\u043f\u0440\u043e\u0441",
                                                                 None))
        self.rd_urls.setText(QCoreApplication.translate("GoogleParser",
                                                        u"\u041f\u043e\u0438\u0441\u043a\u043e\u0432\u0430\u044f \u0432\u044b\u0434\u0430\u0447\u0430",
                                                        None))
        self.cb_download.setText(QCoreApplication.translate("GoogleParser",
                                                            u"\u0417\u0430\u0433\u0440\u0443\u0436\u0430\u0442\u044c \u0444\u0430\u0439\u043b\u044b \u043f\u043e \u0441\u0441\u044b\u043b\u043a\u0430\u043c",
                                                            None))
        self.btn_open_folder.setText(
            QCoreApplication.translate("GoogleParser", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c", None))
        self.rd_photos.setText(
            QCoreApplication.translate("GoogleParser", u"\u041a\u0430\u0440\u0442\u0438\u043d\u043a\u0438", None))
        self.co_select_browser.setItemText(0, QCoreApplication.translate("GoogleParser", u"Firefox", None))
        self.co_select_browser.setItemText(1, QCoreApplication.translate("GoogleParser", u"Chrome", None))

        self.lbl_select_browser.setText(QCoreApplication.translate("GoogleParser",
                                                                   u"\u0412\u044b\u0431\u0435\u0440\u0435\u0442\u0435 \u0441\u0432\u043e\u0439 \u0431\u0440\u0430\u0443\u0437\u0435\u0440",
                                                                   None))
        self.lbl_savefile.setText(QCoreApplication.translate("GoogleParser",
                                                             u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0441\u0441\u044b\u043b\u043a\u0438 \u0432 \u0444\u0430\u0439\u043b",
                                                             None))
        self.lbl_pages_count.setText(QCoreApplication.translate("GoogleParser",
                                                                u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0441\u0442\u0440\u0430\u043d\u0438\u0446 \u0438\u043b\u0438 \u043a\u0430\u0440\u0442\u0438\u043d\u043e\u043a",
                                                                None))
        self.lbl_download_folder.setText(QCoreApplication.translate("GoogleParser",
                                                                    u"\u041f\u0430\u043f\u043a\u0430 \u0434\u043b\u044f \u0437\u0430\u0433\u0440\u0443\u0437\u043a\u0438 \u0444\u0430\u0439\u043b\u043e\u0432",
                                                                    None))
        self.btn_start_parsing.setText(QCoreApplication.translate("GoogleParser",
                                                                  u"\u041d\u0430\u0447\u0430\u0442\u044c \u043f\u0430\u0440\u0441\u0438\u043d\u0433",
                                                                  None))
        self.btn_open_file.setText(
            QCoreApplication.translate("GoogleParser", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c", None))
        self.lbl_progress.setText(
            QCoreApplication.translate("GoogleParser", u"\u041f\u0440\u043e\u0433\u0440\u0435\u0441\u0441", None))
    # retranslateUi
