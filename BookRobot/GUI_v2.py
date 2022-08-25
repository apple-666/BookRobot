# @Time: 2022/8/22 21:48
# @Author: DoubleApple

from PySide2.QtWidgets import QApplication,QMessageBox
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile
import AutoBook_v2 as autobook


class RobotUi:
    def __init__(self):
        qfile_state = QFile("D:/apple/workspace/BookRobot/BookRobot/ui/robot.ui")
        qfile_state.open(QFile.ReadOnly)
        qfile_state.close()
        self.ui = QUiLoader().load(qfile_state)  # 界面对象
        self.ui.pushButton.clicked.connect(self.order)

    def test(self):
        print('has !')

    def order(self):
        user_auth = self.ui.plainTextEdit.toPlainText()
        user_date = self.ui.plainTextEdit_2.toPlainText()
        user_type = self.ui.plainTextEdit_4.toPlainText()
        print(user_auth)
        print(user_date)
        print(user_type)
        autobook.get_info(user_auth, user_date, user_type)
        # print(autobook.get_all_stadium())
        # print(autobook.find_free_field())
        result = autobook.kill_order()
        self.ui.plainTextEdit_3.appendPlainText("拿到了" + str(len(result)) + "个场地")
        self.ui.plainTextEdit_3.appendPlainText("\n" + str(result))


app = QApplication([])
robot = RobotUi()
robot.ui.show()
app.exec_()
