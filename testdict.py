# test for the use of dictionary use for the classes in the show

class Test:

    def __init__(self, number,name, section):
        self.number = number
        self.test_name = name
        self.first = {'voucher' :0, 'money':0}
        self.second = {'voucher' :0, 'money':0}
        self.third = {'voucher' :0, 'money':0}
        self.fourth = {'voucher' :0, 'money':0}
        self.fifth = {'voucher' :0, 'money':0}
        self.sixth = {'voucher' :0, 'money':0}
        self.section = section

    


c1 = Test(1, "Heavy Onion", "vegetable")

print (c1.first)
print (c1.first['voucher'])
print (c1.number)
print (c1.test_name)
print (c1.section)

