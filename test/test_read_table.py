import unittest

from functions.read_table import ReadTransactionTable


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
        
    def test_read_csv_head(self):
        
        csv_file_path = "./test/source/alipay_bills.csv"
        head = ReadTransactionTable().read_csv_head(csv_file_path=csv_file_path,
                                                    frist_line_word="交易时间")
        self.assertEqual(len(head), 13)
        
    def test_open_csv_head_wechat(self):
        
        csv_file_path = "./test/source/wechat_bill.csv"
        # The key word in the first line
        frist_line_word = "交易时间"
        result = ReadTransactionTable.open_csv(csv_file_path=csv_file_path, head=False, frist_line_word=frist_line_word)
        self.assertEqual(len(result), 4)
        
    def test_open_csv_head_alipay(self):
        
        csv_file_path = "./test/source/alipay_bills.csv"
        # The key word in the first line
        frist_line_word = "交易时间"
        result = ReadTransactionTable.open_csv(csv_file_path=csv_file_path, head=False, frist_line_word=frist_line_word)
        self.assertEqual(len(result), 5)
        # Add more assertions for the extracted transactions