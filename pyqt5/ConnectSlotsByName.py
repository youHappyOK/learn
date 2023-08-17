from PyQt5 import QtCore, QtWidgets

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('信号与槽连接示例')
        self.setGeometry(300, 300, 300, 200)

        self.layout = QtWidgets.QVBoxLayout(self)

        self.button = QtWidgets.QPushButton('点击', self)
        self.button.setObjectName('myButton')  # 设置对象名称，用于自动连接


        self.lineText = QtWidgets.QLineEdit(self)
        self.lineText.setObjectName('myLineText')

        self.layout.addWidget(self.button)
        self.layout.addWidget(self.lineText)

        layout2 = QtWidgets.QHBoxLayout()
        self.lineT2 = QtWidgets.QLineEdit()
        self.lineT3 = QtWidgets.QLineEdit()
        layout2.addWidget(self.lineT2)
        layout2.addWidget(self.lineT3)

        self.show()

        QtCore.QMetaObject.connectSlotsByName(self)

    # @QtCore.pyqtSlot()
    def on_myButton_clicked(self):
        print('按钮被点击了')
        # 在这里编写按钮点击后的逻辑

    # @QtCore.pyqtSlot(str)
    def on_myLineText_textChanged(self, text):
        print('so nvidia fxxk you', text)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.show()

    app.exec_()