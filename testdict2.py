import json
from tkinter import *
from tkinter import ttk

#Experiment with using Dictionary to store the data and transfer to JSON to output to the file.
#classes = {"id":1,"description":"Large Onion", "voucher":[30,20,10,0,0,0],"money":[0,0,0,8,5,3],"section":"Vegetable" },{"id":2,"description":"Longest Runner Bean","voucher":[0,0,0,0,0,0],"money":[1.00,0.75,0.50,0,0,0], "section":"Vegetable"}



def populate_list():
    """Need to read the JSON file and populate the classes dictionary which can then be used in the list?"""
    pass

def add_item():
    print(number_text.get())
    item = {"Id":int(number_text.get()),
    "description":description_text.get(),
    "voucher":[int(firstvoucher_text.get()),
               int(secondvoucher_text.get()),
               int(thirdvoucher_text.get()),
               int(fourthvoucher_text.get()),
               int(fifthvoucher_text.get()),
               int(sixthvoucher_text.get())],
    "money":[int(firstmoney_text.get()),
             int(secondmoney_text.get()),
             int(thirdmoney_text.get()),
             int(fourthmoney_text.get()),
             int(fifthmoney_text.get()),
             int(sixthmoney_text.get())],
    "section":section_text.get(),
    "points":checkpoints.get()}
    print(item)
    classes.append(item)
    print (classes)
    #need to write all the data to the class then output to the file, then re-populate the list

def edit_item():
    pass

def remove_item():
    pass

def clear_item():
    pass


app2 = Tk()
app2.title('Colley Gate Garden Club - Class Setup ')
app2.geometry('500x700')

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
firstmoney_text = StringVar(value="0")
firstmoney_entry = Entry(app2, width = 10,textvariable = firstmoney_text)
firstmoney_entry.grid(row=5,column=1)
firstvoucher_text = StringVar(value="0")
firstvoucher_entry = Entry(app2, width = 10,textvariable = firstvoucher_text)
firstvoucher_entry.grid(row=5,column = 2)

#Second_label
second_label = Label(app2, text='Second', pady = 5)
second_label.grid(row=6, column=0)
secondmoney_text = StringVar(value="0")
secondmoney_entry = Entry(app2, width = 10,textvariable = secondmoney_text)
secondmoney_entry.grid(row=6,column=1)
secondvoucher_text = StringVar(value="0")
secondvoucher_entry = Entry(app2, width = 10,textvariable = secondvoucher_text)
secondvoucher_entry.grid(row=6,column = 2)

#Third_label
third_label = Label(app2, text='Third', pady = 5)
third_label.grid(row=7, column=0)
thirdmoney_text = StringVar(value="0")
thirdmoney_entry = Entry(app2, width = 10,textvariable = thirdmoney_text)
thirdmoney_entry.grid(row=7,column=1)
thirdvoucher_text = StringVar(value="0")
thirdvoucher_entry = Entry(app2, width = 10,textvariable = thirdvoucher_text)
thirdvoucher_entry.grid(row=7,column = 2)

#Fourth_label
fourth_label = Label(app2, text='Fourth', pady = 5)
fourth_label.grid(row=8, column=0)
fourthmoney_text = StringVar(value="0")
fourthmoney_entry = Entry(app2, width = 10,textvariable = fourthmoney_text)
fourthmoney_entry.grid(row=8,column=1)
fourthvoucher_text = StringVar(value="0")
fourthvoucher_entry = Entry(app2, width = 10,textvariable = fourthvoucher_text)
fourthvoucher_entry.grid(row=8,column = 2)

#Fifth_label
fifth_label = Label(app2, text='Fifth', pady = 5)
fifth_label.grid(row=9, column=0)
fifthmoney_text = StringVar(value="0")
fifthmoney_entry = Entry(app2, width = 10,textvariable = fifthmoney_text)
fifthmoney_entry.grid(row=9,column=1)
fifthvoucher_text = StringVar(value="0")
fifthvoucher_entry = Entry(app2, width = 10,textvariable = fifthvoucher_text)
fifthvoucher_entry.grid(row=9,column = 2)

#Sixth_label
sixth_label = Label(app2, text='Sixth', pady = 5)
sixth_label.grid(row=10, column=0)
sixthmoney_text = StringVar(value="0")
sixthmoney_entry = Entry(app2, width = 10,textvariable = sixthmoney_text)
sixthmoney_entry.grid(row=10,column=1)
sixthvoucher_text = StringVar(value="0")
sixthvoucher_entry = Entry(app2, width = 10,textvariable = sixthvoucher_text)
sixthvoucher_entry.grid(row=10,column = 2)

#section options

section_text = StringVar()
section_label = Label(app2, text='Section', pady = 5)
section_label.grid(row=11,column =0)
section_combo = ttk.Combobox(app2,values=['Vegetables','Dahlias','Chrysanthemums','Domestic','Wine'],textvariable = section_text)
section_combo.grid(row=11,column=1)


#points checkbox
checkpoints = IntVar()
checkpoint_entry = Checkbutton(app2, text = "Include Points", variable= checkpoints, onvalue=1, offvalue = 0)
checkpoint_entry.grid(row=13,column=1)


#Buttons - Add, Edit, Remove, Clear

add_btn = Button(app2, text='Add', width = 12, command = add_item)
add_btn.grid(row = 14, column = 0, pady = 20)

edit_btn = Button(app2, text='Edit', width = 12, command = edit_item)
edit_btn.grid(row = 14, column = 1, pady = 20)

remove_btn = Button(app2, text='Remove', width = 12, command = remove_item)
remove_btn.grid(row = 14, column = 2, pady = 20)

clear_btn = Button(app2, text='Clear', width = 12, command = clear_item)
clear_btn.grid(row = 14, column = 3, pady = 20)


#open file and read json data
with open('classfile.json') as f:
    classes = json.load(f)
print(classes)

for clss in classes:
    print (clss)
    print (clss["id"])
 #print(classes[0])
#print(classes["voucher"][0])
#

print(classes)

classesfile = open("classfile.json", "w")
json.dump(classes, classesfile)
classesfile.close()


app2.mainloop()





