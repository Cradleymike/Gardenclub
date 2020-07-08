import json
from tkinter import *
from tkinter import ttk
from exhibtdb import Database

db = Database('exhibitor.db')

classes = []

def main ():
    global classes
    classes = get_data()
    for clss in classes:
        print (clss)
    populate_list()
    app3.mainloop()



def get_data():
    #open file and read json data
    with open('classfile.json') as f:
        classes = json.load(f)
    return classes

def populate_list():
    exhibitor_list.delete(0,END)
    for row in db.fetch():
        exhibitor_list.insert(END, row)

def add_details():
    pass

def first_details():
    global first_text
    global selected_item
    first_text.set(selected_item[0])

def second_details():
    global second_text
    global selected_item
    second_text.set(selected_item[0])

def third_details():
    global third_text
    global third_item
    third_text.set(selected_item[0])

def select_item(event):
    try:
        global selected_item
        index = exhibitor_list.curselection()[0]
        selected_item = exhibitor_list.get(index)
        print (selected_item[0])
    except:
        print ("Error")

app3 = Tk()
app3.title('Colley Gate Garden Club - Day Results ')
app3.geometry('500x700')
#Title
title_label = Label(app3, text='Log Class Results', font = 'Bold', pady = 5)
title_label.grid(row=0, column=1)

#Number
number_text = StringVar()
number_label = Label(app3, text='Number',  pady = 5)
number_label.grid(row=1, column=0, sticky = W)
number_entry = Entry(app3, width = 10, textvariable= number_text)
number_entry.grid(row = 1,column=1, sticky = W)

#first
first_text = StringVar()
first_label = Label(app3, text='First',  pady = 5)
first_label.grid(row=2, column=0, sticky = W)
first_entry = Entry(app3, width = 10, textvariable= first_text)
first_entry.grid(row = 2,column=1, sticky = W)

#second
second_text = StringVar()
second_label = Label(app3, text='Second',  pady = 5)
second_label.grid(row=3, column=0, sticky = W)
second_entry = Entry(app3, width = 10, textvariable= second_text)
second_entry.grid(row = 3,column=1, sticky = W)

#third
third_text = StringVar()
third_label = Label(app3, text='Third',  pady = 5)
third_label.grid(row=4, column=0, sticky = W)
third_entry = Entry(app3, width = 10, textvariable= third_text)
third_entry.grid(row = 4,column=1, sticky = W)


#Listbox for the existing Exhibitors
exhibitor_list = Listbox(app3, height=5, width = 50, border =0)
exhibitor_list.grid(row=5, column = 0, columnspan = 3, rowspan = 6, pady=20, padx = 20)

#listbox scrollbar
scrollbar = Scrollbar(app3)
scrollbar.grid(row=5, column=3)

#setscrollbar to listbox
exhibitor_list.configure(yscrollcommand = scrollbar.set)
scrollbar.configure(command = exhibitor_list.yview)

#Bind select item
exhibitor_list.bind('<<ListboxSelect>>',select_item)


#Buttons
first_btn = Button(app3, text='First', width = 12, command = first_details)
first_btn.grid(row = 13, column = 0, pady = 20)

second_btn = Button(app3, text='Second', width = 12, command = second_details)
second_btn.grid(row = 13, column = 1)

third_btn = Button(app3, text='Third', width = 12, command = third_details)
third_btn.grid(row = 13, column = 2)

add_btn = Button(app3, text='Add', width = 12, command = add_details)
add_btn.grid(row = 14, column = 0, pady = 20)


main()