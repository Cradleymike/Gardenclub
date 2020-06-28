import json
from tkinter import *

# Experiment with using Dictionary to store the data and transfer to JSON to output to the file.
classes = { 1: {"description":"Large Onion", "voucher":[30,20,10,0,0,0],"money":[0,0,0,8,5,3],"section":"Vegetable" },
2 : {"description":"Longest Runner Bean","voucher":[0,0,0,0,0,0],"money":[1.00,0.75,0.50,0,0,0], "section":"Vegetable"}
}


app2 = Tk()
app2.title('Colley Gate Garden Club - Class Setup ')
app2.geometry('400x700')

#Title
title_label = Label(app2, text='Classes Setup', font = 'Bold', pady = 5)
title_label.grid(row=0, column=1)

#Number
number_text = StringVar()
number_label = Label(app2, text='Number',  pady = 5)
number_label.grid(row=1, column=0, sticky = W)
number_entry = Entry(app2, width = 10, textvariable= number_text)
number_entry.grid(row = 1,column=1, sticky = W)

#Description
description_text = StringVar()
description_label = Label(app2, text='Description',  pady = 5)
description_label.grid(row=2, column=0, sticky = W)
description_entry = Entry(app2, width = 50, textvariable= description_text)
description_entry.grid(row = 2,column=1, columnspan = 2)

#Winnings
Winning_label = Label(app2, text='Winnings', font = 'Bold', pady = 5)
Winning_label.grid(row=3, column=1, columnspan = 2)

#Moneylabel
Money_label = Label(app2, text='Money', font = 'Bold', pady = 5)
Money_label.grid(row=4, column=1)

#Voucher_label
Voucher_label = Label(app2, text='Voucher', font = 'Bold', pady = 5)
Voucher_label.grid(row=4, column=2)

#first_label
first_label = Label(app2, text='First', pady = 5)
first_label.grid(row=5, column=0)
firstmoney_text = StringVar()
firstmoney_entry = Entry(app2, width = 10,textvariable = firstmoney_text)
firstmoney_entry.grid(row=5,column=1)
firstvoucher_text = StringVar()
firstvoucher_entry = Entry(app2, width = 10,textvariable = firstvoucher_text)
firstvoucher_entry.grid(row=5,column = 2)

#Second_label
second_label = Label(app2, text='Second', pady = 5)
second_label.grid(row=6, column=0)
secondmoney_text = StringVar()
secondmoney_entry = Entry(app2, width = 10,textvariable = secondmoney_text)
secondmoney_entry.grid(row=6,column=1)
secondvoucher_text = StringVar()
secondvoucher_entry = Entry(app2, width = 10,textvariable = secondvoucher_text)
secondvoucher_entry.grid(row=6,column = 2)

#Third_label
third_label = Label(app2, text='Third', pady = 5)
third_label.grid(row=7, column=0)
thirdmoney_text = StringVar()
thirdmoney_entry = Entry(app2, width = 10,textvariable = thirdmoney_text)
thirdmoney_entry.grid(row=7,column=1)
thirdvoucher_text = StringVar()
thirdvoucher_entry = Entry(app2, width = 10,textvariable = thirdvoucher_text)
thirdvoucher_entry.grid(row=7,column = 2)

#Fourth_label
fourth_label = Label(app2, text='Fourth', pady = 5)
fourth_label.grid(row=8, column=0)
fourthmoney_text = StringVar()
fourthmoney_entry = Entry(app2, width = 10,textvariable = fourthmoney_text)
fourthmoney_entry.grid(row=8,column=1)
fourthvoucher_text = StringVar()
fourthvoucher_entry = Entry(app2, width = 10,textvariable = fourthvoucher_text)
fourthvoucher_entry.grid(row=8,column = 2)

#Fifth_label
fifth_label = Label(app2, text='Fifth', pady = 5)
fifth_label.grid(row=9, column=0)
fifthmoney_text = StringVar()
fifthmoney_entry = Entry(app2, width = 10,textvariable = fifthmoney_text)
fifthmoney_entry.grid(row=9,column=1)
fifthvoucher_text = StringVar()
fifthvoucher_entry = Entry(app2, width = 10,textvariable = fifthvoucher_text)
fifthvoucher_entry.grid(row=9,column = 2)

#Sixth_label
sixth_label = Label(app2, text='Sixth', pady = 5)
sixth_label.grid(row=10, column=0)
sixthmoney_text = StringVar()
sixthmoney_entry = Entry(app2, width = 10,textvariable = sixthmoney_text)
sixthmoney_entry.grid(row=10,column=1)
sixthvoucher_text = StringVar()
sixthvoucher_entry = Entry(app2, width = 10,textvariable = sixthvoucher_text)
sixthvoucher_entry.grid(row=10,column = 2)






print(classes)


print(classes[1]["description"])
print(classes[1]["voucher"][0])


print(classes)

classesfile = open("classfile.txt", "w")
json.dump(classes, classesfile)
classesfile.close()


app2.mainloop()





