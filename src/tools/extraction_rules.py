#/bin/bash python3

from modules.transaction import Transaction


class ExtrcationRules:
    
    def __init__(self) -> None:
        pass
    
    @classmethod
    def get_income(cls, transaction: Transaction) -> float:
        
        value = 0
        if '收入' in str(transaction.income_expense):
            value = transaction.amount 
        return value
        
    @classmethod
    def get_expense(cls, transaction: Transaction) -> float:
        
        value = 0
        if '支出' in str(transaction.income_expense):
            value = transaction.amount 
        return value