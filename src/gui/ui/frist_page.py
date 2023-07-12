#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter as tk  # 使用Tkinter前需要先导入

from functions.log4py import print_log
from gui.ui.globel_varable import set_value
from gui.ui.globel_varable import get_value

from functions.read_table import ReadTransactionTable


def fill_bill_files(root: tk.Tk, file_names: list) -> tk.Tk:
    
    # 左侧账单文件列表
    bill_frame = tk.Frame(root)
    bill_frame.pack(side="left", fill="both", expand=True)

    bill_header = tk.Label(bill_frame, text="账单文件列表")
    bill_header.pack(side="top")

    bill_list = tk.Listbox(bill_frame)
    # file_names.reverse()
    for index, file_name in enumerate(reversed(file_names)):
        bill_list.insert(0, file_name)
    bill_list.pack(side="bottom", fill="both", expand=True)
    return root
    
def show_details(root: tk.Tk, year: str):
    
        details_window = tk.Toplevel(root)
        details_window.title(f"{year} 账单详情")
        details_label = tk.Label(details_window, text=f"这里是 {year} 年的账单详情")
        details_label.pack()
        

def create_grandet_bills_window():
    
    
    # 标题
    title = "葛朗台的账单"
    # 账单文件
    files = ["账单1", "账单2", "账单3"]
    # 表头
    head_words = ["年份", "花销总额", "支出交易笔数", "收入交易笔数", "个人转账交易笔数", "详情"]

    years = [("2020", 1000, 10, 5, 3),
            ("2021", 2000, 15, 8, 4),
            ("2022", 3000, 20, 10, 5)]

    root = tk.Tk()
    
    root.title(title)
    root = fill_bill_files(root=root, file_names=files)


    # 右侧每年花销简介
    yearly_summary = tk.Frame(root)
    yearly_summary.pack(side="right", fill="both", expand=True)

    header = tk.Frame(yearly_summary)
    header.pack(side="top", fill="x")

    year_header = tk.Label(header, text=head_words[0], width=10)
    year_header.pack(side="left")

    summary_header = tk.Label(header, text=head_words[1], width=10)
    summary_header.pack(side="left")

    expenditure_header = tk.Label(header, text=head_words[2], width=15)
    expenditure_header.pack(side="left")

    income_header = tk.Label(header, text=head_words[3], width=15)
    income_header.pack(side="left")

    transfer_header = tk.Label(header, text=head_words[4], width=20)
    transfer_header.pack(side="left")

    details_header = tk.Label(header, text=head_words[5], width=10)
    details_header.pack(side="right")

    # 分割线
    separator = tk.Frame(yearly_summary, height=2, bd=1, relief="sunken")
    separator.pack(fill="x", padx=5, pady=5)

    for year, summary, expenditure_count, income_count, transfer_count in years:
        year_row = tk.Frame(yearly_summary)
        year_row.pack(side="top", fill="x")

        year_label = tk.Label(year_row, text=year, width=10)
        year_label.pack(side="left")

        summary_label = tk.Label(year_row, text=str(summary), width=10)
        summary_label.pack(side="left")

        expenditure_label = tk.Label(year_row, text=str(expenditure_count), width=15)
        expenditure_label.pack(side="left")

        income_label = tk.Label(year_row, text=str(income_count), width=15)
        income_label.pack(side="left")

        transfer_label = tk.Label(year_row, text=str(transfer_count), width=20)
        transfer_label.pack(side="left")

        details_button = tk.Button(year_row, text="详情", command=lambda y=year, r=root: show_details(r, y), width=10)
        details_button.pack(side="right")

    root.mainloop()


# create_grandet_bills_window()