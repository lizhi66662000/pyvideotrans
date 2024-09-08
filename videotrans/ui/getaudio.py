# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'getaudio.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import (QMetaObject, QSize, Qt)
from PySide6.QtGui import (QCursor)
from PySide6.QtWidgets import (QHBoxLayout, QLineEdit,
                               QPushButton,
                               QVBoxLayout)

from videotrans.configure import config


class Ui_getaudio(object):
    def setupUi(self, getaudio):
        self.has_done=False

        if not getaudio.objectName():
            getaudio.setObjectName(u"getaudio")
        getaudio.resize(643, 300)
        getaudio.setWindowModality(QtCore.Qt.NonModal)
        self.videourls = []
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(getaudio.sizePolicy().hasHeightForWidth())
        getaudio.setSizePolicy(sizePolicy)
        getaudio.setMaximumSize(QtCore.QSize(643, 300))

        self.horizontalLayout_3 = QHBoxLayout(getaudio)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.videourl = QLineEdit(getaudio)
        self.videourl.setObjectName(u"videourl")
        self.videourl.setMinimumSize(QSize(0, 35))
        self.videourl.setReadOnly(True)
        self.horizontalLayout.addWidget(self.videourl)

        self.videobtn = QPushButton(getaudio)
        self.videobtn.setObjectName(u"videobtn")
        self.videobtn.setMinimumSize(QSize(180, 35))
        self.videobtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.videobtn.setMouseTracking(False)
        self.horizontalLayout.addWidget(self.videobtn)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.startbtn = QPushButton(getaudio)
        self.startbtn.setObjectName(u"startbtn")
        self.startbtn.setMinimumSize(QSize(0, 35))
        self.startbtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.verticalLayout.addWidget(self.startbtn)

        self.resultbtn = QPushButton(getaudio)
        self.resultbtn.setObjectName(u"resultbtn")
        self.resultbtn.setStyleSheet("""background-color:transparent""")
        self.resultbtn.setMinimumSize(QSize(0, 30))
        self.resultbtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.verticalLayout.addWidget(self.resultbtn)
        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.retranslateUi(getaudio)

        QMetaObject.connectSlotsByName(getaudio)

    # setupUi

    def retranslateUi(self, getaudio):
        getaudio.setWindowTitle("批量从视频中分离出音频" if config.defaulelang == 'zh' else 'Separating audio from video')
        self.videourl.setPlaceholderText(
            "选择需要分离出音频的视频文件/1或多个" if config.defaulelang == 'zh' else 'Videos to be separated')
        self.videobtn.setText("选择视频" if config.defaulelang == 'zh' else 'Select the videos')
        self.startbtn.setText("开始执行" if config.defaulelang == 'zh' else 'Start of execution')
        self.resultbtn.setText("打开保存结果目录" if config.defaulelang == 'zh' else 'Open the save results directory')