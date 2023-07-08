#/bin/bash python3
#coding: utf-8

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