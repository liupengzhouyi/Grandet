#/bin/bash python

from gui.ui.globel_varable import set_value
from gui.ui.globel_varable import get_value

from modules.transaction import Transaction
from modules.transaction import YearsTransaction
from modules.transaction import MonthsTransaction
from modules.transaction import DaysTransaction


class ExtractTransactions:
    
    
    def __init__(self) -> None:
        pass
    
    
    @classmethod
    def extract_all(cls) -> list:
        
        all_transactions = []
        every_years_transactions = get_value("every_years_transactions")
        if every_years_transactions is None:
            return all_transactions
        if isinstance(every_years_transactions, dict):
            for year in every_years_transactions.keys():
                temp_transactions = every_years_transactions.get(year)
                if isinstance(temp_transactions, YearsTransaction):
                    all_transactions.extend(temp_transactions.transactions)
        return all_transactions
    
    
    @classmethod
    def extract_by_year(cls, year: int) -> list:
        
        all_transactions = []
        every_years_transactions = get_value("every_years_transactions")
        if every_years_transactions is None:
            return all_transactions
        if isinstance(every_years_transactions, dict):
            for temp_year in every_years_transactions.keys():
                if temp_year == year:
                    temp_transactions = every_years_transactions.get(year)
                    if isinstance(temp_transactions, YearsTransaction):
                        all_transactions.extend(temp_transactions.transactions)
        return all_transactions
    
    
    @classmethod
    def extract_by_year_month(cls, year: int, month: int) -> list:
        
        print(f"extract_by_year:{str(year)}-month:{str(month)}.")
        all_transactions = []
        every_years_transactions = get_value("every_years_transactions")
        if every_years_transactions is None:
            print("None error")
            return all_transactions
        if isinstance(every_years_transactions, dict):
            for temp_year in every_years_transactions.keys():
                if temp_year == str(year):
                    temp_transactions = every_years_transactions.get(temp_year)
                    if isinstance(temp_transactions, YearsTransaction):
                        month_dics = temp_transactions.to_MonthsTransaction()
                        for temp_month in month_dics.keys():
                            if temp_month == str(month):
                                temp_month_transactions = month_dics.get(temp_month)
                                if isinstance(temp_month_transactions, MonthsTransaction):
                                    all_transactions.extend(temp_month_transactions.transactions)
                                else:
                                    print(f"MonthsTransaction 类型 错误.")
                            else:
                                print(f"非目标月")
                    else:
                        print(f"YearsTransaction 类型 错误.")
                else:
                    print(f"非目标年")
        else:
            print(f"读取账单错误.")
        return all_transactions
    
    
    @classmethod
    def extract_by_year_month_day(cls, year: int, month: int, day: int) -> list:
        
        all_transactions = []
        every_years_transactions = get_value("every_years_transactions")
        if every_years_transactions is None:
            return all_transactions
        if isinstance(every_years_transactions, dict):
            for temp_year in every_years_transactions.keys():
                if temp_year == str(year):
                    temp_transactions = every_years_transactions.get(temp_year)
                    if isinstance(temp_transactions, YearsTransaction):
                        month_dics = temp_transactions.to_MonthsTransaction()
                        for temp_month in month_dics.keys():
                            if temp_month == str(month):
                                temp_month_transactions = month_dics.get(temp_month)
                                if isinstance(temp_month_transactions, MonthsTransaction):
                                    days_transactions = temp_month_transactions.to_DaysTransaction()
                                    for temp_day in days_transactions.keys():
                                        if temp_day == str(day):
                                            temp_day_transactions = days_transactions.get(temp_day)
                                            if isinstance(temp_day_transactions, DaysTransaction):
                                                all_transactions.extend(temp_day_transactions.transactions)
        return all_transactions