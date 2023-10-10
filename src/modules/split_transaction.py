#/bin/bash python

from modules.transaction import Transaction
from modules.transaction_datetime import TransactionDateTime


class SplitTransaction:
    
    def __init__(self):
        
        print()
        
        
    @classmethod
    def select_one_day(cls, transactions: list, year: int, month: int, day: int) -> list:
        
        target_transactions = []
        
        for transaction in transactions:
            check_status = transaction.get_datetime().is_target_day(year, month, day)
            if check_status:
                target_transactions.append(transaction)

        return target_transactions
    
    @classmethod
    def select_one_month(cls, transactions: list, year: int, month: int) -> list:
        
        target_transactions = []
        
        for transaction in transactions:
            check_status = transaction.get_datetime().is_target_month(year, month)
            if check_status:
                target_transactions.append(transaction)

        return target_transactions
    
    @classmethod
    def select_every_day(cls, transactions: list, year: int=-1, month: int=-1) -> list:
        
        date_infos = []
        
        if year == -1 or month == -1:
            pass
        else:
            transactions = cls.select_one_month(transactions, year, month)
            
        for transaction in transactions:
            
            date_info = transaction.get_date_info_as_str()
            if date_info not in date_infos:
                date_infos.append(date_info)
        
        return date_infos
        
        