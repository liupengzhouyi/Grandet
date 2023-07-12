#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import tkinter as tk  # 使用Tkinter前需要先导入
from PIL import Image, ImageTk

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from functions.log4py import print_log
from gui.ui.globel_varable import set_value
from gui.ui.globel_varable import get_value

from functions.read_table import ReadTransactionTable
from modules.transaction import YearsTransaction
from modules.transactions_tools import TransactionsTools


def fill_bill_files(bill_frame: tk.Frame, file_names: list) -> tk.Frame:
    
    # 左侧账单文件列表
    # bill_frame = tk.Frame(root)
    # bill_frame = tk.Frame(root, width=20) # 设置列表框架宽度为窗口宽度的1/4
    # bill_frame.pack(side="left", fill="both", expand=True)
    bill_frame.pack(side="left", fill="y", expand=True)

    bill_header = tk.Label(bill_frame, text="📁 账单文件列表")
    bill_header.pack(side="top")
    
    bill_list = tk.Listbox(bill_frame)
    for index, file_name in enumerate(file_names):
        bill_list.insert(index, "📃：" + file_name)
    
    bill_list.pack(side="top", fill="both", expand=True)
    
    log_label = tk.Label(bill_frame, text="📔 日志")
    log_label.pack(side="top")

    log_text = tk.Text(bill_frame, height=10)
    log_text.pack(side="bottom", fill="both", expand=True)
    
    return bill_frame


def fill_bill_information(yearly_summary: tk.Frame, root: tk.Tk, head_words: list, years: list, image_path: str) -> tk.Frame:
    
    # 右侧每年花销简介
    # yearly_summary = tk.Frame(root)
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
    
    all_transfer_header = tk.Label(header, text=head_words[5], width=20)
    all_transfer_header.pack(side="left")

    details_header = tk.Label(header, text=head_words[6], width=10)
    details_header.pack(side="right")

    # 分割线
    separator = tk.Frame(yearly_summary, height=2, bd=1, relief="sunken")
    separator.pack(fill="x", padx=5, pady=5)

    for year, summary, expenditure_count, income_count, transfer_count, all_transfer_count in years:
        year_row = tk.Frame(yearly_summary)
        year_row.pack(side="top", fill="x")

        year_label = tk.Label(year_row, text=year, width=10)
        year_label.pack(side="left")

        summary_label = tk.Label(year_row, text=str(f"{summary:.2f}"), width=10)
        summary_label.pack(side="left")

        expenditure_label = tk.Label(year_row, text=str(expenditure_count), width=15)
        expenditure_label.pack(side="left")

        income_label = tk.Label(year_row, text=str(income_count), width=15)
        income_label.pack(side="left")

        transfer_label = tk.Label(year_row, text=str(transfer_count), width=20)
        transfer_label.pack(side="left")
        
        transfer_label = tk.Label(year_row, text=str(all_transfer_count), width=20)
        transfer_label.pack(side="left")

        details_button = tk.Button(year_row, text="详情", command=lambda y=year, r=root: show_details(r, y), width=10)
        details_button.pack(side="right")
    
    separator_for_image = tk.Frame(yearly_summary, height=2, bd=1, relief="sunken")
    separator_for_image.pack(fill="x", padx=5, pady=5)
    
    canvas = tk.Canvas(yearly_summary, width=200, height=200)
    
    print(f"Read image: {image_path}.")
    # 打开图像并转换为PhotoImage对象
    img = Image.open(image_path)
    img_resized = img.resize((200,200), Image.ANTIALIAS) # 调整图片大小

    photo = ImageTk.PhotoImage(img_resized, master=canvas)

    # 在画布上插入图像
    canvas.create_image(100, 100, anchor=tk.CENTER, image=photo)
    canvas.pack()
    # root.mainloop()

    return yearly_summary
    
    
def show_details(root: tk.Tk, year: str):
    
    details_window = tk.Toplevel(root)
    details_window.title(f"{year} 账单详情")
    details_label = tk.Label(details_window, text=f"这里是 {year} 年的账单详情")
    details_label.pack()


def get_data() -> tuple:
        
    files = []
    years = []
    print_log(f"get every_years_transactions")
    every_years_transactions = get_value("every_years_transactions")
    if every_years_transactions is None:
        print_log(f"get every_years_transactions error.")
        # 账单文件
        files = ["账单1", "账单2", "账单3"]
        years = [("2020", 1000, 10, 5, 3, 18),
                 ("2021", 2000, 15, 8, 4, 27),
                 ("2022", 3000, 20, 10, 5, 35)]
    else:
        print_log(f"get every_years_transactions success.")
        all_files = get_value("bills_files")
        files = []
        for item in all_files:
            files.append(os.path.basename(item))
        years = []
        for key_word in every_years_transactions.keys():
            
            year_transaction = every_years_transactions.get(key_word)
            if isinstance(year_transaction, YearsTransaction):
                year = year_transaction.year
                all_number = TransactionsTools.get_transactions_size(year_transaction)
                summary = round(sum(TransactionsTools.get_amounts(year_transaction)), 3)
                expenditure_count = TransactionsTools.get_summary_count(year_transaction)
                income_count = TransactionsTools.get_income_count(year_transaction)
                transfer_count = TransactionsTools.get_transfer_count(year_transaction)
                
                years.append((year, summary, expenditure_count, income_count, transfer_count, all_number))
            else:
                continue

    image_path = "/Users/pengliu/Code/Grandet/src/gui/ui/images.png" 
    return (files, years, image_path)


def create_grandet_bills_window():
    
    # 标题
    title = "葛朗台的账单"
    # 表头
    head_words = ["年份", "花销总额", "支出交易笔数", "收入交易笔数", "个人转账交易笔数", "交易总笔数", "详情"]
    files, years, image_path = get_data()

    root = tk.Tk()
    root.geometry("1600x720") # 设置窗口大小
    root.title(title)
    bill_frame = tk.Frame(root, width=150) # 设置列表框架宽度为窗口宽度的1/4
    yearly_summary = tk.Frame(root, width=600)
    
    bill_frame = fill_bill_files(bill_frame=bill_frame, file_names=files)
    
    yearly_summary = fill_bill_information(yearly_summary=yearly_summary,
                                           root=root,
                                           head_words=head_words,
                                           years=years,
                                           image_path=image_path)

    years_lable = []
    expenditure_counts = []
    income_counts = []
    transfer_counts = []
    all_transfer_counts = []
    
    for year, summary, expenditure_count, income_count, transfer_count, all_transfer_count in years:
        
        years_lable.append(year)
        expenditure_counts.append(expenditure_count)
        income_counts.append(income_count)
        transfer_counts.append(transfer_count)
        all_transfer_counts.append(all_transfer_count)
        
    print(expenditure_counts)
    print(income_counts)
    print(transfer_counts)
    print(all_transfer_counts)

    # 创建matplotlib图像并在Tkinter窗口中嵌入它
    fig = Figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot(111)
    # 数据
    N = len(years_lable)
    ind = np.arange(N) # x 轴的位置
    width = 0.15 # 柱子的宽度
    rects1 = ax.bar(ind, tuple(expenditure_counts), width, label='expend')
    rects2 = ax.bar(ind + width, tuple(income_counts), width, label='income')
    rects3 = ax.bar(ind + width * 2, tuple(transfer_counts), width, label='self')
    rects3 = ax.bar(ind + width * 3, tuple(all_transfer_counts), width, label='all')
    
    # 添加文本标签和标题
    # ax.set_ylabel('Scores')
    # ax.set_title('Scores by group and gender')
    ax.set_xticks(ind)
    ax.set_xticklabels(tuple(years_lable))
    ax.legend()

    canvas = FigureCanvasTkAgg(fig, master=yearly_summary)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    root.mainloop()
