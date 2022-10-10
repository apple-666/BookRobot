# @Time: 2022/8/22 21:48
# @Author: DoubleApple

from PySide2.QtWidgets import QApplication, QMessageBox, QDateTimeEdit
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile, QDateTime
import AutoBook_v2 as autobook


user_date = ''
user_type = ''
user_count = 2

class RobotUi:
    def __init__(self):
        global user_date
        # qfile = QFile("D:/apple/workspace/BookRobot/BookRobot/ui/robot.ui")
        qfile = QFile("ui/robot.ui")
        # qfile = QFile("ui_save/robot_t.ui")
        qfile.open(QFile.ReadOnly)
        qfile.close()
        self.ui = QUiLoader().load(qfile)  # 界面对象

        # 初始化按钮选项
        self.ui.radioButton_type2.setChecked(True)
        self.ui.radioButton_count2.setChecked(True)
        self.ui.dateEdit.setDateTime(QDateTime.currentDateTime())

        # 获取选项信息
        # 1 date
        self.ui.dateEdit.dateChanged.connect(self.getChangingDate)
        # 2 球场类型
        self.ui.radioButton_type1.clicked.connect(lambda: self.getChangingType(self.ui.radioButton_type1))
        self.ui.radioButton_type2.clicked.connect(lambda: self.getChangingType(self.ui.radioButton_type2))
        # 3 球场个数
        self.ui.radioButton_count1.clicked.connect(lambda: self.getChangingCount(self.ui.radioButton_count1))
        self.ui.radioButton_count2.clicked.connect(lambda: self.getChangingCount(self.ui.radioButton_count2))

        self.ui.pushButton_request.clicked.connect(self.order)

    def getChangingDate(self):
        global user_date
        user_date = self.ui.dateEdit.date().toString('yyyy-MM-dd')
        print(user_date)

    def getChangingType(self, btn):
        global user_type
        user_type = btn.text()
        print(user_type)

    def getChangingCount(self, btn):
        global user_count
        user_count = btn.text()
        print(user_count)

    def test(self):
        print('has !')

    def order(self):
        global user_date, user_type, user_count
        user_auth = self.ui.user_auth.toPlainText()

        autobook.get_info(user_auth, user_date, user_type, user_count)
        # print(autobook.get_all_stadium())
        # print(autobook.find_free_field())
        result = autobook.kill_order()
        self.ui.plainTextEdit_3.appendPlainText("拿到了" + str(len(result)) + "个场地")
        self.ui.plainTextEdit_3.appendPlainText("\n" + str(result))


app = QApplication([])
robot = RobotUi()
robot.ui.show()
app.exec_()
