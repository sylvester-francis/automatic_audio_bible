# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(356, 307)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainWindow.sizePolicy().hasHeightForWidth())
        mainWindow.setSizePolicy(sizePolicy)
        mainWindow.setMaximumSize(QtCore.QSize(356, 307))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons8-holy-bible-36.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMaximumSize(QtCore.QSize(356, 256))
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 321, 241))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMaximumSize(QtCore.QSize(321, 241))
        self.groupBox.setObjectName("groupBox")
        self.widget = QtWidgets.QWidget(self.groupBox)
        self.widget.setGeometry(QtCore.QRect(11, 41, 302, 178))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.comboBox_2 = QtWidgets.QComboBox(self.widget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox_2)
        self.Book_voiceInput = QtWidgets.QPushButton(self.widget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons8-voice-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Book_voiceInput.setIcon(icon1)
        self.Book_voiceInput.setObjectName("Book_voiceInput")
        self.horizontalLayout_2.addWidget(self.Book_voiceInput)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_3.addWidget(self.lineEdit_2)
        self.Chapter_VoiceInput = QtWidgets.QPushButton(self.widget)
        self.Chapter_VoiceInput.setIcon(icon1)
        self.Chapter_VoiceInput.setObjectName("Chapter_VoiceInput")
        self.horizontalLayout_3.addWidget(self.Chapter_VoiceInput)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_4.addWidget(self.lineEdit)
        self.Verse_VoiceInput = QtWidgets.QPushButton(self.widget)
        self.Verse_VoiceInput.setIcon(icon1)
        self.Verse_VoiceInput.setObjectName("Verse_VoiceInput")
        self.horizontalLayout_4.addWidget(self.Verse_VoiceInput)
        self.gridLayout.addLayout(self.horizontalLayout_4, 3, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.Ok_button = QtWidgets.QPushButton(self.widget)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons8-checked-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Ok_button.setIcon(icon2)
        self.Ok_button.setObjectName("Ok_button")
        self.horizontalLayout_5.addWidget(self.Ok_button)
        self.Cancel_button = QtWidgets.QPushButton(self.widget)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons8-cancel-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Cancel_button.setIcon(icon3)
        self.Cancel_button.setObjectName("Cancel_button")
        self.horizontalLayout_5.addWidget(self.Cancel_button)
        self.gridLayout.addLayout(self.horizontalLayout_5, 4, 0, 1, 1)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 356, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)
        self.actionAbout = QtWidgets.QAction(mainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionShortcuts = QtWidgets.QAction(mainWindow)
        self.actionShortcuts.setObjectName("actionShortcuts")
        self.actionClose = QtWidgets.QAction(mainWindow)
        self.actionClose.setObjectName("actionClose")
        self.actionCut = QtWidgets.QAction(mainWindow)
        self.actionCut.setObjectName("actionCut")
        self.actionCopy = QtWidgets.QAction(mainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(mainWindow)
        self.actionPaste.setObjectName("actionPaste")
        self.actionHelp = QtWidgets.QAction(mainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.menuFile.addAction(self.actionClose)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionShortcuts)
        self.menuHelp.addAction(self.actionHelp)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Bible Searcher"))
        self.groupBox.setTitle(_translate("mainWindow", "Audio Bible/Text Searcher"))
        self.label.setText(_translate("mainWindow", "Bible Translation :"))
        self.comboBox.setItemText(0, _translate("mainWindow", "KJV"))
        self.comboBox.setItemText(1, _translate("mainWindow", "NRSV"))
        self.comboBox.setItemText(2, _translate("mainWindow", "RSV"))
        self.comboBox.setItemText(3, _translate("mainWindow", "NKJV"))
        self.comboBox.setItemText(4, _translate("mainWindow", "Amplified"))
        self.label_2.setText(_translate("mainWindow", "Book:"))
        self.comboBox_2.setItemText(0, _translate("mainWindow", "Genesis"))
        self.comboBox_2.setItemText(1, _translate("mainWindow", "Exodus "))
        self.comboBox_2.setItemText(2, _translate("mainWindow", "Leviticus "))
        self.comboBox_2.setItemText(3, _translate("mainWindow", "Numbers "))
        self.comboBox_2.setItemText(4, _translate("mainWindow", "Deuteronomy"))
        self.comboBox_2.setItemText(5, _translate("mainWindow", "Joshua "))
        self.comboBox_2.setItemText(6, _translate("mainWindow", "Judges"))
        self.comboBox_2.setItemText(7, _translate("mainWindow", "Ruth"))
        self.comboBox_2.setItemText(8, _translate("mainWindow", "1 Samuel"))
        self.comboBox_2.setItemText(9, _translate("mainWindow", "2 Samuel"))
        self.comboBox_2.setItemText(10, _translate("mainWindow", "1 Kings"))
        self.comboBox_2.setItemText(11, _translate("mainWindow", "2 Kings"))
        self.comboBox_2.setItemText(12, _translate("mainWindow", "1 Chronicles"))
        self.comboBox_2.setItemText(13, _translate("mainWindow", "2 Chronicles"))
        self.comboBox_2.setItemText(14, _translate("mainWindow", "Ezra"))
        self.comboBox_2.setItemText(15, _translate("mainWindow", "Nehemiah"))
        self.comboBox_2.setItemText(16, _translate("mainWindow", "Esther"))
        self.comboBox_2.setItemText(17, _translate("mainWindow", "Psalms"))
        self.comboBox_2.setItemText(18, _translate("mainWindow", "Proverbs"))
        self.comboBox_2.setItemText(19, _translate("mainWindow", "Ecclesiastes"))
        self.comboBox_2.setItemText(20, _translate("mainWindow", "Song of Songs"))
        self.comboBox_2.setItemText(21, _translate("mainWindow", "Isaiah"))
        self.comboBox_2.setItemText(22, _translate("mainWindow", "Jeremiah"))
        self.comboBox_2.setItemText(23, _translate("mainWindow", "Lamentations"))
        self.comboBox_2.setItemText(24, _translate("mainWindow", "Ezekiel"))
        self.comboBox_2.setItemText(25, _translate("mainWindow", "Daniel"))
        self.comboBox_2.setItemText(26, _translate("mainWindow", "Hosea"))
        self.comboBox_2.setItemText(27, _translate("mainWindow", "Joel"))
        self.comboBox_2.setItemText(28, _translate("mainWindow", "Amos"))
        self.comboBox_2.setItemText(29, _translate("mainWindow", "Obadiah"))
        self.comboBox_2.setItemText(30, _translate("mainWindow", "Jonah"))
        self.comboBox_2.setItemText(31, _translate("mainWindow", "Micah"))
        self.comboBox_2.setItemText(32, _translate("mainWindow", "Nahum"))
        self.comboBox_2.setItemText(33, _translate("mainWindow", "Habakkuk"))
        self.comboBox_2.setItemText(34, _translate("mainWindow", "Zephaniah"))
        self.comboBox_2.setItemText(35, _translate("mainWindow", "Haggai"))
        self.comboBox_2.setItemText(36, _translate("mainWindow", "Zechariah"))
        self.comboBox_2.setItemText(37, _translate("mainWindow", "Malachi"))
        self.comboBox_2.setItemText(38, _translate("mainWindow", "Matthew"))
        self.comboBox_2.setItemText(39, _translate("mainWindow", "Mark"))
        self.comboBox_2.setItemText(40, _translate("mainWindow", "Luke"))
        self.comboBox_2.setItemText(41, _translate("mainWindow", "John"))
        self.comboBox_2.setItemText(42, _translate("mainWindow", "Acts"))
        self.comboBox_2.setItemText(43, _translate("mainWindow", "Romans"))
        self.comboBox_2.setItemText(44, _translate("mainWindow", "1 Corinthians"))
        self.comboBox_2.setItemText(45, _translate("mainWindow", "2 Corinthians"))
        self.comboBox_2.setItemText(46, _translate("mainWindow", "Galatians"))
        self.comboBox_2.setItemText(47, _translate("mainWindow", "Ephesians"))
        self.comboBox_2.setItemText(48, _translate("mainWindow", "Philippians"))
        self.comboBox_2.setItemText(49, _translate("mainWindow", "Colossians"))
        self.comboBox_2.setItemText(50, _translate("mainWindow", "1 Thessalonians"))
        self.comboBox_2.setItemText(51, _translate("mainWindow", "2 Thessalonians"))
        self.comboBox_2.setItemText(52, _translate("mainWindow", "1 Timothy"))
        self.comboBox_2.setItemText(53, _translate("mainWindow", "2 Timothy"))
        self.comboBox_2.setItemText(54, _translate("mainWindow", "Titus"))
        self.comboBox_2.setItemText(55, _translate("mainWindow", "Philemon"))
        self.comboBox_2.setItemText(56, _translate("mainWindow", "Hebrews"))
        self.comboBox_2.setItemText(57, _translate("mainWindow", "James"))
        self.comboBox_2.setItemText(58, _translate("mainWindow", "1 Peter"))
        self.comboBox_2.setItemText(59, _translate("mainWindow", "2 Peter"))
        self.comboBox_2.setItemText(60, _translate("mainWindow", "1 John"))
        self.comboBox_2.setItemText(61, _translate("mainWindow", "2 John"))
        self.comboBox_2.setItemText(62, _translate("mainWindow", "3 John"))
        self.comboBox_2.setItemText(63, _translate("mainWindow", "Jude"))
        self.comboBox_2.setItemText(64, _translate("mainWindow", "Revelation"))
        self.Book_voiceInput.setToolTip(_translate("mainWindow", "Speak out the book name"))
        self.Book_voiceInput.setText(_translate("mainWindow", "Voice Input"))
        self.Book_voiceInput.setShortcut(_translate("mainWindow", "Ctrl+B"))
        self.label_4.setText(_translate("mainWindow", "Chapter:"))
        self.Chapter_VoiceInput.setToolTip(_translate("mainWindow", "Speak the Chapter number"))
        self.Chapter_VoiceInput.setText(_translate("mainWindow", "Voice Input"))
        self.Chapter_VoiceInput.setShortcut(_translate("mainWindow", "Ctrl+Shift+C"))
        self.label_3.setText(_translate("mainWindow", "Verse:"))
        self.Verse_VoiceInput.setToolTip(_translate("mainWindow", "Speak the Verse"))
        self.Verse_VoiceInput.setText(_translate("mainWindow", "Voice Input"))
        self.Verse_VoiceInput.setShortcut(_translate("mainWindow", "Ctrl+Shift+V"))
        self.Ok_button.setText(_translate("mainWindow", "OK"))
        self.Cancel_button.setText(_translate("mainWindow", "Cancel"))
        self.menuFile.setTitle(_translate("mainWindow", "File"))
        self.menuHelp.setTitle(_translate("mainWindow", "Help"))
        self.actionAbout.setText(_translate("mainWindow", "About"))
        self.actionShortcuts.setText(_translate("mainWindow", "Shortcuts"))
        self.actionClose.setText(_translate("mainWindow", "Close"))
        self.actionCut.setText(_translate("mainWindow", "Cut"))
        self.actionCopy.setText(_translate("mainWindow", "Copy"))
        self.actionPaste.setText(_translate("mainWindow", "Paste"))
        self.actionHelp.setText(_translate("mainWindow", "Help"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
