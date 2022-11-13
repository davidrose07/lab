from account_test import Account

class Test:    
    def setup_method(self):
        self.p1 = Account('Jane')
        self.p2 = Account('John')
        
    def teardown_method(self):
        del self.p1
        del self.p2
    
    def test__init__(self):
        assert self.p1.get_name() == 'Jane'
        assert self.p1.get_balance() == 0
        assert self.p2.get_name() == 'John'
        assert self.p2.get_balance() == 0
        
    
    def test_deposit(self):    
        assert self.p1.deposit("") == False
        assert self.p1.deposit("str") == False
        assert self.p1.deposit(-1) == False
        assert self.p1.deposit(0) == False
        assert self.p1.deposit(1.0) == True
        assert self.p1.deposit(1) == True
        
        assert self.p2.deposit("") == False
        assert self.p2.deposit("str") == False
        assert self.p2.deposit(-1) == False
        assert self.p2.deposit(0) == False
        assert self.p2.deposit(1.0) == True
        assert self.p2.deposit(1) == True
                 
    def test_withdrawl(self):
        assert self.p1.withdrawl("") == False
        assert self.p1.withdrawl("str") == False
        assert self.p1.withdrawl(-1) == False
        assert self.p1.withdrawl(0) == False
        assert self.p1.get_balance() == 0
        assert self.p1.withdrawl(1) == False
        assert self.p1.deposit(10)
        assert self.p1.get_balance() == 10
        assert self.p1.withdrawl(11) == False
        
        assert self.p2.withdrawl("") == False
        assert self.p2.withdrawl("str") == False
        assert self.p2.withdrawl(-1) == False
        assert self.p2.withdrawl(0) == False
        assert self.p2.get_balance() == 0
        assert self.p2.withdrawl(1) == False
        assert self.p2.deposit(10)
        assert self.p1.get_balance() == 10
        assert self.p2.withdrawl(11) == False
     