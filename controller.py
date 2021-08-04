from flask import Flask,render_template,request
from orm.bank_prob_stmt.models import app
from orm.bank_prob_stmt.serviceimpl import BankServiceImpl

service = BankServiceImpl()

@app.route("/cust/<int:cid>/account/<int:aid>",methods=["GET"])
def get_account_balance(cid,aid):
    dbaccount = service.get_active_account(cid,aid)
    if dbaccount:
        print(dbaccount)
        #return render_template('account.html',amount=dbaccount)



@app.route("/cust/<int:cid>",methods=["GET"])
def get_customer_balance(cid):
    dbaccount = service.get_all_active_accounts(cid)
    if dbaccount:
        print(dbaccount)


if __name__ == '__main__':
    #app.run(debug=True)
    #print(get_account_balance(111,2))
    pass
