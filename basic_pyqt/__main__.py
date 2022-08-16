import logging
import sys

import qdarkstyle
from PyQt5.QtWidgets import QApplication

from basic_pyqt.basic_signal_slot import BasicSignalSlots
logger = logging.getLogger()


def main():
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    basic_signal_slots = BasicSignalSlots()
    basic_signal_slots.show()
    app.exec_()


if __name__ == '__main__':
    try:
        main()
    except Exception as ex:
        logger.exception('Critical error encountered')
