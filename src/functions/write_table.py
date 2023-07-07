#/bin/bash python3

import csv


class WriteTransactionTable:
    
    def __init__(self) -> None:
        
        pass
    
    
    @classmethod
    def write_csv(cls, csv_file_path: str, fields: list, rows: list):
        
        with open(csv_file_path, 'w', encoding='utf-8') as f:
            # using csv.writer method from CSV package
            write = csv.writer(f)
            write.writerow(fields)
            write.writerows(rows)
            
            