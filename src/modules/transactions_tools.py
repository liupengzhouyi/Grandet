#/bin/bash python3
#coding: utf-8

from tabulate import tabulate

from functions.log4py import print_log
from modules.transaction import Transaction
from modules.transaction import DaysTransaction
from modules.transaction import MonthsTransaction
from modules.transaction import YearsTransaction

from gui.ui.show_transactions_as_table import ShowTransaction

class TransactionsTools:
    
    def __init__(self) -> None:
        pass
        
    @classmethod
    def get_transactions_size(cls, target_transaction: YearsTransaction) -> int:
        
        return len(target_transaction.transactions)
    
    
    @classmethod
    def get_transactions_size(cls, target_transaction: MonthsTransaction) -> int:
        
        return len(target_transaction.transactions)
    
    
    @classmethod
    def get_transactions_size(cls, target_transaction: DaysTransaction) -> int:
        
        return len(target_transaction.transactions)
    
    
    @classmethod
    def get_summary_count(cls, target_transaction: YearsTransaction) -> int:
        
        count = 0
        for transaction in target_transaction.transactions:
            if isinstance(transaction, Transaction):
                if transaction.income_expense == "支出":
                    count += 1
        return count

    
    @classmethod
    def get_income_count(cls, target_transaction: YearsTransaction) -> int:
        
        count = 0
        for transaction in target_transaction.transactions:
            if isinstance(transaction, Transaction):
                if transaction.income_expense == "收入":
                    count += 1
        return count
    
    
    @classmethod
    def get_transfer_count(cls, target_transaction: YearsTransaction) -> int:
        
        count = 0
        for transaction in target_transaction.transactions:
            if isinstance(transaction, Transaction):
                if transaction.income_expense == "/" or transaction.income_expense == '不计收支':
                    count += 1
        return count
    
    
    @classmethod
    def get_amounts(cls, target_transaction: YearsTransaction) -> list:
        
        amounts = []
        for transaction in target_transaction.transactions:
            if isinstance(transaction, Transaction):
                if transaction.income_expense == "支出":
                    amounts.append(float(transaction.amount))
        return amounts
    
    
    @classmethod
    def get_transactions_size(cls, target_transaction: MonthsTransaction) -> int:
        
        return len(target_transaction.transactions)
    
    
    @classmethod
    def get_transactions_size(cls, target_transaction: MonthsTransaction) -> int:
        
        return len(target_transaction.transactions)
    
    
    @classmethod
    def get_transactions_size(cls, target_transaction: DaysTransaction) -> int:
        
        return len(target_transaction.transactions)
    
    
    @classmethod
    def get_summary_count(cls, target_transaction: MonthsTransaction) -> int:
        
        count = 0
        for transaction in target_transaction.transactions:
            if isinstance(transaction, Transaction):
                if transaction.income_expense == "支出":
                    count += 1
        return count

    
    @classmethod
    def get_income_count(cls, target_transaction: MonthsTransaction) -> int:
        
        count = 0
        for transaction in target_transaction.transactions:
            if isinstance(transaction, Transaction):
                if transaction.income_expense == "收入":
                    count += 1
        return count
    
    
    @classmethod
    def get_transfer_count(cls, target_transaction: MonthsTransaction) -> int:
        
        count = 0
        for transaction in target_transaction.transactions:
            if isinstance(transaction, Transaction):
                if transaction.income_expense == "/" or transaction.income_expense == '不计收支':
                    count += 1
        return count
    
    
    @classmethod
    def get_amounts(cls, target_transaction: MonthsTransaction) -> list:
        
        amounts = []
        for transaction in target_transaction.transactions:
            if isinstance(transaction, Transaction):
                if transaction.income_expense == "支出":
                    amounts.append(float(transaction.amount))
        return amounts
    
    
    @classmethod
    def get_transactions_size(cls, target_transaction: DaysTransaction) -> int:
        
        return len(target_transaction.transactions)
    
    
    @classmethod
    def get_transactions_size(cls, target_transaction: DaysTransaction) -> int:
        
        return len(target_transaction.transactions)
    
    
    @classmethod
    def get_transactions_size(cls, target_transaction: DaysTransaction) -> int:
        
        return len(target_transaction.transactions)
    
    
    @classmethod
    def get_summary_count(cls, target_transaction: DaysTransaction) -> int:
        
        count = 0
        for transaction in target_transaction.transactions:
            if isinstance(transaction, Transaction):
                if transaction.income_expense == "支出":
                    count += 1
        return count

    
    @classmethod
    def get_income_count(cls, target_transaction: DaysTransaction) -> int:
        
        count = 0
        for transaction in target_transaction.transactions:
            if isinstance(transaction, Transaction):
                if transaction.income_expense == "收入":
                    count += 1
        return count
    
    
    @classmethod
    def get_transfer_count(cls, target_transaction: DaysTransaction) -> int:
        
        count = 0
        for transaction in target_transaction.transactions:
            if isinstance(transaction, Transaction):
                if transaction.income_expense == "/" or transaction.income_expense == '不计收支':
                    count += 1
        return count
    
    
    @classmethod
    def get_amounts(cls, target_transaction: DaysTransaction) -> list:
        
        amounts = []
        for transaction in target_transaction.transactions:
            if isinstance(transaction, Transaction):
                if transaction.income_expense == "支出":
                    amounts.append(float(transaction.amount))
        return amounts
    
    
    @classmethod
    def show_transactions_in_terminal(cls, transactions: list):
        
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
        
        
        ShowTransaction.show_transactions(transactions=transactions)          
