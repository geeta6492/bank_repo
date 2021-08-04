
from abc import ABC,abstractmethod
class BankService(ABC):

    @abstractmethod
    def withdraw_amount(self,bank,amount,accno):
        pass

    @abstractmethod
    def deposit_amount(self,bank,amount, accno):
        pass

    @abstractmethod
    def add_customer(self,cust):
        pass

    @abstractmethod
    def duplicateAddress(self,adrid):
        pass
    @abstractmethod
    def findDuplicateEmail(self,email):
        pass

    @abstractmethod
    def update_customer(self, cust):
        pass

    @abstractmethod
    def get_all_active_address(self):
        pass