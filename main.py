import random
#coin demo



class Coin:
    def __init__(self):
        self.sideup = "Heads"

    def toss(self):
        num = random.randint(0,2)
        if num == 0:
            self.sideup = 'Heads'
        else:
            self.sideup = 'Tails'

    def get_sideup(self):
        return self.sideup



def main():
    #creating objects for class Coin

    c1 = Coin()
    print(c1.get_sideup())
    c1.toss()
    print(c1.get_sideup())
    c1.toss()
    print(c1.get_sideup())
    


main()

#Transaction class for finance tracker app
'''
Functionality:
- Store transaction details (amount, date, category, description)
- Methods to add, remove, and view transactions
- Calculate total income and expenses
- Edit transaction details
'''

class Transaction:
    def __init__(self):
        print("Welcome to personal finance tracker app")


    def add_transaction(self, amount, date, category, description):
        pass

    def remove_transaction(self, transaction_id):
        pass

# Write code here


class Client:
    pass


def mainFinanceTracker():
    print("Finance Tracker App")
    while True:
        user = input("What function you want to perform? (add/remove/view/total/edit/exit): ")
        if user == "add":
            pass
        elif user == 'remove':
            pass
        elif user == 'view':
            pass
        elif user == 'total':
            pass
        elif user == 'edit':
            pass
        elif user == 'exit':
            print("Exiting the app")
        else:
            print("Invalid input")
            continue


mainFinanceTracker()