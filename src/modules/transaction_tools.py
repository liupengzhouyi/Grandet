#/bin/bash python3

import os

from datetime import datetime
from functools import cmp_to_key
from functions.log4py import print_log
from modules.transaction import Transaction
from modules.transaction_datetime import TransactionDateTime
from functions.read_table import ReadTransactionTable
from functions.write_table import WriteTransactionTable
from gui.ui.globel_varable import set_value
from gui.ui.globel_varable import get_value



def check_dt1_dt2(dt1: TransactionDateTime, dt2: TransactionDateTime) -> bool:
    """
    比较两个 TransactionDateTime 对象的时间先后顺序。

    Args:
        dt1 (TransactionDateTime): 第一个 TransactionDateTime 对象。
        dt2 (TransactionDateTime): 第二个 TransactionDateTime 对象。

    Returns:
        bool: 如果 dt1 晚于 dt2，则返回 False；如果 dt1 早于或等于 dt2，则返回 True。
    """
    
    dt1_bigger_than_dt2 = False
    # 创建 datetime 对象以便比较
    dt_1 = datetime(dt1.year, dt1.month, dt1.day, dt1.hour, dt1.minute, dt1.second)
    dt_2 = datetime(dt2.year, dt2.month, dt2.day, dt2.hour, dt2.minute, dt2.second)

    if dt_1 > dt_2:
        # dt1 晚于 dt2
        dt1_bigger_than_dt2 = False
    elif dt_1 < dt_2:
        # dt1 早于 dt2
        dt1_bigger_than_dt2 = True
    else:
        # dt1 等于 dt2
        dt1_bigger_than_dt2 = True

    return dt1_bigger_than_dt2



def cmp_transaction_by_datetime(x: Transaction, y: Transaction) -> int:
    """
    比较两个交易对象的时间先后顺序。

    Args:
        x (Transaction): 第一个交易对象。
        y (Transaction): 第二个交易对象。

    Returns:
        int: 如果 x 的时间晚于 y，则返回 1；如果 x 的时间早于 y，则返回 -1。
    """
    if check_dt1_dt2(x.get_datetime(), y.get_datetime()):
        # x 的时间晚于 y
        return 1
    else:
        # x 的时间早于 y
        return -1

    
def delete_same_transaction(transactions: list) -> list:
    """
    从交易列表中删除具有相同交易号的交易对象，并返回新的交易列表。

    Args:
        transactions (list): 包含交易对象的列表。

    Returns:
        list: 不包含相同交易号交易的新列表。
    """
    new_transactions = []  # 存储不包含相同交易号的新交易列表
    transaction_ids = []  # 存储已经处理过的交易号

    for item in transactions:
        if isinstance(item, Transaction):
            # 获取交易的交易号并去除空格和制表符
            transaction_id = str(item.transaction_number).replace(" ", "").replace("\t", "")

            if transaction_id not in transaction_ids:
                # 如果交易号不在已处理列表中，将该交易添加到新列表中
                transaction_ids.append(transaction_id)
                new_transactions.append(item)
            else:
                # 如果交易号已经存在于已处理列表中，记录日志并不添加该交易
                print_log(f"{item.time_.get_v_str()}: {item.transaction_number}, has same transaction number.")

    return new_transactions


def check_number_is_float(number: str) -> bool:
    """
    检查给定字符串是否可以转换为浮点数。

    Args:
        number (str): 要检查的字符串。

    Returns:
        bool: 如果字符串可以转换为浮点数，则返回 True；否则返回 False。
    """
    isFloat = False  # 用于存储检查结果的布尔变量

    try:
        float(number)  # 尝试将字符串转换为浮点数
    except:
        isFloat = False  # 转换失败，设置为 False
    else:
        isFloat = True   # 转换成功，设置为 True

    return isFloat



def get_batch_transactions_target_values(transactions: list, func: callable) -> list:
    """
    从交易对象列表中提取目标值，并返回包含这些目标值的新列表。

    Args:
        transactions (list): 包含交易对象的列表。
        func (callable): 用于从交易对象中提取目标值的函数。

    Returns:
        list: 包含提取的目标值的新列表。
    """
    
    batch_transactions = []  # 存储提取的目标值的新列表

    for item in transactions:
        if not isinstance(item, Transaction):
            continue
        else:
            value = func(item)  # 使用提供的函数从交易对象中提取目标值
            if check_number_is_float(str(value)):
                value_num = float(value)  # 如果目标值可以转换为浮点数，将其转换为浮点数并添加到新列表
                batch_transactions.append(value_num)
            else:
                # 如果目标值无法转换为浮点数，记录错误信息并不添加到新列表
                print("Error:" + str(type(value)) + ":" + str(value))

    return batch_transactions


def analysis_all_bills(target_csv_files: list, csv_folder_path: str) -> list:
    """
    分析多个 CSV 文件中的交易数据，并返回合并并去除重复后的交易列表。

    Args:
        target_csv_files (list): 包含目标 CSV 文件名的列表。
        csv_folder_path (str): CSV 文件所在的文件夹路径。

    Returns:
        list: 合并并去除重复后的交易列表。
    """
    all_transactions = []  # 存储所有交易数据的列表

    for item in target_csv_files:
        # 构造 CSV 文件路径
        csv_file_path = os.path.join(csv_folder_path, item)
        # 打印日志信息
        # info = "Read transaction csv file: " + item
        # print_log(info)

        # 打开 CSV 文件并获取交易数据
        transactions = ReadTransactionTable.open_csv(csv_file_path=item,
                                                     head=False,
                                                     frist_line_word='交易时间')
        # 将获取的交易数据扩展到所有交易数据列表中
        all_transactions.extend(transactions)
        
    # 根据交易时间对所有交易数据进行排序
    all_transactions.sort(key=cmp_to_key(cmp_transaction_by_datetime))
    # 删除具有相同交易号的交易，并获取新的交易列表
    target_transactions = delete_same_transaction(all_transactions)
    # 打印日志信息，记录交易数量
    print_log("All transactions count: " + str(len(target_transactions)) + ".")
    print_log("All transactions count: " + str(len(all_transactions)) + ".")
    # 将新的交易列表存储在全局变量中
    set_value("all_transactions_as_list", target_transactions)
    
    return target_transactions  # 返回合并并去除重复后的交易列表


def save_transactions_to_file(all_transactions: list, transaction_file_path: str, head: list):
    """
    将交易数据列表保存到 CSV 文件中。

    Args:
        all_transactions (list): 包含交易数据的列表。
        transaction_file_path (str): 要保存到的目标 CSV 文件路径。
        head (list): CSV 文件的字段名列表。

    Returns:
        None
    """
    target_transactions_list = []  # 存储要保存到文件的交易数据列表

    for item in all_transactions:
        if isinstance(item, Transaction):
            # 将交易对象转换为列表形式并添加到目标列表中
            target_transactions_list.append(item.to_list())

    # 使用 WriteTransactionTable 类将数据写入 CSV 文件
    WriteTransactionTable.write_csv(csv_file_path=transaction_file_path,
                                    fields=head,
                                    rows=target_transactions_list)
