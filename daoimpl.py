from orm.bank_prob_stmt.models import *
from orm.bank_prob_stmt.dao import BankDao

MIN_BALANCE = 10000

class BankCrudOp(BankDao):

    def get_all_active_customers(self):
        return Customer.query.filter(Customer.active=='Y').all()

    def get_active_customer(self,cid):
        return Customer.query.filter(Customer.active=='Y',Customer.id==cid).first()

    def get_all_active_accounts(self,cid):
        customer = self.get_active_customer(cid)
        if customer:
            accountList =[]
            for acc in customer.accounts:
                if acc.active=='Y':
                    accountList.append(acc)
            return accountList
        else:
            print('No customer present..')

    def get_active_account(self,cid,aid):
        customer = self.get_active_customer(cid)
        if customer:
            account =  Account.query.filter(
            Account.active=='Y',
            Account.id==aid
            ).first()
            if account:
                if account.custid==cid:
                    return account
                else:
                    print("No account with Customer..!")
            else:
                print("No Account with Given Id..!")
        else:
            print("Customer Not Present")

    def bank_capital(self):
        accounts = Account.query.filter(Account.custid!=None).all()
        sum = 0
        for acc in accounts:
            sum+=acc.balance
        return sum

    def withdrow_amount(self, dbacc, amount):
        try:
            existingBal = dbacc.balance
            dbacc.balance=existingBal-amount
            db.session.commit()
            return True
        except:
            return False

    def deposit_amount(self, dbacc, amount):
        try:
            existingBal = dbacc.balance
            dbacc.balance = existingBal + amount
            db.session.commit()
            return True
        except:
            return False

    def duplicateAddress(self,adrid):
        if Customer.query.filter(Customer.aid==adrid).first():
            return True
        else:
            return False

    def findDuplicateEmail(self,email):
        if Customer.query.filter(Customer.email==email).first():
            return True
        else:
            return False


    def add_customer(self,custModel):
        db.session.add(custModel)
        db.session.commit()
        return "Customer Saved Successfully...!"

    def update_customer(self):
        pass

    def get_active_addresses(self):
        return Address.query.filter(Address.active=='Y').all()