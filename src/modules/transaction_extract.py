#/bin/bash python

from gui.ui.globel_varable import set_value
from gui.ui.globel_varable import get_value

from modules.transaction import Transaction
from modules.transaction import YearsTransaction
from modules.transaction import MonthsTransaction
from modules.transaction import DaysTransaction


class ExtractTransactions:
    """
    用于从全局存储的年度交易数据中提取特定时间段的交易数据的辅助类。
    """
    
    
    def __init__(self) -> None:
        """
        初始化一个 ExtractTransactions 对象。
        """
        
        pass
    
    
    @classmethod
    def extract_all(cls) -> list:
        """
        提取所有年度交易数据中的交易对象，并返回一个列表。

        Returns:
            list: 所有年度交易数据中的交易对象列表。
        """
        
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
        """
        提取特定年份的交易数据，并返回一个列表。

        Args:
            year (int): 要提取的年份。

        Returns:
            list: 特定年份的交易数据列表。
        """
        
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
        """
        提取特定年份和月份的交易数据，并返回一个列表。

        Args:
            year (int): 要提取的年份。
            month (int): 要提取的月份。

        Returns:
            list: 特定年份和月份的交易数据列表。
        """
        
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
        """
        提取特定年份、月份和日期的交易数据，并返回一个列表。

        Args:
            year (int): 要提取的年份。
            month (int): 要提取的月份。
            day (int): 要提取的日期。

        Returns:
            list: 特定年份、月份和日期的交易数据列表。
        """
        
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