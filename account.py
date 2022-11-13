


class Account:
    def __init__(self,name:str) -> None:
        '''
        Initialization function that creates an instance of the class and takes in the name of the account
        
        :param name: The name of the account 
        :return: None        
        '''
        self.__account_name: str = name
        self.__account_balance = 0
        
    def deposit(self,amount:float) -> bool:
        '''
        This function takes in a deposit amount and adds to the account balance if the deposit is greater than zero
        
        :param: the amount to add to the private instance variable (__account_balance)
        :return: returns true if successful and false if not successful
        
        '''
        try:
            if amount > 0:
                self.__account_balance += amount  # add amount to balance
                return True
            else:
                return False
        except TypeError:  # amount is not numeric
            return False
    
    def withdrawl(self,amount:float) -> bool:
        '''
        This function takes in a withdrawl amount and subtracts it from the account balance if withdrawl is greater than zero
        
        :param: the amount to subtract from the private instance variable (__account_balance)
        :return: returns True if successful and False if not successful
        '''
        try:
            if (amount > 0) and (amount <= self.__account_balance):
                self.__account_balance -= amount  # subtract amount from balance
                return True
            else:  #amount is negative, zero, or more than the account balance
                return False
        except TypeError:
            return False
    
    def get_balance(self) -> float:
        '''
        This function returns the account balance
        :return: account balance (__account_balance)
        '''
        return self.__account_balance
    
    def get_name(self) -> str:
        '''
        This function returns the account name
        :return: account name (__account_name)
        
        '''
        return self.__account_name
