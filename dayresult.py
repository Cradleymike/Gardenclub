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

#Listbox for the existing Exhibitors
exhibitor_list = Listbox(app3, height=8, width = 50, border =0)
exhibitor_list.grid(row=5, column = 0, columnspan = 3, rowspan = 6, pady=20, padx = 20)

#listbox scrollbar
scrollbar = Scrollbar(app3)
scrollbar.grid(row=5, column=3)

#setscrollbar to listbox
exhibitor_list.configure(yscrollcommand = scrollbar.set)
scrollbar.configure(command = exhibitor_list.yview)

#Bind select item
exhibitor_list.bind('<<ListboxSelect>>',select_item)

add_btn = Button(app3, text='Add', width = 12, command = add_details)
add_btn.grid(row = 14, column = 0, pady = 20)


main()