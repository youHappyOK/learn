import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QPushButton, QHBoxLayout
from PyQt5.QtCore import Qt

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def clear(self):
        # 这会将表格的行数设置为0，从而清空所有的内容，但是保留表格的行数和表头。这样，您可以在清空内容的同时保留原有的行
        self.table_widget.setRowCount(0)

    def addRow(self):
        row_position = self.table_widget.rowCount()
        self.table_widget.insertRow(row_position)

        # Fill the new row with data (you can modify this as needed)
        data = ["New Data 1", "New Data 2", "New Data 3"]
        for col, value in enumerate(data):
            item = QTableWidgetItem(value)
            item.setTextAlignment(Qt.AlignCenter) # Set alignment to center
            self.table_widget.setItem(row_position, col, item)

    def initUI(self):
        layoutV = QVBoxLayout()
        self.table_widget = QTableWidget()
        self.table_widget.setRowCount(3)  # 设置行数
        self.table_widget.setColumnCount(10)  # 设置列数
        buttonAdd = QPushButton("添加一行")
        buttonAdd.clicked.connect(self.addRow)
        buttonClear = QPushButton("清空")
        buttonClear.clicked.connect(self.clear)
        layoutV.addWidget(self.table_widget)
        layoutV.addStretch(1)
        layoutH = QHBoxLayout()
        layoutH.addStretch(1)
        layoutH.addWidget(buttonAdd)
        layoutH.addWidget(buttonClear)
        layoutV.addLayout(layoutH)


        # 表头
        self.table_widget.setHorizontalHeaderLabels(["线程", "句柄", "运行状态", "账号", "密码", "区服", "等级", "账号状态", "金币", "运行时间"])

        # 添加数据到单元格
        data = [
            ["数据10", "数据11", "数据12", "数据13", "数据14", "数据15", "数据16", "数据17", "数据18", "数据19"],
            ["数据20", "数据21", "数据22", "数据23", "数据24", "数据25", "数据26", "数据27", "数据28", "数据29"],
            ["数据30", "数据31", "数据32", "数据33", "数据34", "数据35", "数据36", "数据37", "数据38", "数据39"],
        ]

        for row, rowData in enumerate(data):
            for col, value in enumerate(rowData):
                item = QTableWidgetItem(value)
                item.setTextAlignment(Qt.AlignCenter)  # Set alignment to center
                self.table_widget.setItem(row, col, item)

        self.setGeometry(300, 300, 1100, 500)
        self.setWindowTitle("so fuck you nvida")
        self.setLayout(layoutV)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())