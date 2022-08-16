import logging
import sys

import qdarkstyle
from PyQt5.QtWidgets import QApplication

from Pyqt_signals_slots.data_viz_app.gui.view_project import ViewProject
logger = logging.getLogger()


def main():
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    view_project = ViewProject()
    view_project.show()
    app.exec_()


if __name__ == '__main__':
    try:
        main()
    except Exception as ex:
        logger.exception('Critical error encountered')
