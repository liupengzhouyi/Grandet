#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 使用Tkinter前需要先导入

import tkinter as tk  
import tkinter.filedialog
from tkinter import ttk
from tkinter import *

from functions.log4py import print_log
from gui.ui.globel_varable import set_value
from gui.ui.globel_varable import get_value

from gui.ui.select_bills import chooes_bills_folder
from gui.ui.frist_page import create_grandet_bills_window
from gui.ui.help import show_help

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
    
    
def add_file(filemenu: tk.Menu, window: tk.Tk) -> tk.Menu:
    
    # 第1步，创建第二级菜单，即菜单项里面的菜单
    submenu = tk.Menu(filemenu) # 和上面定义菜单一样，不过此处实在File上创建一个空的菜单
    filemenu.add_cascade(label='Import', menu=submenu, underline=0) # 给放入的菜单submenu命名为Import
    
    # 第9步，创建第三级菜单命令，即菜单项里面的菜单项里面的菜单命令（有点拗口，笑~~~）
    submenu.add_command(label='账单', command=chooes_bills_folder)
    submenu.add_command(label='微信账单', command=do_job)
    submenu.add_command(label='支付宝账单', command=do_job)
    
    # 在File中加入New、Open、Save等小菜单，即我们平时看到的下拉菜单，每一个小菜单对应命令操作。
    filemenu.add_command(label='Open', command=create_grandet_bills_window)
    filemenu.add_command(label='Save', command=do_job)
    
    filemenu.add_separator()    # 添加一条分隔线
    filemenu.add_command(label='Exit', command=window.quit) # 用tkinter里面自带的quit()函数

    return filemenu
    
def add_edit(editmenu: tk.Menu, window: tk.Tk) -> tk.Menu:
    
    # 同样的在 Edit 中加入Cut、Copy、Paste等小命令功能单元，如果点击这些单元, 就会触发do_job的功能
    editmenu.add_command(label='Cut', command=do_job)
    editmenu.add_command(label='Copy', command=do_job)
    editmenu.add_command(label='Paste', command=do_job)
    
    return editmenu

def add_help(helpmenu: tk.Menu, window: tk.Tk) -> tk.Menu:
    
    # 同样的在 Edit 中加入Cut、Copy、Paste等小命令功能单元，如果点击这些单元, 就会触发do_job的功能
    helpmenu.add_command(label='help', command=show_help)
    helpmenu.add_command(label='使用手册', command=show_help)
    
    return helpmenu

def add_about(aboutmenu: tk.Menu, window: tk.Tk) -> tk.Menu:
    
    # 同样的在 Edit 中加入Cut、Copy、Paste等小命令功能单元，如果点击这些单元, 就会触发do_job的功能
    aboutmenu.add_command(label='关于', command=show_help)
    aboutmenu.add_command(label='关于作者', command=show_help)
    aboutmenu.add_command(label='关于葛朗台', command=show_help)
    
    return aboutmenu
    
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
    filemenu = add_file(filemenu=filemenu, window=window)
    # 将上面定义的空菜单命名为File，放在菜单栏中，就是装入那个容器中
    menubar.add_cascade(label='File', menu=filemenu)
    
    # # 第7步，创建一个Edit菜单项（默认不下拉，下拉内容包括Cut，Copy，Paste功能项）
    editmenu = tk.Menu(menubar, tearoff=0)
    editmenu = add_edit(editmenu=editmenu, window=window)
    # # 将上面定义的空菜单命名为 Edit，放在菜单栏中，就是装入那个容器中
    menubar.add_cascade(label='Edit', menu=editmenu)
    
    # # 第7步，创建一个Edit菜单项（默认不下拉，下拉内容包括Cut，Copy，Paste功能项）
    helpmenu = tk.Menu(menubar, tearoff=0)
    helpmenu = add_help(helpmenu=helpmenu, window=window)
    # # 将上面定义的空菜单命名为 Edit，放在菜单栏中，就是装入那个容器中
    menubar.add_cascade(label='Help', menu=helpmenu)
    
    # # 第7步，创建一个Edit菜单项（默认不下拉，下拉内容包括Cut，Copy，Paste功能项）
    aboutmenu = tk.Menu(menubar, tearoff=0)
    aboutmenu = add_about(aboutmenu=aboutmenu, window=window)
    # # 将上面定义的空菜单命名为 Edit，放在菜单栏中，就是装入那个容器中
    menubar.add_cascade(label='About', menu=aboutmenu)
    
    # 第11步，创建菜单栏完成后，配置让菜单栏menubar显示出来
    window.config(menu=menubar)
    
    # 第4步，在图形界面上设定标签
    l = tk.Label(window, text='欢迎您来到年度消费冠军评选系统，谁是今年的消费大魔王呢？', bg='green', font=('Arial', 12), width=50, height=2)
    # 说明： bg为背景，font为字体，width为长，height为高，这里的长和高是字符的长和高，比如height=2,就是标签有2个字符这么高
    l.pack(expand=1)

    # # 第4步，在图形界面上设定输入框控件entry并放置控件
    # bills_file_path = tk.Entry(window, show=None, font=('Arial', 14))  # 显示成明文形式
    # bills_file_path.pack()
    
    # btn = tk.Button(window,text="弹出选择文件对话框",command=chooes_bills_folder)
    # btn.pack()
    
    # analysis_bills_btn = tk.Button(window,text="解析账单文件",command=analysis_bills)
    # analysis_bills_btn.pack()
    
    info = ''
    start_time_text = tk.Entry(window, width=20)
    start_time_text.place(x=100,y=30)
    start_time_text.configure(state="normal")
    start_time_text.delete(0, END)
    start_time_text.insert("0", info)
    start_time_text.configure(state="disabled")
    
    # 第5步，主窗口循环显示
    window.mainloop()