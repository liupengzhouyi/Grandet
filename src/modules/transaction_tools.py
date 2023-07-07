#/bin/bash python3

from datetime import datetime

from functions.log4py import print_log
from modules.transaction import Transaction
from modules.transaction_datetime import TransactionDateTime


def check_dt1_dt2(dt1: TransactionDateTime, dt2: TransactionDateTime) -> bool:
    
    dt1_bigger_than_dt2 = False
    dt_1 = datetime(dt1.year, dt1.month, dt1.day, dt1.hour, dt1.minute, dt1.second)
    dt_2 = datetime(dt2.year, dt2.month, dt2.day, dt2.hour, dt2.minute, dt2.second)

    if dt_1 > dt_2:
        # print_log("dt1 晚于 dt2")
        dt1_bigger_than_dt2 = False
    elif dt_1 < dt_2:
        # print_log("dt1 早于 dt2")
        dt1_bigger_than_dt2 = True
    else:
        # print_log("dt1 等于 dt2")
        dt1_bigger_than_dt2 = True
    
    return dt1_bigger_than_dt2


def cmp_transaction_by_datetime(x: Transaction, y: Transaction) -> int:
    

    if check_dt1_dt2(x.get_datetime(), y.get_datetime()):
        return 1
    else:
        return -1
    

def delete_same_transaction(transactions: list) -> list:
    
    new_transactions = []
        
    for item in transactions:
        if len(new_transactions) == 0:
            new_transactions.append(item)
        else:
            last_item  = new_transactions[-1]
            check_date_time = last_item.get_datetime().get_v_str() == item.get_datetime().get_v_str()
            check_get_transaction_number = last_item.get_transaction_number() == item.get_transaction_number()
            if check_date_time and check_get_transaction_number:
                continue
            else:
                new_transactions.append(item)
    return new_transactions

def check_number_is_float(number: str) -> bool:
    
    isFloat = False
    try:
        float(number)
    except:
        isFloat = False
    else:
        isFloat = True
    return isFloat


def get_batch_transactions_target_values(transactions: list, func: callable) -> list:
    
    batch_transactions = []
    
    for item in transactions:
        if not isinstance(item, Transaction):
            continue
        else:
            value = func(item)
            if check_number_is_float(str(value)):
                value_num = float(value)
                batch_transactions.append(value_num)
            else:
                print("Error:" + str(type(value)) + ":" + str(value))
    return batch_transactions