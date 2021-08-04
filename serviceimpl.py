from orm.bank_prob_stmt.service import BankService
from orm.bank_prob_stmt.daoimpl import BankCrudOp
from orm.bank_prob_stmt.models import Customer
bankPeristInstance = None
class BankServiceImpl(BankService):

    def __init__(self):
        global bankPeristInstance
        bankPeristInstance = BankCrudOp()

    def get_active_account(self,cid,aid):
        dbaccount = bankPeristInstance.get_active_account(cid,aid)
        if dbaccount:
            return dbaccount
        #print("No account Present..")

    def get_all_active_accounts(self,cid):
        dbaccount = bankPeristInstance.get_all_active_accounts(cid)
        if dbaccount:
            return dbaccount


    def withdraw_amount(self,accno,amount):
        if amount>0:
            dbacc = self.get_active_account(accno) #acc and cust =Y
            if dbacc and dbacc.balance-10000>amount: #acc and min balanc
                if bankPeristInstance.withdraw_amount(dbacc,amount):
                    return "Successful Trasncation"
                else:
                    return "Transcation Failed"
            else:
                print("No account present or insufficient fund")
        else:
            print("invalid amount..!")

    def deposit_amount(self,accno,amount):
        if amount > 0:
            dbacc = self.get_active_account(accno)  # acc and cust =Y
            if dbacc:  # acc and min balanc
                if bankPeristInstance.deposit_amount(dbacc, amount):
                    return "Successful Trasncation"
                else:
                    return "Transcation Failed"
            else:
                print("No account present or insufficient fund")
        else:
            print("invalid amount..!")


    def duplicateAddress(self,adrid):
        return bankPeristInstance.duplicateAddress(adrid)

    def findDuplicateEmail(self,email):
            return bankPeristInstance.findDuplicateEmail(email)
#ImmutableMultiDict([('cid', '101'), ('cnm', 'ABCf'), ('cag', '23'),
    # ('ceml', 'abc@gmail.com'), ('adr', '1112')])
    def add_customer(self,cust):
        if cust:
            if not self.findDuplicateEmail(cust['ceml']):
                if not self.duplicateAddress(cust['adr']):
                    cust = Customer(name=cust["cnm"],
                             gender=cust['gender'],
                             age=cust['cag'],
                             email=cust['ceml'],
                             aid=cust['adr'])
                    return bankPeristInstance.add_customer(cust)
                else:
                    return "Duplicate Address..already given to other person"
            else:
                return "Duplicate Email address..!"
        else:
            return "Invalid Customer..!"


    def update_customer(self, cust):
        pass

    def get_all_active_address(self):
        return bankPeristInstance.get_active_addresses()


