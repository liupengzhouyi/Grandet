#/bin/bash python3

import csv
import math

from functools import cmp_to_key

from functions.log4py import print_log
from functions.read_table import ReadTransactionTable
from functions.write_table import WriteTransactionTable

from modules.transaction import Transaction

from modules.transaction_tools import get_batch_transactions_target_values
from modules.transaction_tools import save_transactions_to_file
from modules.transaction_tools import analysis_all_bills

from modules.inject_style import InjectStyle
from modules.split_transaction import SplitTransaction

from tools.extraction_rules import ExtrcationRules

from gui.create_image.create_image import GenarationImage

from gui.ui.main_windows import run_main_windows
from gui.ui.show_transactions_as_table import ShowTransaction

from tools.analysis_transactions import AnalysisTransactions

from modules.transactions_tools import TransactionsTools
from modules.transaction_filter import FilterRules
from modules.transaction_filter import FilterRulesFactory


csv_folder_path = "/Users/pengliu/Code/Grandet/bills/"
transaction_file_path = "/Users/pengliu/Code/Grandet/bills/all.csv"
save_transaction = False


if __name__ == "__main__":
    
    model = 'ui'
    # model = 'command'
    if model == 'ui':
        run_main_windows()
    else:
        csv_files = ReadTransactionTable.extract_csv_file_path(csv_folder_path)
        target_csv_files = ReadTransactionTable.flitter_csv_file(csv_files)
        transactions_count = 0

        all_transactions = []
        
        print(target_csv_files[2])
        head = ReadTransactionTable.read_csv_head(csv_file_path=target_csv_files[2], frist_line_word="交易时间")
        head = list(filter(lambda x: x != '', head))
        
        if head[3] != "对方账号":
            head.insert(3, "对方账号")
        
        head = InjectStyle.add_source_in_head(transaction_head=head, source="来源")
        print(head)
        
        target_transactions = analysis_all_bills(target_csv_files=target_csv_files, csv_folder_path=csv_folder_path)

        # rules = []
        # rules.append(FilterRulesFactory(name="交易对方", operation="包含", value="姜威"))
        # rules.append(FilterRulesFactory(name="交易对方", operation="不等于", value=""))
        # #  add your code here
        # a = TransactionsTools.filter_transactions(transactions=target_transactions, rules=rules)
        # print(type(a))
        # print(len(a))
        # ShowTransaction.show_transactions(transactions=a)
        
        analysis = AnalysisTransactions(transactions=target_transactions)
        
        print(f"Target transactions: {str(analysis.get_size())}")
        
        print(f"Source transactions years: {str(analysis.get_years())}")
        
        print(f"Source transactions months: {str(analysis.get_months(target_year=2022))}")
        
        print(f"Source transactions days: {str(analysis.get_days(target_year=2022, target_month=11))}")
        
        every_years_transactions = analysis.get_every_years_transactions()

        if save_transaction:
            save_transactions_to_file(all_transactions=all_transactions,
                                      transaction_file_path=transaction_file_path,
                                      head=head)
            
        date_infos = SplitTransaction.select_every_day(target_transactions, 2023, 5)
        data_values = []
        for item in date_infos:
            year = int(str(item).split("-")[0])
            month = int(str(item).split("-")[1])
            day = int(str(item).split("-")[2])
            targets = SplitTransaction.select_one_day(target_transactions, year=year, month=month, day=day)
            a = get_batch_transactions_target_values(targets, ExtrcationRules.get_expense)
            one_day_sum = math.fsum(a)
            one_day_sum = round(one_day_sum, 2)
            data_values.append(one_day_sum)
            print_log(f"select {item} transaction: {str(len(targets))} olders, sun value is {str(one_day_sum)}, infos: {str(a)}") 
        GenarationImage.genaration_month_image(values=data_values, labels=date_infos)

