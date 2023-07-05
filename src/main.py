#/bin/bash python3

from functions.read_table import ReadTransactionTable

csv_folder_path = "/Users/pengliu/Code/Grandet/bills"


if __name__ == "__main__":
    csv_files = ReadTransactionTable.extract_csv_file_path(csv_folder_path)
    target_csv_files = ReadTransactionTable.flitter_csv_file(csv_files)
    transactions_count = 0

    for item in target_csv_files:
        
        info = "Read transaction csv file: " + item
        print(info)
        
        transactions = ReadTransactionTable.open_csv(csv_file_path=item, head=False, frist_line_word='交易时间')
        transactions_count = transactions_count + len(transactions)
        
    print("All transactions count: " + str(transactions_count) + ".")
