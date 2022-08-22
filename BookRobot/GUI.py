# @Time: 2022/8/22 21:30
# @Author: DoubleApple

import tkinter as tk
import AutoBook_v2 as autobook_v2

root = tk.Tk()
root.title('BookRobot')
root.geometry('480x720')

label = tk.Label(root, text='欢迎进入 AutoBook 软件', bg='orange', font=('Arial', 12))
label.grid(row=0, sticky='w')
l1 = tk.Label(root, text='输入用户authorization')
l1.grid(row=1, sticky='w')
l2 = tk.Label(root, text='输入要预订的日期')
l2.grid(row=2, sticky='w')
entry_auth = tk.Entry(root, width=50)
entry_auth.grid(row=1, sticky='e')
entry_date = tk.Entry(root, width=50)
entry_date.grid(row=2, sticky='e')


def text_grid():
    i = 0
    for i in range(10):
        bt = tk.Button(root, text="1", fg='black', bg="orange")
        bt.grid(column=i)
        i += 1
        print(bt.grid_info())



def order():
    print('we can')


def insert_info():
    auth = entry_auth.get()
    date = entry_date.get()
    autobook_v2.get_info(auth, date)
    # 打印结果 kill_order()
    # print(get_all_stadium())
    # print(get_order_date())
    # print(find_free_field())
    # print(get_order_date())
    # print(kill_order())
    result = autobook_v2.get_all_stadium()
    text.insert('end', result)


btn = tk.Button(root, text='预购场地', command=insert_info)
btn.grid(row=3, sticky='w')

l3 = tk.Label(root, text="获取的结果：")
l3.grid(row=4, sticky='w')
text = tk.Text(root, height=50)
text.grid(row=5, column=0)
root.mainloop()
