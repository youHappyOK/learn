import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTabWidget, QLabel

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        tab_widget = QTabWidget()
        tab1 = QWidget()
        tab2 = QWidget()
        tab_widget.addTab(tab1, "标签页1")
        tab_widget.addTab(tab2, "标签页2")

        tab1_layout = QVBoxLayout()
        label1 = QLabel("这是标签页1的内容")
        tab1_layout.addWidget(label1)
        tab1.setLayout(tab1_layout)

        tab2_layout = QVBoxLayout()
        label2 = QLabel("这是标签页2的内容")
        tab2_layout.addWidget(label2)
        tab2.setLayout(tab2_layout)

        layout.addWidget(tab_widget)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('TabWidget')
        self.setLayout(layout)
        self.show()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())