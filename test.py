#file to test the use of lists

class Test1:


    def __init__(self, number,name, prizes):
        self.number = number
        self.test_name = name
        self.prizes = prizes
        self.voucher = []

    def assign_voucher(self):
        for prize in self.prizes:
            if prize == "v":       #need to convert to lowercase
                amt=float(input("Enter voucher amount"))
            else:
                amt = 0.0
            self.voucher.append(amt)




    

nme = "Large Onion"
num = 1
prizes = ["v","v","v","M","M","M"]


c1 = Test1(num,nme,prizes)
print(c1.prizes)
c1.assign_voucher()
print(c1.voucher)
