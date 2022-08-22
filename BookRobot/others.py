# @Time: 2022/8/22 21:48
# @Author: DoubleApple

import tkinter
# import tkMessageBox

top = tkinter.Tk()


def helloCallBack():
    # tkMessageBox.showinfo("Hello Python", "Hello Runoob")
    print('1')

B = tkinter.Button(top, text="点我", command=helloCallBack)

B.pack()
top.mainloop()