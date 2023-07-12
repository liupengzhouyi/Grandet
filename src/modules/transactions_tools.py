#/bin/bash python3
#coding: utf-8

from functions.log4py import print_log
from modules.transaction import Transaction
from modules.transaction import YearsTransaction
from modules.transaction import MonthsTransaction
from modules.transaction import DaysTransaction


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
    
    
    