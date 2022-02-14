#python banking program which saves its data to an sqllite database
import os, sys, sqlite3, random


def menu():
    while True:
        print('Welcome to YES bank')
        print("1.press 1 to make account\n2.press 2 to deposit money \n3.press 3 to transfer money\n4.press 4 to withdraw money\n5.enter 5 to exit ")
        inp = input()
        if inp == '1':
            make_account()
        if inp == '2':
            number = int(input('enter your bank account No '))
            amount = int(input('enter how much you want to deposit '))
            deposit(number,amount)
        if inp == '3':
            x = int(input('enter your bank account No '))
            y = int(input('enter your bank account No you want to transfer to '))
            amount = int(input('enter how much you want to transfer '))
            transfer(x,y,amount)
        if inp == '4':
            number = int(input('enter your bank account No '))
            amount = int(input('enter how much you want to withdraw '))
            withdraw(number,amount)
        if inp == '5':
            sys.exit()
    


def make_account():
    name = input('name: ')
    balance = input('balance: ')
    number = random.randint(700,800)
    c.execute('''
    insert into users(id, name, balance) 
    values(?,?,?)''',(number,name,balance))
    db.commit()

def deposit(number, amount):
    c.execute('''
    select balance from users where id = ?
    ''',(number,))
    balance = c.fetchone()[0]
    balance = balance + amount   
    c.execute('''UPDATE users SET balance = ? WHERE id = ? ''', (balance, number))
    db.commit()

def withdraw(number, amount):
    c.execute('''
    select balance from users where id = ?
    ''',(number,))
    balance = c.fetchone()[0]
    balance = balance - amount   
    c.execute('''UPDATE users SET balance = ? WHERE id = ? ''', (balance, number))
    db.commit()
    

def transfer(x,y,amount):
    c.execute('''
    select balance from users where id = ?
    ''',(y,))
    balance = c.fetchone()[0]
    balance = balance + amount 
    c.execute('''UPDATE users SET balance = ? WHERE id = ? ''', (balance, y))
    db.commit()

    c.execute('''
    select balance from users where id = ?
    ''',(x,))
    balance = c.fetchone()[0]
    balance = balance - amount 
    c.execute('''UPDATE users SET balance = ? WHERE id = ? ''', (balance, x))
    db.commit()




db = sqlite3.connect('bank.db')
c = db.cursor()
c.execute('''
create table if not exists users(id integer primary key,
name text,
balance integer)
'''
)
db.commit()

menu()
