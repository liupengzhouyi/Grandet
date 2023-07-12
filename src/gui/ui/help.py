#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 使用Tkinter前需要先导入

import tkinter as tk  
import tkinter.filedialog
from tkinter import ttk


    
def show_help():

    # 第1步，实例化object，建立窗口window
    window = tk.Tk()
    
    # 第2步，给窗口的可视化起名字
    window.title('Help')
    
    # 第3步，设定窗口的大小(长 * 宽)
    window.geometry('500x300')  # 这里的乘是小x
    
    # 第4步，在图形界面上设定标签
    l = tk.Label(window, text='欢迎您来到年度消费冠军评选系统的帮助页面', bg='green', font=('Arial', 12), width=50, height=2)
    # 说明： bg为背景，font为字体，width为长，height为高，这里的长和高是字符的长和高，比如height=2,就是标签有2个字符这么高
    l.pack(expand=1)
    
    # 第5步，主窗口循环显示
    window.mainloop()