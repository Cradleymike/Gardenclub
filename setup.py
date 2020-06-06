
class Classes :
    """Set up the classes to allocate the prize money and category"""
    def __init__(self, number, description, first_prize, second_prize, third_prize,fourth_prize,fifth_prize,sixth_prize , section ):
        self.number = number
        self.description = description
        self.first_prize = first_prize
        self.second_prize = second_prize
        self.third_prize = third_prize
        self.fourth_prize = fourth_prize
        self.fifth_prize = fifth_prize
        self.sixth_prize = sixth_prize
        self.section = section

    def update_desc(self):
        print(f"Current description is :{self.description}.")
        new_description = input ("what is the new description?:")
        self.description = new_description

    def update_prize(self):
        print(f"Current prize money \n first:{self.first_prize}\n second:{self.second_prize}")
        self.first_prize = float(input("enter new first prize:"))
        self.second_prize = float(input("Enter new second prize"))


#testing of the class
c1 = Classes(1,"large onion",30,20,10,8,5,3,"Vegetable")

print(c1.description)
c1.update_desc()
print(c1.description)

print (c1.first_prize)
print (c1.second_prize)
c1.update_prize()
print (c1.first_prize)
print (c1.second_prize)
