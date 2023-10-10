#/bin/bash python3
#coding: utf-8

from tabulate import tabulate

from functions.log4py import print_log
from modules.transaction import Transaction
from modules.transaction import DaysTransaction
from modules.transaction import MonthsTransaction
from modules.transaction import YearsTransaction
from gui.ui.show_transactions_as_table import show_transactions

from modules.transaction_filter import FilterRules
from tools.extraction_rules import ExtrcationRules

class TransactionsTools:
    """
    用于处理交易数据的工具类，提供了一系列方法用于分析、过滤和展示交易数据。
    """
    
    def __init__(self) -> None:
        """
        初始化一个 TransactionsTools 对象。
        """
        
        pass
        
    @classmethod
    def get_transactions_size(cls, target_transaction: YearsTransaction) -> int:
        """
        获取年度交易数据中的交易数量。

        Args:
            target_transaction (YearsTransaction): 年度交易数据对象。

        Returns:
            int: 年度交易数据中的交易数量。
        """
        
        return len(target_transaction.transactions)
    
    
    @classmethod
    def get_transactions_size(cls, target_transaction: MonthsTransaction) -> int:
        """
        获取月度交易数据中的交易数量。

        Args:
            target_transaction (MonthsTransaction): 月度交易数据对象。

        Returns:
            int: 月度交易数据中的交易数量。
        """
        
        return len(target_transaction.transactions)
    
    
    @classmethod
    def get_transactions_size(cls, target_transaction: DaysTransaction) -> int:
        """
        获取日度交易数据中的交易数量。

        Args:
            target_transaction (DaysTransaction): 日度交易数据对象。

        Returns:
            int: 日度交易数据中的交易数量。
        """
        
        return len(target_transaction.transactions)
    
    
    @classmethod
    def get_summary_count(cls, target_transaction: YearsTransaction) -> int:
        """
        获取年度交易数据中支出类型的交易数量。

        Args:
            target_transaction (YearsTransaction): 年度交易数据对象。

        Returns:
            int: 年度交易数据中支出类型的交易数量。
        """
        
        count = 0
        for transaction in target_transaction.transactions:
            if isinstance(transaction, Transaction):
                if transaction.income_expense == "支出":
                    count += 1
        return count

    
    @classmethod
    def get_income_count(cls, target_transaction: YearsTransaction) -> int:
        """
        获取年度交易数据中收入类型的交易数量。

        Args:
            target_transaction (YearsTransaction): 年度交易数据对象。

        Returns:
            int: 年度交易数据中收入类型的交易数量。
        """
        
        count = 0
        for transaction in target_transaction.transactions:
            if isinstance(transaction, Transaction):
                if transaction.income_expense == "收入":
                    count += 1
        return count
    
    
    @classmethod
    def get_transfer_count(cls, target_transaction: YearsTransaction) -> int:
        """
        获取年度交易数据中转账类型的交易数量。

        Args:
            target_transaction (YearsTransaction): 年度交易数据对象。

        Returns:
            int: 年度交易数据中转账类型的交易数量。
        """
        
        count = 0
        for transaction in target_transaction.transactions:
            if isinstance(transaction, Transaction):
                if transaction.income_expense == "/" or transaction.income_expense == '不计收支':
                    count += 1
        return count
    
    
    @classmethod
    def get_amounts(cls, target_transaction: YearsTransaction) -> list:
        """
        获取年度交易数据中支出类型交易的金额列表。

        Args:
            target_transaction (YearsTransaction): 年度交易数据对象。

        Returns:
            list: 年度交易数据中支出类型交易的金额列表。
        """
        
        amounts = []
        for transaction in target_transaction.transactions:
            if isinstance(transaction, Transaction):
                if transaction.income_expense == "支出":
                    amounts.append(float(transaction.amount))
        return amounts
    
    
    @classmethod
    def get_transactions_size(cls, target_transaction: MonthsTransaction) -> int:
        """
        获取月度交易数据中的交易数量。

        Args:
            target_transaction (MonthsTransaction): 月度交易数据对象。

        Returns:
            int: 月度交易数据中的交易数量。
        """
        
        return len(target_transaction.transactions)
    
    
    @classmethod
    def get_transactions_size(cls, target_transaction: MonthsTransaction) -> int:
        """
        获取月度交易数据中的交易数量。

        Args:
            target_transaction (MonthsTransaction): 月度交易数据对象。

        Returns:
            int: 月度交易数据中的交易数量。
        """
        
        return len(target_transaction.transactions)
    
    
    @classmethod
    def get_transactions_size(cls, target_transaction: DaysTransaction) -> int:
        """
        获取日度交易数据中的交易数量。

        Args:
            target_transaction (DaysTransaction): 日度交易数据对象。

        Returns:
            int: 日度交易数据中的交易数量。
        """
        
        return len(target_transaction.transactions)
    
    
    @classmethod
    def get_summary_count(cls, target_transaction: MonthsTransaction) -> int:
        """
        获取月度交易数据中支出类型的交易数量。

        Args:
            target_transaction (MonthsTransaction): 月度交易数据对象。

        Returns:
            int: 月度交易数据中支出类型的交易数量。
        """
        
        count = 0
        for transaction in target_transaction.transactions:
            if isinstance(transaction, Transaction):
                if transaction.income_expense == "支出":
                    count += 1
        return count

    
    @classmethod
    def get_income_count(cls, target_transaction: MonthsTransaction) -> int:
        """
        获取月度交易数据中收入类型的交易数量。

        Args:
            target_transaction (MonthsTransaction): 月度交易数据对象。

        Returns:
            int: 月度交易数据中收入类型的交易数量。
        """
        
        count = 0
        for transaction in target_transaction.transactions:
            if isinstance(transaction, Transaction):
                if transaction.income_expense == "收入":
                    count += 1
        return count
    
    
    @classmethod
    def get_transfer_count(cls, target_transaction: MonthsTransaction) -> int:
        """
        获取月度交易数据中转账类型的交易数量。

        Args:
            target_transaction (MonthsTransaction): 月度交易数据对象。

        Returns:
            int: 月度交易数据中转账类型的交易数量。
        """
        
        count = 0
        for transaction in target_transaction.transactions:
            if isinstance(transaction, Transaction):
                if transaction.income_expense == "/" or transaction.income_expense == '不计收支':
                    count += 1
        return count
    
    
    @classmethod
    def get_amounts(cls, target_transaction: MonthsTransaction) -> list:
        """
        获取月度交易数据中支出类型交易的金额列表。

        Args:
            target_transaction (MonthsTransaction): 月度交易数据对象。

        Returns:
            list: 月度交易数据中支出类型交易的金额列表。
        """
        
        amounts = []
        for transaction in target_transaction.transactions:
            if isinstance(transaction, Transaction):
                if transaction.income_expense == "支出":
                    amounts.append(float(transaction.amount))
        return amounts
    
    
    @classmethod
    def get_transactions_size(cls, target_transaction: DaysTransaction) -> int:
        """
        获取日度交易数据中的交易数量。

        Args:
            target_transaction (DaysTransaction): 日度交易数据对象。

        Returns:
            int: 日度交易数据中的交易数量。
        """
        
        return len(target_transaction.transactions)
    
    
    @classmethod
    def get_transactions_size(cls, target_transaction: DaysTransaction) -> int:
        """
        获取日度交易数据中的交易数量。

        Args:
            target_transaction (DaysTransaction): 日度交易数据对象。

        Returns:
            int: 日度交易数据中的交易数量。
        """
        
        return len(target_transaction.transactions)
    
    
    @classmethod
    def get_transactions_size(cls, target_transaction: DaysTransaction) -> int:
        """
        获取日度交易数据中的交易数量。

        Args:
            target_transaction (DaysTransaction): 日度交易数据对象。

        Returns:
            int: 日度交易数据中的交易数量。
        """
        
        return len(target_transaction.transactions)
    
    
    @classmethod
    def get_summary_count(cls, target_transaction: DaysTransaction) -> int:
        """
        获取日度交易数据中支出类型的交易数量。

        Args:
            target_transaction (DaysTransaction): 日度交易数据对象。

        Returns:
            int: 日度交易数据中支出类型的交易数量。
        """
        
        count = 0
        for transaction in target_transaction.transactions:
            if isinstance(transaction, Transaction):
                if transaction.income_expense == "支出":
                    count += 1
        return count

    
    @classmethod
    def get_income_count(cls, target_transaction: DaysTransaction) -> int:
        """
        获取日度交易数据中收入类型的交易数量。

        Args:
            target_transaction (DaysTransaction): 日度交易数据对象。

        Returns:
            int: 日度交易数据中收入类型的交易数量。
        """
        
        count = 0
        for transaction in target_transaction.transactions:
            if isinstance(transaction, Transaction):
                if transaction.income_expense == "收入":
                    count += 1
        return count
    
    
    @classmethod
    def get_transfer_count(cls, target_transaction: DaysTransaction) -> int:
        """
        获取日度交易数据中转账类型的交易数量。

        Args:
            target_transaction (DaysTransaction): 日度交易数据对象。

        Returns:
            int: 日度交易数据中转账类型的交易数量。
        """
        
        count = 0
        for transaction in target_transaction.transactions:
            if isinstance(transaction, Transaction):
                if transaction.income_expense == "/" or transaction.income_expense == '不计收支':
                    count += 1
        return count
    
    
    @classmethod
    def get_amounts(cls, target_transaction: DaysTransaction) -> list:
        """
        获取日度交易数据中支出类型交易的金额列表。

        Args:
            target_transaction (DaysTransaction): 日度交易数据对象。

        Returns:
            list: 日度交易数据中支出类型交易的金额列表。
        """
        
        amounts = []
        for transaction in target_transaction.transactions:
            if isinstance(transaction, Transaction):
                if transaction.income_expense == "支出":
                    amounts.append(float(transaction.amount))
        return amounts
    
    
    @classmethod
    def show_transactions_in_terminal(cls, transactions: list):
        """
        在终端中显示交易数据表格。

        Args:
            transactions (list): 交易数据列表。
        """
        
        if len(transactions) <= 0 or transactions is None:
            print_log("No bills.")
            return
        else:
            headers = ["交易时间", "交易分类", "交易对方", "对方账号", "商品说明", "收/支", "金额", "收/付款方式", "交易状态", "交易订单号", "商家订单号", "备注", "来源"]
            table = []
            for transaction in transactions:
                if isinstance(transaction, Transaction):
                    row = [
                        transaction.time_.get_date_info_as_str(),
                        transaction.type_,
                        transaction.counterparty,
                        transaction.counterparty_number,
                        transaction.product,
                        transaction.income_expense,
                        transaction.amount,
                        transaction.payment_method,
                        transaction.current_status,
                        transaction.transaction_number,
                        transaction.merchant_number,
                        transaction.remark,
                        transaction.source
                    ]               
                    table.append(row)
            print(tabulate(table, headers=headers))    
            
    
    @classmethod
    def show_transactions_in_window(cls, transactions: list):
        """
        在窗口中显示交易数据。

        Args:
            transactions (list): 交易数据列表。
        """
        
        cls.show_transactions_in_terminal(transactions=transactions)
        reversed(transactions)
        show_transactions(transactions=transactions)
      
    @classmethod
    def filter_transactions_simple(cls, transactions: list, type_word: list) -> list:
        """
        简单过滤交易数据，根据交易分类类型过滤。

        Args:
            transactions (list): 交易数据列表。
            type_word (list): 需要过滤的交易分类类型列表。

        Returns:
            list: 过滤后的交易数据列表。
        """
        
        target_transaction = []
        for transaction in transactions:
            if isinstance(transaction, Transaction):
                if str(transaction.type_).replace(" ", "") in type_word:
                    target_transaction.append(transaction)
        return target_transaction
    
    @classmethod
    def filter_transactions(cls, transactions: list, rules: list) -> list:
        """
        根据过滤规则过滤交易数据。

        Args:
            transactions (list): 交易数据列表。
            rules (list): 过滤规则列表。

        Returns:
            list: 过滤后的交易数据列表。
        """
        
        target_transaction = []
        for transaction in transactions:
            if isinstance(transaction, Transaction):
                check_result = True
                for rule in rules:
                    if isinstance(rule, FilterRules):
                        if not ExtrcationRules.check_transaction_by_filter_rule(transaction=transaction, rule=rule):
                            check_result = False
                if check_result:
                    target_transaction.append(transaction)
        return target_transaction
    
    
    

