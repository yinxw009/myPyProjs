# %% [markdown]
# 在QtDesigner中布局、signal&slot、菜单工具栏、创建主窗口
# <PyQt5教程，来自网易云课堂, bilibili, 新建文本文档-1>

# %%
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

# %% [markdown]
# 5. 创建主窗口        <P23 课时24>

# %%
from PyQt5.QtGui import QIcon
class FirstMainWin(QMainWindow):
    def __init__(self, parent=None):
        super(FirstMainWin,self).__init__(parent)
        
        #设置主窗口的标题
        self.setWindowTitle('第一个主窗口应用')

        #设置窗口的尺寸
        self.resize(400,300)

        self.status = self.statusBar()

        self.status.showMessage('只存在5秒的消息',5000)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # app.setWindowIcon(./)
    main = FirstMainWin()
    main.show()

    sys.exit(app.exec_())


# %% [markdown]
# 4. 为窗口添加菜单和工具栏        <P22 课时23>

# %%
import guiQt5ManuBar
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = guiQt5ManuBar.Ui_MainWindow()
    #向主窗口上添加控件
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())

# %% [markdown]
# 3. Signal & Slot设置        <P21 课时22>

# %%
import guiQt5Slot
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = guiQt5Slot.Ui_MainWindow()
    #向主窗口上添加控件
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())

# %% [markdown]
# 2. 布局Layout        <P7 课时08 ~ P20 课时21>

# %% [markdown]
# 1. 初识       <P1 课时01 ~ P6 课时07>


