from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QTabWidget, QLabel, QLineEdit

if __name__ == '__main__':
    app = QApplication([])

    # 创建主窗口
    mainWindow = QMainWindow()
    centralWidget = QWidget(mainWindow)  # 创建中心部件
    mainWindow.setCentralWidget(centralWidget)  # 设置中心部件
    mainLayout = QVBoxLayout(centralWidget)  # 在中心部件上设置布局

    # 创建QTabWidget
    tabWidget = QTabWidget()
    mainLayout.addWidget(tabWidget)

    # 创建tab页1
    tab1 = QWidget()
    tabLayout1 = QVBoxLayout()
    tab1.setLayout(tabLayout1)
    # 添加需要的控件，例如：
    label1 = QLabel("Label 1")
    lineEdit1 = QLineEdit()
    tabLayout1.addWidget(label1)
    tabLayout1.addWidget(lineEdit1)
    # 将tab页1添加到QTabWidget中
    tabWidget.addTab(tab1, "Tab 1")

    # 创建tab页2
    tab2 = QWidget()
    tabLayout2 = QVBoxLayout()
    tab2.setLayout(tabLayout2)
    # 添加需要的控件，例如：
    label2 = QLabel("Label 2")
    lineEdit2 = QLineEdit()
    tabLayout2.addWidget(label2)
    tabLayout2.addWidget(lineEdit2)
    # 将tab页2添加到QTabWidget中
    tabWidget.addTab(tab2, "Tab 2")

    mainWindow.show()
    app.exec_()
