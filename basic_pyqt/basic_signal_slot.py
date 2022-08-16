from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QLabel,
    QCheckBox,
    QGridLayout,
    QWidget,
    QMainWindow,
)


class BasicSignalSlots(QMainWindow):
    """
        Creating a Pyqt widget with a checkbox and a label. When the checkbox is checked the label text is set to checked,
        otherwise it is set Unchecked.
    """

    def __init__(self):
        super().__init__()
        self.checkbox_2 = None
        self.checkbox_3 = None
        self.checkbox_1 = None
        self.widget = QWidget()
        self.layout = QGridLayout()
        self.label = QLabel()
        self.create_main_window()

    def create_main_window(self):
        self.setWindowTitle('Basic Signals and Slots')
        self.setMinimumSize(300, 150)

        self.label.setStyleSheet('color: #FFF80A; font: bold 12px')
        self.label.setWordWrap(True)

        self.checkbox_1 = QCheckBox("Checkbox 1")
        self.layout.addWidget(self.checkbox_1)
        self.checkbox_1.stateChanged.connect(self.clickbox)

        self.checkbox_2 = QCheckBox("Checkbox 2")
        self.layout.addWidget(self.checkbox_2)
        self.checkbox_2.stateChanged.connect(self.clickbox)

        self.checkbox_3 = QCheckBox("Checkbox 3")
        self.layout.addWidget(self.checkbox_3)
        self.checkbox_3.stateChanged.connect(self.clickbox)

        self.layout.addWidget(self.label)
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)

    def clickbox(self, checkbox_checked):
        """
            Slot connection to establish if the checkbox is checked or not.
        :return:
        """
        if checkbox_checked == Qt.Checked:
            self.label.setText("A checkbox was just checked")
        else:
            self.label.setText("A checkbox was just unchecked")
