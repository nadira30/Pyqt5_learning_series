import pkg_resources
import pandas as pd
import seaborn as sns
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (
    QLabel,
    QWidget,
    QDesktopWidget,
    QCheckBox,
    QVBoxLayout,
    QPushButton,
    QDialog,
    QLineEdit,
    QScrollArea,
    QMainWindow, QSpacerItem, QSizePolicy,
)


class ViewProject(QMainWindow):
    """

    """

    def __init__(self):
        super().__init__()

        self.verticalSpacer = None
        self.widget = QWidget()
        self.my_label = None
        self.correlation_bttn = None
        self.grid_layout = None
        self.dlg = None
        self.btn = None
        self.pixmap = None
        self.graph_name = "scatter_plot.png"
        self.corr_variables = []
        self.checkbox = []

        self.searchbar = QLineEdit()
        self.searchbar.setPlaceholderText("Search for a specific variable")
        self.searchbar.textChanged.connect(self.update_display)
        self.scroll_area = QScrollArea()

        self.df = pd.read_csv(pkg_resources.resource_filename('Pyqt_signals_slots.data_viz_app.core', 'data.csv'))

        self.create_mainwindow()

    def create_mainwindow(self):
        """
        Creating a window displaying all the header in the csv file defined above. Give  the user the opportunity to
        check multiple  variables and display a scatter plot analysing the correlation between the selected field.
        :return:
        """

        self.setWindowTitle('Statistical Analysis App')
        self.setFixedSize(500, 600)
        self.my_label = QLabel(
            'The dependant and independent variables of your research are displayed below. Please select or serach for '
            'the variables to analyse statistically. ')
        self.my_label.adjustSize()
        self.my_label.setWordWrap(True)
        self.my_label.setStyleSheet("font: bold 14px")

        self.grid_layout = QVBoxLayout()
        self.grid_layout.setSpacing(2)
        self.grid_layout.addWidget(self.my_label)
        self.grid_layout.addWidget(self.searchbar)

        # Going through the array of header and create a checkbox for each one
        for idx in self.df.columns:
            self.btn = QCheckBox(idx, self)
            self.btn.setStyleSheet("font: 14px")
            self.btn.stateChanged.connect(self.clickBox)
            self.grid_layout.addWidget(self.btn)
            self.checkbox.append(self.btn)

        # Button creating the graph
        self.correlation_bttn = QPushButton('Analyse Variables')
        self.correlation_bttn.clicked.connect(self.graph_dialog)
        self.grid_layout.addWidget(self.correlation_bttn)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.grid_layout.addItem(self.verticalSpacer)
        self.widget.setLayout(self.grid_layout)

        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setWidget(self.widget)

        self.setCentralWidget(self.scroll_area)

        self.center()

    def center(self):
        """
            Center the window at the middle of the user screen
        :return:
        """
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def clickBox(self):
        """
            Slot for the checkboxes. Also, not sure why checked and unchecked are similar. I feel like it is
            behaving more as a button than a checkbox.
        :return:
        """
        checked_elelents = []
        for box in self.checkbox:
            if box.isChecked():
                box.setStyleSheet("color: #00BEEF; font: bold 14px")
                checked_elelents.append(box.text())
            else:
                box.setStyleSheet("color: white; font: bold 14px")
        self.corr_variables = checked_elelents

    def update_display(self, text):
        """
        Adding a search widget so the user can search for a specific variable. If any variable is found,
        it is displayed otherwise hide.
        :param text: user input in the search bar
        :return:
        """
        for checkbox in self.checkbox:
            if text.lower() in checkbox.text().lower():
                checkbox.show()
            else:
                checkbox.hide()

    def create_correlation_graph(self):
        """
        Using seaborn library to create a scatter plot of all the selected variables and save the figure in the
        project folder.
        #ToDO: Determine the p-value using the Anova-test and display a conclusion for the user to
        confirm if they are correlated or not.
        :return:
        """
        try:
            print(self.corr_variables)
            analysis_graph = sns.PairGrid(self.df, vars=self.corr_variables, hue='diagnosis')
            analysis_graph.map(sns.scatterplot, color='purple')
            analysis_graph.add_legend()
            analysis_graph.savefig(self.graph_name, dpi=70)
        except Exception as ex:
            pass

    def graph_dialog(self):
        """
            Creating a dialog and displaying the saved graph in the dialog.
        :return:
        """
        self.create_correlation_graph()
        self.dlg = QDialog()
        self.dlg.setWindowTitle("Data Visualization")
        pic = QLabel(self.dlg)
        pic.setMinimumSize(250, 250)
        self.pixmap = QPixmap(self.graph_name)
        pic.setPixmap(self.pixmap)
        pic.resize(self.pixmap.width(), self.pixmap.height())
        self.dlg.show()

    # TODO: make use of the code and gui folder by dividing the pyqt code from the graph, calculation, ...code
