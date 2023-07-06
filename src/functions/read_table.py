# /bin/bash python3

import pandas as pd
import csv
import os

from functions.log4py import print_log

from modules.transaction import Transaction
from modules.transaction import create_transaction
from modules.inject_style import InjectStyle


class ReadTransactionTable:

    
    def __init__(self) -> None:
        pass
    
    @classmethod
    def extract_csv_file_path(cls, folder_path: str) -> list:
        
        csv_file_paths = []
        try:
            for filename in os.listdir(folder_path):
                
                temp_path = os.path.join(folder_path, filename)
                if os.path.isfile(temp_path):
                    csv_file_paths.append(temp_path)
                else:
                    temp_files = cls.extract_csv_file_path(temp_path)
                    for item in temp_files:
                        csv_file_paths.append(os.path.join(folder_path, item))
        except Exception:
            print_log("Can't open fodler:" + folder_path)
            return csv_file_paths
        return csv_file_paths

    @classmethod
    def flitter_csv_file(cls, csv_files: list) -> list:
        
        target_csv_files = []
        for item in csv_files:
            file_name = os.path.basename(item)
            if file_name.endswith(".csv") and not file_name.startswith("alipay_record"):
                target_csv_files.append(item)
        return target_csv_files


    @classmethod
    def read_table(cls, input_file: str, output_file: str):
        """
        Reads a table from the input file and writes it to the output file.

        Parameters:
            input_file (str): The path to the input file.
            output_file (str): The path to the output file.

        Returns:
            None
        """
        df = pd.read_csv(input_file)
        df.to_csv(output_file, index=False)


    @classmethod
    def read_csv_head(cls, csv_file_path: str, frist_line_word="") -> list:
        
        heads = []
        with open(csv_file_path, 'r') as f:
            reader = csv.reader(f)
            begin = False
            target = frist_line_word
            for row in reader:
                # print(row)
                if not begin:
                    if len(row) == 0 or target != row[0]:
                        continue
                    else:
                        begin = True
                if begin:
                    heads = row
                    break
        return heads


    @classmethod
    def open_csv(cls, csv_file_path: str, head=False, frist_line_word="", source="alipay") -> list:
        
        transactions = []
        with open(csv_file_path, 'r') as f:
            reader = csv.reader(f)
            head_ = head
            begin = False
            target = frist_line_word
            for row in reader:
                if not begin:
                    if len(row) == 0 or target != row[0]:
                        continue
                    else:
                        begin = True
                        
                if not head_:
                    head_ = True
                    continue

                temp = create_transaction(row)
                temp_transaction_with_source = InjectStyle.add_source(temp, source)
                # temp_transaction_with_source.show()
                transactions.append(temp_transaction_with_source)
                
            print_log(f"Read over. Size: {str(len(transactions))} transactions.")
        return transactions
        
