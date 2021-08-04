from orm.bank_prob_stmt.models import app
from flask import Flask,render_template,request
from orm.bank_prob_stmt.serviceimpl import BankServiceImpl
from orm.bank_prob_stmt.models import Customer
service = BankServiceImpl()
genderTypes = {"M":"Male","F":"Female"}


class CustVal:
    def __init__(self, cid, cnm, cag, ceml, gender, adr):
        self.cid = cid
        self.cnm = cnm
        self.cag = cag
        self.gender = gender
        self.ceml = ceml
        self.adr = int(adr)


def dummycust():
    return CustVal(cid=0, cnm='', cag=0, ceml='', gender='', adr='0')


@app.route("/customer/welcome/",methods=["GET"])
def welcome_customer():
    return render_template('customer.html',custs = Customer.query.filter(Customer.active=='Y').all(),
                           genders = genderTypes,cust=dummycust(),
                           addresses = service.get_all_active_address())

@app.route("/customer/persist/",methods=["POST"])
def save_customer_info():
    print(request.form)
    msg = service.add_customer(request.form)
    if "Successfully" not in msg:
        cust = CustVal(**request.form)
    else:
        cust=dummycust()
    return render_template('customer.html',cust=cust,
                           genders=genderTypes,
                           msg=msg,custs = Customer.query.filter(Customer.active=='Y').all(),
                           addresses = service.get_all_active_address())

#([('cid', '12812'), ('cnm', 'asda'), ('cag', '28'),
# ('ceml', 'ada@fajj.com'), ('gender', 'M'), ('adr', '1114')])

if __name__ == '__main__':
    app.run(debug=True)