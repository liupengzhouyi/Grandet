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
    