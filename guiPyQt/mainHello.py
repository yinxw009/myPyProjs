import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

import testHello

def click_success():
    print("Hahahaha, wo zhongyu chenggong le!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = testHello.Ui_MainWindow()
    #向主窗口上添加控件
    ui.setupUi(MainWindow)

    MainWindow.show()

    ui.pushButton.clicked.connect(click_success)

    sys.exit(app.exec_())