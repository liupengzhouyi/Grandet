#/bin/bash python3

import csv

from functions.log4py import print_log
from functools import cmp_to_key  
from functions.read_table import ReadTransactionTable
from functions.write_table import WriteTransactionTable
from modules.transaction_tools import cmp_transaction_by_datetime
from modules.transaction import Transaction
from modules.transaction_tools import delete_same_transaction
from modules.inject_style import InjectStyle


csv_folder_path = "/Users/pengliu/Code/Grandet/bills/"

transaction_file_path = "/Users/pengliu/Code/Grandet/bills/all.csv"
    
    
if __name__ == "__main__":
    csv_files = ReadTransactionTable.extract_csv_file_path(csv_folder_path)
    target_csv_files = ReadTransactionTable.flitter_csv_file(csv_files)
    transactions_count = 0
    
    # target_csv_files = ['']
    all_transactions = []
    print(target_csv_files[2])
    head = ReadTransactionTable.read_csv_head(csv_file_path=target_csv_files[2], frist_line_word="交易时间")
    head = list(filter(lambda x: x != '', head))
    head = InjectStyle.add_source_in_head(transaction_head=head, source="来源")

    for item in target_csv_files:

        info = "Read transaction csv file: " + item
        print_log(info)
        file_source = str(item).replace(csv_folder_path, "").split('/')[0]
        info = "The file source was " + file_source
        print_log(info)
        transactions = ReadTransactionTable.open_csv(csv_file_path=item,
                                                     head=False,
                                                     frist_line_word='交易时间',
                                                     source=file_source)
        all_transactions.extend(transactions)

    all_transactions.sort(key=cmp_to_key(cmp_transaction_by_datetime))
    target_transactions = delete_same_transaction(all_transactions)

    print_log("All transactions count: " + str(len(target_transactions)) + ".")
    print_log("All transactions count: " + str(len(all_transactions)) + ".")
    
    target_transactions_list = []
    for item in all_transactions:
        if isinstance(item, Transaction):
            target_transactions_list.append(item.to_list())
            if len(item.to_list()) != 13:
                    print(len(item.to_list()))
            
    WriteTransactionTable.write_csv(csv_file_path=transaction_file_path, fields=head, rows=target_transactions_list)
