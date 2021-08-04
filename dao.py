
from abc import ABC,abstractmethod

class BankDao(ABC):

    @abstractmethod
    def get_all_active_customers(self):
        pass

    @abstractmethod
    def get_active_customer(self):
        pass

    @abstractmethod
    def bank_capital(self):
        pass

    @abstractmethod
    def withdrow_amount(self,account,amount):
        pass

    @abstractmethod
    def deposit_amount(self,account,amount):
        pass

    @abstractmethod
    def add_customer(self):
        pass

    @abstractmethod
    def update_customer(self):
        pass

    @abstractmethod
    def get_active_addresses(self):
        pass