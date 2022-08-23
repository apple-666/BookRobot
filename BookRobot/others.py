# @Time: 2022/8/22 21:48
# @Author: DoubleApple

from PySide2.QtWidgets import QApplication,QMessageBox
from PySide2.QtUiTools import QUiLoader
from  PySide2.QtCore import QFile


class RobotUi:
    def __init__(self):
        qfile_state = QFile("ui/robot.ui")
        qfile_state.open(QFile.ReadOnly)
        qfile_state.close()
        self.ui = QUiLoader().load(qfile_state)  # 界面对象


app = QApplication([])
robot = RobotUi()
robot.ui.show()
app.exec_()
