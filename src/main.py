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

from tools.analysis_transactions import AnalysisTransactions


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
        
        target_transactions = analysis_all_bills(target_csv_files=target_csv_files, 
                                                 csv_folder_path=csv_folder_path)

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

