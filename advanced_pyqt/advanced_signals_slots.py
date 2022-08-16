from PyQt5.QtCore import pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import (
    QWidget,
    QPushButton,
    QHBoxLayout,
    QMessageBox,
    QMainWindow
)


class QSuperPushButton(QPushButton):
    """
    Subclassing QPushbutton to create QSuperPushButton class
    """
    super_clicked = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.clicked.connect(self.emit_signal)

    @pyqtSlot()
    def emit_signal(self):
        self.super_clicked.emit(self.text())


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.button3 = None
        self.button2 = None
        self.button1 = None
        self.widget = QWidget()
        self.layout = QHBoxLayout()
        self.create_main_window()

    def create_main_window(self):
        """
        Creating the main window and adding the button
        :return:
        """
        self.button1 = QSuperPushButton()
        self.button1.setText("Button 1")
        self.layout.addWidget(self.button1)
        self.button1.super_clicked.connect(self.button_clicked)

        self.button2 = QSuperPushButton()
        self.button2.setText("Button 2")
        self.layout.addWidget(self.button2)
        self.button2.super_clicked.connect(self.button_clicked)

        self.button3 = QSuperPushButton()
        self.button3.setText(f"Button 3")
        self.layout.addWidget(self.button3)
        self.button3.super_clicked.connect(self.button_clicked)

        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)
        self.setWindowTitle("Advanced PyQt Learning")
        self.setFixedSize(300, 100)

    @pyqtSlot(str)
    def button_clicked(self, text):
        """
        Button slot connection
        :param text: button title passed for the message box
        :return:
        """

        QMessageBox.information(self, "SuperClicked Button",
                                f"SuperClicked  {text} was clicked",
                                QMessageBox.Cancel)
