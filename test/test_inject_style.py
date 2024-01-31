import unittest

from modules.transaction import Transaction
from modules.inject_style import InjectStyle


class TestInjectStyle(unittest.TestCase):
    
    def test_add_source_in_head(self):
        transaction_head = ['id', 'amount']
        source = 'external'
        updated_head = InjectStyle.add_source_in_head(transaction_head, source)
        self.assertEqual(updated_head, ['id', 'amount', 'external'])
        
    
    def test_add_source(self):
        transaction = Transaction()
        source = "example_source"
        updated_transaction = InjectStyle.add_source(transaction, source)
        self.assertEqual(updated_transaction.source, source)