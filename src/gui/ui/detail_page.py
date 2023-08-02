#/bin/bash python3

import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

from functions.log4py import print_log
from modules.transaction import Transaction
from modules.transactions_tools import TransactionsTools

from matplotlib.figure import Figure
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from tools.analysis_transactions import AnalysisTransactions
from gui.ui.show_transactions_as_table import ShowTransaction


class DetailPage:
    
    def __init__(self) -> None:
        pass
    
    
    @classmethod
    def get_frequency_data(cls, transactions: list):
        
        colors = ["#B0C4DE", "#FF00FF", "#1E90FF", "#FA8072", "#EEE8AA", "#FF1493", "#7B68EE",
                  "#FFC0CB", "#696969", "#556B2F", "#CD853F", "#000080", "#32CD32", "#7F007F",
                  "#B03060", "#800000", "#483D8B", "#008000", "#3CB371", "#008B8B", "#FF0000",
                  "#FF8C00", "#FFD700", "#00FF00", "#9400D3", "#00FA9A", "#DC143C", "#00FFFF",
                  "#00BFFF", "#0000FF", "#ADFF2F", "#DA70D6", '#e6194B', '#3cb44b', '#ffe119',
                  '#4363d8', '#f58231', '#911eb4', '#42d4f4', '#f032e6', '#bfef45', '#fabed4',
                  '#469990', '#dcbeff', '#9A6324', '#fffac8', '#800000', '#aaffc3', '#808000',
                  '#ffd8b1', '#000075', '#a9a9a9', '#ffffff', '#000000', '#FF0000', '#FFA500',
                  '#FFFF00', '#00FF00', '#228B22']
        
        color_index = 0
        type_indexs = []
        
        date_info = []
        time_info = []
        value_info = []
        color_info = []
        for transaction in transactions:
            if isinstance(transaction, Transaction):
                
                date_info.append(str(transaction.time_.day))
                time_info.append(transaction.time_.get_time_info_as_number())
                value_info.append(float(transaction.amount))
                if transaction.type_ not in type_indexs:
                    type_indexs.append(transaction.type_)
                    color_info.append(colors[color_index])
                    color_index += 1
                else:
                    temp_index = type_indexs.index(transaction.type_)
                    color_info.append(colors[temp_index])
                
        print_log(f"data size: {str(len(date_info))}")
        print_log(f"time size: {str(len(time_info))}")
        print_log(f"value size: {str(len(value_info))}")
        date_info.reverse()
        time_info.reverse()
        value_info.reverse()
        color_info.reverse()
        return date_info, time_info, value_info, color_info


    @classmethod
    def genartion_frequency_image(cls, transactions: list, take_size_effect: bool=True) -> Figure:
        
        date_info, time_info, value_info, color_info = cls.get_frequency_data(transactions=transactions)
        fig = Figure(figsize=(5, 4), dpi=100)
        ax = fig.add_subplot(111)


        # 数据
        if len(date_info) != len(value_info) or len(time_info) != len(value_info):
            ax.scatter(date_info, time_info)
        else:
            new_value_info = np.array(value_info)
            if take_size_effect:
                ax.scatter(date_info, time_info, s=new_value_info, c=color_info)
            else:
                ax.scatter(date_info, time_info, c=color_info)
        return fig
    
    
    @classmethod
    def get_pie_data(cls, transactions: list) -> dict:
        
        datas = {}
        for transaction in transactions:
            if isinstance(transaction, Transaction):
                if transaction.income_expense not in ["支出"]:
                    continue
                temp_type = transaction.type_
                if temp_type not in datas.keys():
                    datas[temp_type] = []
                    datas[temp_type].append(transaction)
                else:
                    datas[temp_type].append(transaction)
        return datas
    
    
    @classmethod
    def genartion_pie_image(cls, transactions: list) -> Figure:
        
        date_infos = cls.get_pie_data(transactions=transactions)
        fig = Figure(figsize=(5, 4), dpi=100)
        ax = fig.add_subplot(111)
        sizes = []
        labels = []
        for label in date_infos.keys():
            all_count = 0.0
            for transaction in date_infos[label]:
                all_count += float(transaction.amount)
            sizes.append(all_count)
            labels.append(label)

        ax.pie(sizes, labels=labels)
        return fig

            

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
    def full_button(cls, window: tk.Frame, transactions: list) -> tk.Frame:
        
        check_button_text = ['餐饮美食', '投资理财', '生活服务', '日用百货', '交通出行', '信用借还', '酒店旅游', '收入', '账户存取',
                            '退款', '商业服务', '文化休闲', '充值缴费', '爱车养车', '转账红包', '教育培训', '美容美发', '服饰装扮',
                            '医疗健康', '数码电器', '其他', '家居家装', '母婴亲子', '运动户外', '保险', '交易类型', '商户消费',
                            '转账', '微信红包（单发）', '扫二维码付款', '转账-退款', '微信红包', '零钱提现', '零钱充值', '群收款',
                            '退款', '微信红包（群红包）', '二维码收款', ]
        target_type_codes = []
        
        check_buttons = []
        number_of_line = 3
        n = 0
        j = 0
        checkboxes = {}
        for index, item in enumerate(check_button_text):
            checkboxes[index] = tk.BooleanVar(window)
            temp_check_button = tk.Checkbutton(window, text=item, variable=checkboxes[index])
            temp_check_button.grid(row=n, column=j)
            check_buttons.append(temp_check_button)
            j += 1
            if j == number_of_line:
                j = 0
                n += 1
            
        # 画一个分界线
        n = n + 1
        ttk.Separator(window, orient="horizontal").grid(row=n, column=0, columnspan=4, sticky="ew")
        n = n + 2
        
        radio_text = ["柱状图", "散点图", "频率图", "饼图", "折线图"]
        # 下边是三个Radiobutton
        radio_var = tk.StringVar(window)
        for i, item in enumerate(radio_text):
            tk.Radiobutton(window, text=item, variable=radio_var, value=f"{i + 1}").grid(row=n, column=i)
        n = n + 1
        
        # 画一个分界线
        ttk.Separator(window, orient="horizontal").grid(row=n, column=0, columnspan=4, sticky="ew")
        n = n + 1

        def button_Click(event=None):
            
            print(len(checkboxes.keys()))
            filter_words = []
            for i in checkboxes.keys():           # 检查此字典的关键字,同: for i in checkboxes:
                if checkboxes[i].get() == True:   # 若被选中则执行
                    print(f"{str(i)}: [{str(checkboxes[i].get())}:{str(check_button_text[i])}]", end=", ")
                    filter_words.append(check_button_text[i])
            print()
            print(radio_var.get())
            print(filter_words)
            new_transactions = TransactionsTools.filter_transactions_simple(transactions=transactions,
                                                                            type_word=filter_words)
            sub_title_name = "窗口:"
            for item in filter_words:
                sub_title_name += f"{item}-"
            print_log(sub_title_name)
            if len(filter_words) > 0:
                image_index = -1
                if str(radio_var.get()).isdigit():
                    image_index = int(radio_var.get())
                cls.show_detail_page(transactions=new_transactions,
                                     window_title=sub_title_name,
                                     image_index=image_index)
            
            
        
        def clear():
            for item in check_buttons:
                item.deselect()
            print_log(f"reset check boxes.")

        # 下面是俩个并排的按钮，分别是“恢复默认”，“确认”
        tk.Button(window, text="恢复默认", command=clear).grid(row=n, column=1)
        tk.Button(window, text="确认", command=button_Click).grid(row=n, column=2)
        
        return window
    
    @classmethod
    def show_detail_page(cls, transactions: list, window_title: str="详情窗口", image_index: int="-1"):
        
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
        left_panel_item = cls.full_button(window=left_panel_item, transactions=transactions)
        left_panel_item.pack()
    
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

        # fig = cls.genartion_pie_image(transactions=transactions)
        fig = cls.genartion_frequency_image(transactions=transactions)
        if image_index == 2:
            fig = cls.genartion_frequency_image(transactions=transactions, take_size_effect=False)
        if image_index == 3:
            fig = cls.genartion_frequency_image(transactions=transactions, take_size_effect=True)
        if image_index == 4:
            fig = cls.genartion_pie_image(transactions=transactions)
        
        canvas = FigureCanvasTkAgg(fig, master=right_panel)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        # 运行窗口
        window.mainloop()
