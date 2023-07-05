#/bin/bash python3

from functions.read_table import open_csv


csv_file_path = "/Users/pengliu/Code/Grandet/bills/wechat/微信支付账单(20211001-20211201).csv"
csv_file_path = '/Users/pengliu/Code/Grandet/bills/alipay/alipay_2020.csv'
open_csv(csv_file_path)
