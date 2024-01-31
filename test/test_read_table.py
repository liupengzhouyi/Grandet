import unittest

from functions.read_table import ReadTransactionTable


# test
class TestReadTransactionTable(unittest.TestCase):
    
    def test_extract_csv_file_path(self):
        
        folder_path = "./test/source"
        result = ReadTransactionTable().extract_csv_file_path(folder_path=folder_path)
        self.assertEqual(len(result), 2)
        
        
    def test_flitter_csv_file(self):
        
        folder_path = "./test/source"
        result = ReadTransactionTable().extract_csv_file_path(folder_path=folder_path)
        new_result = ReadTransactionTable().flitter_csv_file(result)
        self.assertEqual(len(new_result), 2)
        
        
    def test_alipay_or_wechatI(self):
        
        csv_file_path = "./test/source/alipay_bills.csv"
        info = ReadTransactionTable().alipay_or_wechat(csv_file_path)
        self.assertEqual(info, 'alipay')
        
    def test_alipay_or_wechatII(self):
        
        csv_file_path = "./test/source/wechat_bill.csv"
        info = ReadTransactionTable().alipay_or_wechat(csv_file_path)
        self.assertEqual(info, 'wechat')