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


csv_folder_path = "/Users/pengliu/Code/Grandet/bills/"
transaction_file_path = "/Users/pengliu/Code/Grandet/bills/all.csv"
save_transaction = False


# def analysis_all_bills(target_csv_files: list, csv_folder_path: str) -> list:
    
#     all_transactions = []

#     for item in target_csv_files:
#         info = "Read transaction csv file: " + item
#         print_log(info)
#         file_source = str(item).replace(csv_folder_path, "").split('/')[0]
#         info = "The file source was " + file_source
#         print_log(info)
        
#         transactions = ReadTransactionTable.open_csv(csv_file_path=item,
#                                                     head=False,
#                                                     frist_line_word='交易时间',
#                                                     source=file_source)
#         all_transactions.extend(transactions)
#     all_transactions.sort(key=cmp_to_key(cmp_transaction_by_datetime))
#     target_transactions = delete_same_transaction(all_transactions)
#     print_log("All transactions count: " + str(len(target_transactions)) + ".")
#     print_log("All transactions count: " + str(len(all_transactions)) + ".")
#     return target_transactions


# def save_transactions_to_file(all_transactions: list, transaction_file_path: str, head: list):
    
#     target_transactions_list = []
#     for item in all_transactions:
#         if isinstance(item, Transaction):
#             target_transactions_list.append(item.to_list())
#     WriteTransactionTable.write_csv(csv_file_path=transaction_file_path,
#                                     fields=head,
#                                     rows=target_transactions_list)


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

        if save_transaction:
            save_transactions_to_file(all_transactions=all_transactions,
                                      transaction_file_path=transaction_file_path,
                                      head=head)
            # target_transactions_list = []
            # for item in all_transactions:
            #     if isinstance(item, Transaction):
            #         target_transactions_list.append(item.to_list())
            #         # if len(item.to_list()) != 13:
            #         #         print(len(item.to_list()))
            # WriteTransactionTable.write_csv(csv_file_path=transaction_file_path, fields=head, rows=target_transactions_list)

        # targets = SplitTransaction.select_one_month(target_transactions, 2023, 6)
        
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

