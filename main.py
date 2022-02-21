
# Music List Generator by Yuzuru #

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QComboBox
from mutagen.mp3 import MP3, HeaderNotFoundError
import webbrowser
import os
import pathlib


class Ui_MainWindow(object):
    def __init__(self):
        """This __init__ method is to store and prepare for the rest of the code."""
        self.main_path = os.getcwd()
        self._music_extensions = ('Original Format', '.flac', '.m4a', '.mp3', '.ogg', '.oga', '.mogg', '.opus', '.raw', '.wav', '.wma', '.webm')
        self.music_fail = list()

    def setupUi(self, MainWindow):
        """Standard Code Generated from Qt Designer."""
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 500)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(20, 250, 461, 192))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setText("Once Executed, this program may freeze. Do not panic, this is part of the process."
                                 "\nIf you found any bugs, please contact Yuzuru via Github or Discord <Yuzuru#2897>"
                                 "\nProgress:")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(374, 10, 111, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda: self.load_directory())

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 10, 341, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setReadOnly(True)

        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(20, 50, 341, 181))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.load_dir_path(self.main_path)

        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(380, 60, 101, 17))
        self.radioButton.setObjectName("radioButton")

        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(380, 120, 101, 20))
        self.lineEdit_2.setStatusTip("")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(380, 180, 101, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        # self.pushButton_2.setEnabled(False)
        self.pushButton_2.clicked.connect(lambda: self.music_to_list())

        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.setGeometry(QtCore.QRect(380, 150, 101, 20))
        self.comboBox.addItems(self._music_extensions)
        self.comboBox.setEditable(False)

        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(380, 90, 91, 17))
        self.checkBox.setObjectName("checkBox")

        MainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 21))
        self.menubar.setObjectName("menubar")

        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")

        MainWindow.setMenuBar(self.menubar)

        self.actionCredits = QtWidgets.QAction(MainWindow)
        self.actionCredits.setObjectName("actionCredits")
        self.actionCredits.triggered.connect(lambda: self.action_guide())

        self.actionTutorial = QtWidgets.QAction(MainWindow)
        self.actionTutorial.setObjectName("actionTutorial")
        self.actionTutorial.triggered.connect(lambda: self.tutorial_guide())

        self.menuMenu.addAction(self.actionCredits)
        self.menuMenu.addAction(self.actionTutorial)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Music List YAML Creator"))

        self.lineEdit.setText(_translate("MainWindow", self.main_path))

        self.pushButton.setToolTip(_translate("MainWindow", "Load the Directory of your Desired Music"))
        self.pushButton.setText(_translate("MainWindow", "Load Directory"))

        self.textBrowser_2.setToolTip(_translate("MainWindow", "The List of Music Extensions in the Directory."))

        self.radioButton.setToolTip(_translate("MainWindow", "Turning this ON will not ignore the Directories and use them as music separators"))
        self.radioButton.setText(_translate("MainWindow", "Multi-Directory"))

        self.lineEdit_2.setWhatsThis(_translate("MainWindow", "Prefix"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Prefix"))

        self.pushButton_2.setText(_translate("MainWindow", "Execute"))

        self.comboBox.setWhatsThis(_translate("MainWindow", "File Extention for the YAML"))
        self.comboBox.setPlaceholderText(_translate("MainWindow", ".opus"))

        self.checkBox.setText(_translate("MainWindow", "AO2.8+?"))

        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))

        self.actionCredits.setText(_translate("MainWindow", "Github Page"))
        self.actionTutorial.setText(_translate("MainWindow", "Tutorial Document"))

    # === Function Lists === #

    # Links and Guide
    def action_guide(self):
        """Opens the Link to the Github Page."""
        url = "https://github.com/Yuzurukyun/ao-music-list-maker"
        webbrowser.open(url)

    def tutorial_guide(self):
        """Opens the Link to the Google Document Page."""
        url = "https://docs.google.com/document/d/11gmWUdRREEEPuU4NsORP6iznFtJgbPJbQCuPdhve19c/edit?usp=sharing"
        webbrowser.open(url)

    # Failure Message and Popups
    def failure_message(self):
        """If something failed, this will be displayed."""
        self.textBrowser.append("\nThe Following Failed:")
        for failed in self.music_fail:
            self.textBrowser.append(f"--> {failed}")
        self.textBrowser.append("\nMost likely due to not being an MP3 File or Corrupted.")

    def show_popup(self):
        msg = QMessageBox()
        msg.setWindowTitle("Task completed!")
        msg.setText(f"Your generated_music_list.yaml is ready!"
                    f"\nTotal Failures: {len(self.music_fail)}")
        msg.setIcon(QMessageBox.Information)
        msg.exec_()

    # Load Directories and Paths
    def load_directory(self):
        """This loads the Directory."""
        try:
            dir_path = QFileDialog.getExistingDirectory(None, "Open Directory", self.main_path)
            self.lineEdit.setText(dir_path)
            self.main_path = dir_path
        except Exception as e:
            raise e

        self.load_dir_path(dir_path)

    def load_dir_path(self, dir_path):
        """The continuation of loading the Directory. This is to display in the Text Browser."""
        result = os.listdir(dir_path)
        _directory = list()
        _music_files = list()
        _music_extensions = self._music_extensions

        for item in result:
            dir_check = os.path.isdir(f"{dir_path}\\{item}")
            if dir_check is True:
                _directory.append(f'[dir] {item}')
            else:
                if pathlib.Path(item).suffix in _music_extensions:
                    _music_files.append(item)

        list_result = _directory + _music_files

        self.textBrowser_2.setText('\n'.join(list_result))

    # The Process
    def music_check(self, _file):
        """This checks the length of the Music file. With the Attorney Online 2.8 Update, this is no longer needed.
        However, Danganronpa Online does not have this feature yet. So, both will be complemented."""
        _ao2_8_is_checked = self.checkBox.isChecked()

        if _ao2_8_is_checked:
            audio_length = -1

        else:
            try:
                audio = MP3(_file)
                audio_length = round(audio.info.length)
            except HeaderNotFoundError:
                self.music_fail.append(_file)
                audio_length = 0

        return audio_length

    def music_listing(self, given_dir, new_path, _prefix, _suffix):
        """This will generate the code for the music.yaml."""
        with open('generated_music_list.yaml', 'a+', encoding='utf-8') as music_yaml:
            for y in given_dir:
                if _suffix == "Original Format":
                    _suffix = pathlib.Path(y).suffix

                dir_check = os.path.isdir(f"{new_path}\\{y}")
                if dir_check:
                    continue

                if not pathlib.Path(y).suffix in self._music_extensions:
                    continue

                audio_length = self.music_check(f"{new_path}\\{y}")
                music_ = f'    - name: "{_prefix}{pathlib.Path(y).stem}{_suffix}"\n' \
                         f'      length: {audio_length} \n'

                music_yaml.write(music_)

                status_, msg_ = "SUCCESS", ""
                if audio_length == 0:
                    status_ = "FAILED"
                    msg_ = "Not an MP3 file or Corrupted."

                self.textBrowser.append(f"-> {_prefix}{pathlib.Path(y).stem}{_suffix} {status_}! {msg_}")

    def music_to_list(self):
        """This is the entire process from start to finish."""
        self.textBrowser.setText("Once Executed, this program may freeze. Do not panic, this is part of the process."
                                 "\nIf you found any bugs, please contact Yuzuru via Github or Discord <Yuzuru#2897>"
                                 "\nProgress:")
        self.music_fail = list()
        _multi_directory_is_checked = self.radioButton.isChecked()

        _prefix, _suffix = self.lineEdit_2.text(), self.comboBox.currentText()
        if _prefix:
            _prefix = f"{_prefix}/"

        count = 0
        current_dir = os.listdir(self.main_path)
        for x in current_dir:
            dir_check = os.path.isdir(f"{self.main_path}\\{x}")
            if not _multi_directory_is_checked:
                if dir_check:
                    continue
                with open('generated_music_list.yaml', 'w+', encoding='utf-8') as music_yaml:
                    _category = f"- category: -- General --\n" \
                                f"  songs: \n"
                    music_yaml.write(_category)

                self.music_listing(current_dir, self.main_path, _prefix, _suffix)
                break

            else:
                if not dir_check:
                    continue

                if count == 0:
                    with open('generated_music_list.yaml', 'w+', encoding='utf-8') as music_yaml:
                        _category = f"- category: -- {x} --\n" \
                                    f"  songs: \n"
                        music_yaml.write(_category)
                else:
                    with open('generated_music_list.yaml', 'a+', encoding='utf-8') as music_yaml:
                        _category = f"- category: -- {x} --\n" \
                                    f"  songs: \n"
                        music_yaml.write(_category)

                new_path = f"{self.main_path}\\{x}"
                new_dir = os.listdir(new_path)
                self.music_listing(new_dir, new_path, _prefix, _suffix)
                count += 1

        if self.music_fail:
            self.failure_message()
        self.show_popup()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
