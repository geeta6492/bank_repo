from flask import Flask #web
from flask_sqlalchemy import SQLAlchemy #ORM
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/dbemp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False # dont show case warnings on console
db = SQLAlchemy(app) #integration Database with flask - thru sqlachemy-- pymysql or mysqldbclient

'''
    Bank  - Customer -- MM
    Customer -- Account --1M
    Bank -- Address -- 11
    Customer - Address - M-1
'''

bank_cust = db.Table(
    "BankCustomers",
    db.Column("cid", db.Integer(), db.ForeignKey("customer.id")),
    db.Column("bid", db.Integer(), db.ForeignKey("bank.id"))
)

class Bank(db.Model):
    id = db.Column("id", db.Integer(), primary_key=True)
    name = db.Column("name", db.String(100))
    active = db.Column("active", db.String(10), default='Y')
    aid = db.Column("adr_id", db.Integer(), db.ForeignKey("address.id"), unique=True)
    customers = db.relationship("Customer",secondary=bank_cust,backref="banks",lazy=True)

#Bank(id=11223,name='SBI',aid=1111,customers=[c1,c2,c3])

class Account(db.Model):
    id = db.Column("id", db.Integer(), primary_key=True)
    type = db.Column("name", db.String(100))
    balance = db.Column("balance", db.Float())
    active = db.Column("active", db.String(10), default='Y')
    custid = db.Column("cust_id", db.Integer(), db.ForeignKey("customer.id"), unique=False)

#Account(id=1111,type='Saving',balance=2883.34)
class Customer(db.Model):
    id = db.Column("id", db.Integer(), primary_key=True)
    name = db.Column("name", db.String(100))
    gender = db.Column("gender", db.String(100))
    age = db.Column("age", db.Integer())
    email = db.Column("email", db.String(100), unique=True)
    active = db.Column("active", db.String(10), default='Y')
    aid = db.Column("adr_id", db.Integer(), db.ForeignKey("address.id"),unique=True)
    accounts = db.relationship("Account",uselist=True,backref="customer",lazy=True)

#c1 = Customer(id=11,name='AAAA',gender='M',age=22,email='aa',aid=1111)


    #accounts = db.relationship("Account",uselist=True,secondary=custaccounts,
    #                             backref="customer",lazy=True)

#Customer(id=1,name='AAA',gender='M',age=23,email='abc@gmail.com')

class Address(db.Model):
    id = db.Column("id", db.Integer(), primary_key=True)
    city = db.Column("city", db.String(100))
    state = db.Column("state", db.String(100))
    pincode = db.Column("pincode", db.Integer())
    active = db.Column("active", db.String(10), default='Y')
    cust = db.relationship("Customer",backref="address",lazy=True)
#Address(id=111,city='Pune',state='MH')


if __name__ == '__main__':
    db.create_all()