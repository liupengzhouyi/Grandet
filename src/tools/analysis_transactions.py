#/bin/bash python3
#coding: utf-8

from modules.transaction import Transaction
from modules.transaction import YearsTransaction
from modules.transactions_tools import TransactionsTools

from functions.log4py import print_log

class AnalysisTransactions:
    
    def __init__(self, transactions: list):
        self.transactions = transactions
    
    
    def get_transactions(self) -> list:
        return self.transactions
    
    
    def get_size(self) -> int:
        return len(self.transactions)
    
    
    def get_years(self) -> list:
        years = []
        for transaction in self.transactions:
            year = transaction.get_datetime().year
            if year not in years:
                years.append(year)
        return years
    
    
    def get_months(self, target_year: int) -> list:
        months = []
        for transaction in self.transactions:
            year = transaction.get_datetime().year
            if year == target_year:
                month = transaction.get_datetime().month
                if month not in months:
                    months.append(month)
        return months


    def get_days(self, target_year: int, target_month: int) -> list:
        days = []
        for transaction in self.transactions:
            year = transaction.get_datetime().year
            if year == target_year:
                month = transaction.get_datetime().month
                if month == target_month:
                    day = transaction.get_datetime().day
                    if day not in days:
                        days.append(day)
        return days
    
    def get_every_years_transactions(self) -> dict:
        
        print_log("Begin set every years transactions.")
        years = []
        result = {}
        for transaction in self.transactions:
            year = str(transaction.get_datetime().year)
            if year not in years:
                years.append(year)
                result[year] = YearsTransaction(year=int(year))
                result[year].add_transaction(transaction)
            else:
                result[year].add_transaction(transaction)
        
        print_log(f"years number: {len(result.keys())}")
        
        for year in result.keys():
            print_log(f"{year} year has {str(TransactionsTools.get_transactions_size(target_transaction=result.get(year)))} transactions.")
        
        print_log("Set every years transactions over.")
        return result
    
    
    @classmethod
    def analyze_transactions_income(cls, transactions: list) -> tuple:
        
        key_word = "收入"
        count = 0
        money = 0.0
        temp_transactions = []
        for transaction in transactions:
            if isinstance(transaction, Transaction):
                if transaction.income_expense == key_word:
                    count += 1
                    money += float(transaction.amount)
                    temp_transactions.append(transaction)
        print_log(f"账单收入详情：交易笔数:{str(count)} 金额:{str(money)}.")
        return (count, money, temp_transactions)
    
    
    @classmethod
    def analyze_transactions_expenditure(cls, transactions: list) -> tuple:
        
        key_word = "支出"
        count = 0
        money = 0.0
        temp_transactions = []
        for transaction in transactions:
            if isinstance(transaction, Transaction):
                if transaction.income_expense == key_word:
                    count += 1
                    money += float(transaction.amount)
                    temp_transactions.append(transaction)
        print_log(f"账单收入详情：交易笔数:{str(count)} 金额:{str(money)}.")
        return (count, money, temp_transactions)

    
    @classmethod
    def analyze_transactions_no_income_and_expenditure(cls, transactions: list) -> tuple:
        
        key_word = "不计收支"
        count = 0
        money = 0.0
        temp_transactions = []
        for transaction in transactions:
            if isinstance(transaction, Transaction):
                print_log(f"{transaction.income_expense}")
                if transaction.income_expense == key_word:
                    count += 1
                    money += float(transaction.amount)
                    temp_transactions.append(transaction)
        print_log(f"账单收入详情：交易笔数:{str(count)} 金额:{str(money)}.")
        return (count, money, temp_transactions)
        