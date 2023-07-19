#/bin/bash python3

import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

from tools.analysis_transactions import AnalysisTransactions


class DetailPage:
    
    def __init__(self) -> None:
        pass


    @classmethod
    def setting_tree_view_for_transaction(cls, transactions: list, left_tree: ttk.Treeview) -> ttk.Treeview:
        
        # 支出
        count_01, money_01, _ = AnalysisTransactions.analyze_transactions_expenditure(transactions=transactions)
        # 收入
        count_02, money_02, _ = AnalysisTransactions.analyze_transactions_income(transactions=transactions)
        # 不记收支
        count_03, money_03, _ = AnalysisTransactions.analyze_transactions_no_income_and_expenditure(transactions=transactions)
        
        count = count_01 + count_02 + count_03
        money = 0 - money_01 + money_02
        
        left_tree["columns"] = ("one", "two")
        left_tree.column("one", width=100)
        left_tree.column("two", width=100)
        left_tree.heading("one", text="交易笔数")
        left_tree.heading("two", text="金额")
        left_tree.insert("", 0, text="收入",    values=(f"{str(count_01)}", f"{str(money_01)}"))
        left_tree.insert("", 1, text="支出",    values=(f"{str(count_02)}", f"{str(money_02)}"))
        left_tree.insert("", 2, text="不记收支", values=(f"{str(count_03)}", f"{str(money_03)}"))
        left_tree.insert("", 3, text="总计",    values=(f"{str(count)}", f"{str(money)}"))
        
        return left_tree


    @classmethod
    def show_detail_page(cls, transactions: list, window_title: str="详情窗口"):
        
        # 创建窗口
        window = tk.Tk()
        window.title(window_title)

        # 创建左右两个面板
        left_panel = tk.Frame(window)
        left_panel.pack(side="left", fill="both", expand=True)
        ttk.Separator(window, orient="vertical").pack(side="left", fill="y")
        right_panel = tk.Frame(window)
        right_panel.pack(side="right", fill="both", expand=True)

        # 调整左侧面板宽度占整个窗口的1/3
        window.update()
        left_panel.config(width=window.winfo_width() // 3)

        # 左侧上方显示文本信息

        left_tree = ttk.Treeview(left_panel)
        left_tree = cls.setting_tree_view_for_transaction(transactions=transactions, left_tree=left_tree)
        # left_tree["columns"] = ("one", "two")
        # left_tree.column("one", width=100)
        # left_tree.column("two", width=100)
        # left_tree.heading("one", text="列标题1")
        # left_tree.heading("two", text="列标题2")
        # left_tree.insert("", 0, text="行1", values=("1A", "1B"))
        # left_tree.insert("", 1, text="行2", values=("2A", "2B"))
        left_tree.pack(fill="both", expand=True)

        # text_label = tk.Label(left_panel, text="这里是文本信息")
        # text_label.pack(fill="both", expand=True)

        # 调整标签高度占整个窗口的1/3
        left_tree.config(height=window.winfo_height() // 3)

        # 左侧下方显示多个复选框
        check_var1 = tk.BooleanVar()
        check_var2 = tk.BooleanVar()
        check_var3 = tk.BooleanVar()
        check_button1 = tk.Checkbutton(left_panel, text="选项1", variable=check_var1)
        check_button2 = tk.Checkbutton(left_panel, text="选项2", variable=check_var2)
        check_button3 = tk.Checkbutton(left_panel, text="选项3", variable=check_var3)
        check_button1.pack()
        check_button2.pack()
        check_button3.pack()

        # 右侧上方实现表格
        tree = ttk.Treeview(right_panel)
        tree["columns"] = ("one", "two")
        tree.column("one", width=100)
        tree.column("two", width=100)
        tree.heading("one", text="列标题1")
        tree.heading("two", text="列标题2")
        tree.insert("", 0, text="行1", values=("1A", "1B"))
        tree.insert("", 1, text="行2", values=("2A", "2B"))
        tree.pack()

        # 右侧添加分界线
        ttk.Separator(right_panel, orient="horizontal").pack(fill="x")

        # 右侧下方插入图片
        # image = Image.open("/Users/pengliu/Code/Grandet/src/tests/iii.png")
        # photo = ImageTk.PhotoImage(image)
        # image_label = tk.Label(right_panel, image=photo)
        # image_label.pack()

        # 运行窗口
        window.mainloop()
