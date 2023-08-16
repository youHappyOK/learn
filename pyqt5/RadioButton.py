import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QRadioButton, QLabel

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        radio_button1 = QRadioButton("选项1")
        radio_button2 = QRadioButton("选项2")
        radio_button3 = QRadioButton("选项3")
        self.label = QLabel("选项1", self)

        layout.addWidget(radio_button1)
        layout.addWidget(radio_button2)
        layout.addWidget(radio_button3)
        layout.addWidget(self.label)

        radio_button1.setChecked(True)  # 设置默认选中状态

        def on_radio_button_clicked():
            selected_option = "选项1"
            if radio_button2.isChecked():
                selected_option = "选项2"
            elif radio_button3.isChecked():
                selected_option = "选项3"
            self.label.setText(f"你选择了：{selected_option}")

        radio_button1.clicked.connect(on_radio_button_clicked)
        radio_button2.clicked.connect(on_radio_button_clicked)
        radio_button3.clicked.connect(on_radio_button_clicked)

        self.setLayout(layout)
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('radioButton')
        self.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())