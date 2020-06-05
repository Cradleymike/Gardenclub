
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

    def get_number(self):
        return self.number

    def get_description(self):
        return self.description

    def get_first_prize(self):
        return self.first_prize

    def get_second_prize(self):
        return self.second_prize

    def get_third_prize(self):
        return self.third_prize

    def get_fourth_prize(self):
        return self.fourth_prize

    def get_fifth_prize(self):
        return self.fifth_prize

    def get_sixth_prize(self):
        return self.sixth_prize

    def get_section(self):
        return self.section

c1 = Classes(1,"large onion",30,20,10,8,5,3,"Vegetable")
print(c1.get_description())
