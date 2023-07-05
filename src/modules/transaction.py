#/bin/bash python3


from tabulate import tabulate

from modules.transaction_datetime import TransactionDateTime

# alipay
# 交易时间,交易分类,交易对方,对方账号,商品说明,收/支,金额,收/付款方式,交易状态,交易订单号,商家订单号,备注,

# wechat
# 交易时间,交易分类,交易对方,对方账号,商品说明,收/支,金额,收/付款方式,交易状态,交易订单号,商家订单号,备注,

class Transaction:
    
    def __init__(self):
        
        self.time_ = TransactionDateTime()
        self.type_ = ''
        self.counterparty = ''
        self.product = ''
        self.income_expense = ''
        self.amount = ''
        self.payment_method = ''
        self.current_status = ''
        self.transaction_number = ''
        self.merchant_number = ''
        self.remark = ''
        self.source = ''
        
    def init_by_list(self, infos: list):
        
        time_ = infos[0]
        type_ = infos[1]
        counterparty = infos[2]
        product = infos[3]
        income_expense = infos[4]
        amount = infos[5]
        payment_method = infos[6]
        current_status = infos[7]
        transaction_number = infos[8]
        merchant_number = infos[9]
        remark = infos[10]
        
        self.time_.inject_datetime_str(time_)
        self.type_ = type_
        self.counterparty = counterparty
        self.product = product
        self.income_expense = income_expense
        self.amount = amount
        self.payment_method = payment_method
        self.current_status = current_status
        self.transaction_number = transaction_number
        self.merchant_number = merchant_number
        self.remark = remark
        
    def set_source(self, source):
        
        self.source = source
        
    def __str__(self):
        
        return str(self.__dict__)


    def show(self):
        


        headers = ["Field", "Value"]
        data = [
            ["Time", self.time_.get_v_str()],
            ["Type", self.type_],
            ["Counterparty", self.counterparty],
            ["Product", self.product],
            ["Income/Expense", self.income_expense],
            ["Amount", self.amount],
            ["Payment Method", self.payment_method],
            ["Current Status", self.current_status],
            ["Transaction Number", self.transaction_number],
            ["Merchant Number", self.merchant_number],
            ["Remark", self.remark]
        ]
        # print()
        print(tabulate(data, headers, tablefmt="simple"))


        # print(f"Time: {self.time_}")
        # print(f"Type: {self.type_}")
        # print(f"Counterparty: {self.counterparty}")
        # print(f"Product: {self.product}")
        # print(f"Income/Expense: {self.income_expense}")
        # print(f"Amount: {self.amount}")
        # print(f"Payment Method: {self.payment_method}")
        # print(f"Current Status: {self.current_status}")
        # print(f"Transaction Number: {self.transaction_number}")
        # print(f"Merchant Number: {self.merchant_number}")
        # print(f"Remark: {self.remark}")


def create_transaction(infos: list) -> Transaction:
    
    transaction = Transaction()
    transaction.init_by_list(infos)
    return transaction
    