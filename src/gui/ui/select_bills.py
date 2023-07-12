#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter as tk  # 使用Tkinter前需要先导入
import tkinter.filedialog

from functions.log4py import print_log
from gui.ui.globel_varable import set_value
from gui.ui.globel_varable import get_value

from functions.read_table import ReadTransactionTable


def select_folder_path(bills_folder_bable: tk.Label):

    folder_name = tkinter.filedialog.askdirectory()
    print_log(f"Select bills folder: {folder_name}")
    if folder_name != '':
        bills_folder_bable.config(text = "您选择的文件是：" + folder_name)
        set_value("bills_folder", folder_name)
    else:
        bills_folder_bable.config(text = "您没有选择任何文件夹")
    return folder_name


def select_bills_file_path(bills_file_list: tk.Listbox):
    
    folder_path = get_value("bills_folder")
    print_log(f"Select bills file in folder {folder_path}.")
    
    csv_files = ReadTransactionTable.extract_csv_file_path(folder_path)
    target_csv_files = ReadTransactionTable.flitter_csv_file(csv_files)
    
    set_value("bills_files", target_csv_files)
    
    count = bills_file_list.size() + 1
    for index, item in enumerate(target_csv_files):
        now_index = index + count 
        bills_file_list.insert(now_index, f"{str(now_index)}. {item}")
        print(f"{str(now_index)}. {item}")
    return
    

def clear_bills_file_path(bills_file_list: tk.Listbox):
    
    print_log(f"Clear bills file list.")
    
    bills_file_list.delete(0, tk.END)
    return
    
    
def chooes_bills_folder():
    
    folder_path = ''
    # 第1步，实例化object，建立窗口window
    select_folder_window = tk.Tk()
    # 第2步，给窗口的可视化起名字
    select_folder_window.title('导入账单')
    # 第3步，设定窗口的大小(长 * 宽)
    select_folder_window.geometry('800x500')  # 这里的乘是小x
    
    bills_folder_bable = tk.Label(select_folder_window, text = '')
    bills_folder_bable.pack()
    
    btn = tk.Button(
        select_folder_window, text="导入账单", command=lambda : select_folder_path(bills_folder_bable=bills_folder_bable))
    btn.pack()
    
    print_log(f"--- Print folder path: {folder_path}")
    
    # 提取账单文件
    bills_file_list = tk.Listbox(select_folder_window, width=60, height=20)
    bills_file_list.pack()
    select_bills_file_btn = tk.Button(
        select_folder_window, text="提取账单文件", command=lambda : select_bills_file_path(bills_file_list=bills_file_list))
    select_bills_file_btn.pack()
    clear_bills_file_btn = tk.Button(
        select_folder_window, text="重置账单文件", command=lambda : clear_bills_file_path(bills_file_list=bills_file_list)) 
    clear_bills_file_btn.pack()
    
    quit_btn = tk.Button(select_folder_window, text="退出选择账单", command=select_folder_window.quit)
    quit_btn.pack()
    
    select_folder_window.mainloop()