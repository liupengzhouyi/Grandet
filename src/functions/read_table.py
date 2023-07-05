# /bin/bash python3 read_table.py --input_file input.txt --output_file output.txt

import pandas as pd
import csv

from modules.transaction import Transaction
from modules.transaction import create_transaction


def read_table(input_file: str, output_file: str):
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


def open_csv(csv_file_path: str, head=False):
    
    with open(csv_file_path, 'r') as f:
        reader = csv.reader(f)
        head_ = head
        begin = False
        target = '交易时间'
        for row in reader:
            if not begin:
                if len(row) == 0 or target != row[0]:
                    continue
                else:
                    begin = True
                    
            if not head_:
                head_ = True
                continue
            a = create_transaction(row)
            a.show()
    print("Read over.")
