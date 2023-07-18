#/bin/bash python3

import tkinter as tk
from tkinter import ttk

from modules.transaction import Transaction


class ShowTransaction:
    
    
    def __init__(self):
        
        pass

    
    @classmethod
    def show_transactions(cls, transactions: list):
        
        # 创建窗口
        window = tk.Tk()
        window.title("表格数据")
        heading_text = ["交易时间", "交易分类", "交易对方", "对方账号", "商品说明", "收/支", "金额", "收/付款方式", "交易状态", "交易订单号", "商家订单号", "备注", "来源"]
        # 创建表格
        tree = ttk.Treeview(window)
        tree["columns"] = heading_text

        for index, item in enumerate(heading_text):
            tree.column(item, width=100)
            tree.heading(item, text=item)
        # 插入数据
        for index, item in enumerate(transactions):
            if isinstance(item, Transaction):
                tree.insert("", 0, text=f"{str(index)}", values=item.to_list())

        tree.pack()

        # 运行窗口
        window.mainloop()



