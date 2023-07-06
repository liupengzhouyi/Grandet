#/bin/bash python3

from modules.transaction import Transaction

class InjectStyle:
    
    def __init__(self, style: str):
        
        self.style = style
        

    @classmethod
    def add_source_in_head(cls, transaction_head: list, source: str) -> list:
        
        transaction_head.append(source)
        return transaction_head
    
    @classmethod
    def add_source(cls, transaction: Transaction, source: str) -> Transaction:
        
        transaction.set_source(source)
        return transaction
    

        
    
        