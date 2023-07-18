#/bin/bash python3

from modules.transaction import Transaction
from modules.transaction_filter import FilterRules


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
    
    
    @classmethod
    def add_taget(cls, transaction: Transaction, rules: list) -> Transaction:
        
        pass
    
    
    @classmethod
    def check_transaction_by_filter_rule(cls, transaction: Transaction, rule: FilterRules) -> bool:
        
        value = transaction.get_value_str_by_name(name=rule.name)
        target_value = rule.value
        if rule.operation == "等于":
            result = target_value == value
        elif rule.operation == "包含":
            result = target_value in value
        elif rule.operation == "不包含":
            result =target_value not in value
        elif rule.operation == "不等于":
            result = target_value != value
        else:
            result = False
        return result
    
    
    def paly():
        
        pass

