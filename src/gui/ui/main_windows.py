#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter as tk  # 使用Tkinter前需要先导入
import tkinter.filedialog

from functions.log4py import print_log
from gui.ui.globel_varable import set_value
from gui.ui.globel_varable import get_value

from gui.ui.select_bills import chooes_bills_folder

from functions.read_table import ReadTransactionTable
from modules.transaction_tools import analysis_all_bills


def do_job():
    
    print("Do some job.")
    
   
def analysis_bills():
    
    bills_files = get_value("bills_files")
    if len(bills_files) == 0:
        print("No bills files.")
    else:
        print("Bills files: " + str(bills_files))
    
    bills_folder_path = get_value("bills_folder")
        
    taregt_transactions = analysis_all_bills(target_csv_files=bills_files,
                                             csv_folder_path=bills_folder_path)
    
    print("Target transactions: " + str(len(taregt_transactions)))
    
    
    
def run_main_windows():

    # 第1步，实例化object，建立窗口window
    window = tk.Tk()
    
    # 第2步，给窗口的可视化起名字
    window.title('My Window')
    
    # 第3步，设定窗口的大小(长 * 宽)
    window.geometry('500x300')  # 这里的乘是小x
    
    
    # 第5步，创建一个菜单栏，这里我们可以把他理解成一个容器，在窗口的上方
    menubar = tk.Menu(window)

    # 第6步，创建一个File菜单项（默认不下拉，下拉内容包括New，Open，Save，Exit功能项）
    filemenu = tk.Menu(menubar, tearoff=0)
    # 将上面定义的空菜单命名为File，放在菜单栏中，就是装入那个容器中
    menubar.add_cascade(label='File', menu=filemenu)
    
    # 在File中加入New、Open、Save等小菜单，即我们平时看到的下拉菜单，每一个小菜单对应命令操作。
    filemenu.add_command(label='New', command=do_job)
    filemenu.add_command(label='Open', command=do_job)
    filemenu.add_command(label='Save', command=do_job)
    
    # 第8步，创建第二级菜单，即菜单项里面的菜单
    submenu = tk.Menu(filemenu) # 和上面定义菜单一样，不过此处实在File上创建一个空的菜单
    filemenu.add_cascade(label='Import', menu=submenu, underline=0) # 给放入的菜单submenu命名为Import
    
    # 第9步，创建第三级菜单命令，即菜单项里面的菜单项里面的菜单命令（有点拗口，笑~~~）
    submenu.add_command(label='账单', command=chooes_bills_folder)     # 这里和上面创建原理也一样，在Import菜单项中加入一个小菜单命令Submenu_1
    submenu.add_command(label='微信账单', command=do_job)               # 这里和上面创建原理也一样，在Import菜单项中加入一个小菜单命令Submenu_1
    submenu.add_command(label='支付宝账单', command=do_job)              # 这里和上面创建原理也一样，在Import菜单项中加入一个小菜单命令Submenu_1
    
    filemenu.add_separator()    # 添加一条分隔线
    filemenu.add_command(label='Exit', command=window.quit) # 用tkinter里面自带的quit()函数

    # # 第7步，创建一个Edit菜单项（默认不下拉，下拉内容包括Cut，Copy，Paste功能项）
    # editmenu = tk.Menu(menubar, tearoff=0)
    # # 将上面定义的空菜单命名为 Edit，放在菜单栏中，就是装入那个容器中
    # menubar.add_cascade(label='Edit', menu=editmenu)
    
    # # 同样的在 Edit 中加入Cut、Copy、Paste等小命令功能单元，如果点击这些单元, 就会触发do_job的功能
    # editmenu.add_command(label='Cut', command=do_job)
    # editmenu.add_command(label='Copy', command=do_job)
    # editmenu.add_command(label='Paste', command=do_job)
    
    # 第11步，创建菜单栏完成后，配置让菜单栏menubar显示出来
    window.config(menu=menubar)
    
    # 第4步，在图形界面上设定标签
    # l = tk.Label(window, text='你好,欢迎您查看自己的账单', bg='green', font=('Arial', 12), width=30, height=2)
    # # 说明： bg为背景，font为字体，width为长，height为高，这里的长和高是字符的长和高，比如height=2,就是标签有2个字符这么高
    # l.pack()

    # # 第4步，在图形界面上设定输入框控件entry并放置控件
    # bills_file_path = tk.Entry(window, show=None, font=('Arial', 14))  # 显示成明文形式
    # bills_file_path.pack()
    
    # btn = tk.Button(window,text="弹出选择文件对话框",command=chooes_bills_folder)
    # btn.pack()
    
    analysis_bills_btn = tk.Button(window,text="解析账单文件",command=analysis_bills)
    analysis_bills_btn.pack()
    
    # 第5步，主窗口循环显示
    window.mainloop()
   
   
# if __name__ == '__main__':
#     run_main_windows()