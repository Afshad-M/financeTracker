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