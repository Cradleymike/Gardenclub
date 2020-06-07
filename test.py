#file to test the use of lists

class Test1:


    def __init__(self, number,name, prizes):
        self.number = number
        self.test_name = name
        self.prizes = prizes
        self.voucher = []
        self.money = []

    def assign_voucher(self):
        i = 1
        for prize in self.prizes:
            if prize.upper() == "V":       #need to convert to uppercase
                amt=float(input(f"Enter voucher amountfor position {i}:"))
            else:
                amt = 0.0
            self.voucher.append(amt)
            i +=1

    def assign_money(self):
        i = 1
        for prize in self.prizes:
            if prize.upper() == "M":    #convert to uppercase
                amt = float(input(f"Enter the money amount for position {i}:"))
            else:
                amt = 0.0
            self.money.append(amt)
            i +=1

    def write_file(self):
        f = open("Showclasses.txt","a")
        f.write(c1.test_name)
        f.close()




    

nme = "Large Onion"
num = 1
prizes = ["v","v","v","M","M","M"]


c1 = Test1(num,nme,prizes)
print(c1.prizes)
c1.assign_voucher()
print(c1.voucher)
c1.assign_money()
print(c1.money)
c1.write_file()

