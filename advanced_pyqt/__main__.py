import logging
import sys

import qdarkstyle
from PyQt5.QtWidgets import QApplication

from advanced_pyqt.advanced_signals_slots import MainWindow
logger = logging.getLogger()


def main():
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    advanced_signal_slot = MainWindow()
    advanced_signal_slot.show()
    app.exec_()


if __name__ == '__main__':
    try:
        main()
    except Exception as ex:
        logger.exception('Critical error encountered')
