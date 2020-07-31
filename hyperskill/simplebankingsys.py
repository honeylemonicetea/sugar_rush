import random
import sqlite3

conn = sqlite3.connect('card.s3db')
cur = conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS card (id INTEGER, number TEXT, pin TEXT,  balance INTEGER DEFAULT 0);')
conn.commit()


class BankingSystem:
    def __init__(self):
        self.balance = 0
        self.cardn = ""
        self.pin = ""

    def action_choice(self, action):
        self.action = action
        if self.action == '1':
            self.create_acc()
        elif self.action == '2':
            self.log_in()
        elif self.action == '0':
            return self.exit()

    def exit(self):
        print("Bye")
        return 0

    def create_acc(self):
        k = pow(10, 8)
        p = pow(10, 9) - 1
        acc = random.randrange(k, p)
        test_numbers = []
        test_sum = 0
        checksum = 0
        l = ['400000', str(acc)]
        test_acc = "".join(l)
        for i in range(1, len(test_acc) + 1):
            if int(i) % 2 == 1:
                i = int(test_acc[i - 1]) * 2
                test_numbers.append(i)
            else:
                test_numbers.append(int(test_acc[i - 1]))
        for i in range(len(test_numbers)):
            if int(test_numbers[i]) > 9:
                test_numbers[i] = int(test_numbers[i]) - 9
        for i in test_numbers:
            test_sum += i
        for y in range(10):
            if (test_sum + y) % 10 == 0:
                checksum = y
        nl = ['400000', str(acc), str(checksum)]
        num = "".join(nl)
        self.cardn = num
        ps = []
        for i in range(4):
            i = random.randrange(0, 9)
            ps.append(str(i))
        pin = "".join(ps)
        self.pin = pin
        conn = sqlite3.connect('card.s3db')
        cur = conn.cursor()
        cur.execute('INSERT INTO card (number, pin) values (?, ?) ', (self.cardn, self.pin))
        conn.commit()
        print("\nYour card has been created")
        print(f"Your card number:\n{self.cardn}")
        print(f"Your card PIN:\n{self.pin}")
        print("""\n1. Create an account
2. Log into account
0. Exit""")
        self.action_choice(input())

    def log_in(self):
        print("Enter your card number:")
        self.card = input()
        print("Enter your PIN:")
        self.pinn = input()
        conn = sqlite3.connect('card.s3db')
        cur = conn.cursor()
        cur.execute('SELECT number, pin, balance FROM card WHERE number = ?', (self.card,))
        jd = cur.fetchone()
        if jd == None:
            print("\nWrong card number or PIN!")
            print("""\n1. Create an account
2. Log into account
0. Exit""")
            self.action_choice(input())
        elif jd[1] == self.pinn:
            print("\nYou have successfully logged in!")
            self.private()
        elif jd[1] != self.pinn:
            print("\nWrong card number or PIN!")
            print("""\n1. Create an account
2. Log into account
0. Exit""")
            self.action_choice(input())
    def private(self):
        print("""\n1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit
        """)
        self.option = input()
        if self.option == '1':  # balance
            conn = sqlite3.connect('card.s3db')
            cur = conn.cursor()
            cur.execute('SELECT number, balance FROM card WHERE number = ?', (self.card,))
            jd = cur.fetchone()
            print(jd[1])
            self.private()
        elif self.option == '5':  # log out
            print("\nYou have successfully logged out!\n")
            print("""1. Create an account
2. Log into account
0. Exit""")
            self.action_choice(input())
        elif self.option == '0':
            self.exit()
        elif self.option == '2':  # add income
            print("Enter income:")
            self.income = int(input())
            conn = sqlite3.connect('card.s3db')
            cur = conn.cursor()
            cur.execute('UPDATE card SET balance = balance + ? WHERE number = ?', (self.income, self.card))
            conn.commit()
            print("Income was added!")
            self.private()
        elif self.option == '3':  # do transfer
            print("Transfer")
            print("Enter card number:")
            self.reciever_card = input()
            conn = sqlite3.connect('card.s3db')
            cur = conn.cursor()
            cur.execute('SELECT number, balance FROM card WHERE number = ?', (self.card,))
            bal = cur.fetchone() #senders number and balance
            conn = sqlite3.connect('card.s3db')
            cur = conn.cursor()
            cur.execute('SELECT number, balance FROM card WHERE number = ?', (self.reciever_card,))
            rec = cur.fetchone() #recepients num and balance
            #check Luhn's algorithm
            test_numbers = []
            test_sum = 0
            checksum = int(self.reciever_card) % 10
            rest = int(self.reciever_card) // 10
            rest = str(rest)
            for i in range(1, len(rest) + 1):
                if int(i) % 2 == 1:
                    i = int(rest[i - 1]) * 2
                    test_numbers.append(i)
                else:
                    test_numbers.append(int(rest[i - 1]))
            for i in range(len(test_numbers)):
                if int(test_numbers[i]) > 9:
                    test_numbers[i] = int(test_numbers[i]) - 9
            for i in test_numbers:
                test_sum += i
            #checking cardn and balance
            if self.card == self.reciever_card:
                print("You can't transfer money to the same account!")
                self.private()
            elif (test_sum + checksum) % 10 != 0:
                print("Probably you made mistake in the card number. Please try again!")
                self.private()
            elif rec == None:
                print("Such a card does not exist")
                self.private()
            else:
                print("Enter how much money you want to transfer:")
                self.money = int(input())
                if int(bal[1]) < self.money:
                    print("Not enough money!")
                    self.private()
                else:
                    conn = sqlite3.connect('card.s3db')
                    cur = conn.cursor()
                    cur.execute('UPDATE card SET balance = balance + ? WHERE number = ?', (self.money, self.reciever_card))
                    conn.commit()
                    conn = sqlite3.connect('card.s3db')
                    cur = conn.cursor()
                    cur.execute('UPDATE card SET balance = balance - ? WHERE number = ?',(self.money, self.card))
                    conn.commit()
                    print("Success!")
                    self.private()
        elif self.option == '4':  # close account
            conn = sqlite3.connect('card.s3db')
            cur = conn.cursor()
            cur.execute('DELETE FROM card WHERE number = ?', (self.card,))
            conn.commit()
            print("The account has been closed!")
            print("""1. Create an account
2. Log into account
0. Exit""")
            self.action_choice(input())
a = BankingSystem()
print("""1. Create an account
2. Log into account
0. Exit""")
a.action_choice(input())
