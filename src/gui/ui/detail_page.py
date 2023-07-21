#/bin/bash python3

import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

from matplotlib.figure import Figure
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from tools.analysis_transactions import AnalysisTransactions
from gui.ui.show_transactions_as_table import ShowTransaction

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
        left_tree.insert("", 0, text="收入",    values=(f"{str(count_01)}", f"{money_01:.2f}"))
        left_tree.insert("", 1, text="支出",    values=(f"{str(count_02)}", f"{money_02:.2f}"))
        left_tree.insert("", 2, text="不记收支", values=(f"{str(count_03)}", f"{money_03:.2f}"))
        left_tree.insert("", 3, text="总计",    values=(f"{str(count)}",    f"{money:.2f}"))
        
        return left_tree


    @classmethod
    def full_button(cls, window: tk.Frame) -> tk.Frame:
        
        check_button_text = ['餐饮美食', '投资理财', '生活服务', '日用百货', '交通出行', '信用借还', '酒店旅游', '收入', '账户存取',
                            '退款', '商业服务', '文化休闲', '充值缴费', '爱车养车', '转账红包', '教育培训', '美容美发', '服饰装扮',
                            '医疗健康', '数码电器', '其他', '家居家装', '母婴亲子', '运动户外', '保险', '交易类型', '商户消费',
                            '转账', '微信红包（单发）', '扫二维码付款', '转账-退款', '微信红包', '零钱提现', '零钱充值', '群收款',
                            '退款', '微信红包（群红包）', '二维码收款', ]
        
        number_of_line = 3
        n = 0
        j = 0
        for item in check_button_text:
            tk.Checkbutton(window, text=item).grid(row=n, column=j)
            j += 1
            if j == number_of_line:
                j = 0
                n += 1
                
        # 画一个分界线
        # n = int(len(check_button_text) / number_of_line)
        n = n + 1
        ttk.Separator(window, orient="horizontal").grid(row=n, column=0, columnspan=4, sticky="ew")
        n = n + 2
        
        radio_text = ["柱状图", "折线图", "频率图", "饼图"]
        # 下边是三个Radiobutton
        radio_var = tk.StringVar()
        for i, item in enumerate(radio_text):
            tk.Radiobutton(window, text=item, variable=radio_var, value=f"选择{i + 1}").grid(row=n, column=i)
        n = n + 1
        
        # 画一个分界线
        ttk.Separator(window, orient="horizontal").grid(row=n, column=0, columnspan=4, sticky="ew")
        n = n + 1

        # 下面是俩个并排的按钮，分别是“恢复默认”，“确认”
        tk.Button(window, text="恢复默认").grid(row=n, column=1)
        tk.Button(window, text="确认").grid(row=n, column=2)
        
        return window


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
        left_tree.pack(fill="both", expand=True)
        # 调整标签高度占整个窗口的1/3
        left_tree.config(height=window.winfo_height() // 3)

        # 坐侧添加分界线
        ttk.Separator(left_tree, orient="horizontal").pack(fill="x")
        
        left_panel_item = tk.Frame(left_panel)
        left_panel_item = cls.full_button(left_panel_item)
        left_panel_item.pack()
        # # 左侧下方显示多个复选框
        # check_var1 = tk.BooleanVar()
        # check_var2 = tk.BooleanVar()
        # check_var3 = tk.BooleanVar()
        # check_button1 = tk.Checkbutton(left_panel, text="选项1", variable=check_var1)
        # check_button2 = tk.Checkbutton(left_panel, text="选项2", variable=check_var2)
        # check_button3 = tk.Checkbutton(left_panel, text="选项3", variable=check_var3)
        # check_button1.pack()
        # check_button2.pack()
        # check_button3.pack()

        # 右侧上方实现表格
        tree = ttk.Treeview(right_panel)
        yscrollbar = ttk.Scrollbar(right_panel)
        yscrollbar.pack(side=tk.RIGHT,fill=tk.Y)
        yscrollbar.config(command=tree.yview)
        tree.configure(yscrollcommand=yscrollbar.set)
        tree = ShowTransaction.genaertion_table(tree=tree, transactions=transactions)
        tree.pack()

        # 右侧添加分界线
        ttk.Separator(right_panel, orient="horizontal").pack(fill="x")


        years_lable = [1, 2, 3]
        expenditure_counts = [1, 3, 5]
        income_counts = [2, 4, 6]
        
        fig = Figure(figsize=(5, 4), dpi=100)
        ax = fig.add_subplot(111)
        # 数据
        N = len(years_lable)
        ind = np.arange(N) # x 轴的位置
        width = 0.15 # 柱子的宽度
        ax.set_xticks(ind)
        ax.set_xticklabels(tuple(years_lable))
        ax.legend()
    
        rects1 = ax.bar(ind, tuple(expenditure_counts), width, label='expend')
        rects2 = ax.bar(ind + width, tuple(income_counts), width, label='income')
    
        canvas = FigureCanvasTkAgg(fig, master=right_panel)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    
        # 右侧下方插入图片
        # image = Image.open("/Users/pengliu/Code/Grandet/src/tests/iii.png")
        # photo = ImageTk.PhotoImage(image)
        # image_label = tk.Label(right_panel, image=photo)
        # image_label.pack()

        # 运行窗口
        window.mainloop()
