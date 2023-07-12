#/bin/bash python3
# coding: utf-8

#日期时间选择器


import tkinter as tk
from tkcalendar import Calendar

from tkinter import ttk
from tkinter import *
import datetime
 

def start_calendar(callback_for_save_datatime: function):
    
    def print_sel():
        start_time_text.configure(state="normal")
        print(str(cal.selection_get()) + " " + str(hour.get()) + ":" + str(minute.get()))
        s_data = str(cal.selection_get()) + " " + str(hour.get()) + ":" + str(minute.get())
        start_time_text.delete(0, END)
        start_time_text.insert("0", s_data)
        start_time_text.configure(state="disabled")
        cal.see(datetime.date(year=2016, month=2, day=5))
 
    top = tk.Toplevel()
    top.geometry("300x250")
 
    today = datetime.date.today()
 
    mindate = datetime.date(year=2022, month=1, day=1)
    maxdate = today + datetime.timedelta(days=5)
 
    cal = Calendar(top, font="Arial 14", selectmode='day', locale='zh_CN', mindate=mindate, maxdate=maxdate,
                   background="red", foreground="blue", bordercolor="red", selectbackground="red",
                   selectforeground="red", disabledselectbackground=False)
    cal.place(x=0, y=0, width=300, height=200)
    value = 0
    values_h = ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
                20, 21, 22, 23]
    values_m = ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
                20, 21, 22, 23, 24, 25, 26, 27, 28,
                29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53,
                54,
                55, 56, 57, 58, 59]
 
    hour = ttk.Combobox(
        master=top,  # 父容器
        height=15,  # 高度,下拉显示的条目数量
        width=3,  # 宽度
        state="normal",  # 设置状态 normal(可选可输入)、readonly(只可选)、 disabled
        cursor="arrow",  # 鼠标移动时样式 arrow, circle, cross, plus...
        font=("", 20),  # 字体
        values=values_h,  # 设置下拉框的选项
    )
    hour.place(x=0, y=200)
    ttk.Label(top, text="时").place(x=60, y=195, width=20, height=40)
 
    minute = ttk.Combobox(
        master=top,  # 父容器
        height=15,  # 高度,下拉显示的条目数量
        width=3,  # 宽度
        state="normal",  # 设置状态 normal(可选可输入)、readonly(只可选)、 disabled
        cursor="arrow",  # 鼠标移动时样式 arrow, circle, cross, plus...
        font=("", 20),  # 字体
        values=values_m,  # 设置下拉框的选项
    )
    minute.place(x=80, y=200)
    ttk.Label(top, text="分").place(x=140, y=195, width=20, height=40)
 
    tk.Button(top, text="确定", command=print_sel).place(x=240, y=205)

    
root =Tk()
start_time = tk.Button(root, text="开始时间", command=start_calendar)
start_time.place(x=10,y=10)
start_time = tk.Button(root, text="结束时间", command=start_calendar)
start_time.place(x=10,y=50)

start_time_text = tk.Entry(root, width=20)
start_time_text.place(x=100,y=10)
end_time_text = tk.Entry(root, width=20)
end_time_text.place(x=100,y=50)
root.geometry("400x200")
root.mainloop()
