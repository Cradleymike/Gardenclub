import json
from tkinter import *
from tkinter import ttk
from exhibtdb import Database

db = Database('exhibitor.db')

classes = []
dayresult = []

def main ():
    global classes
    global dayresult
    classes = get_data()
    for clss in classes:
        print (clss)
    populate_list()
    dayresult = get_results()
    app3.mainloop()

def get_results():
    try:
        with open('dayresultfile.json') as f1:
            dayresult = json.load(f1)
    except:
        dayresult = []
    return dayresult


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
    try:
        item = {"Id":int(number_text.get()),
        "first":int(first_text.get()),
        "second":int(second_text.get()),
        "third":int(third_text.get()),
        "fourth":int(fourth_text.get()),
        "fifth":int(fifth_text.get()),
        "sixth":int(sixth_text.get())}
        print(item)
        dayresult.append(item)
        print (dayresult)
        save_file()
    #need to write all the data to the class then output to the file, then re-populate the list
    except:
        print("error storing result")

def save_file():
    dayresultfile = open("dayresultfile.json", "w")
    json.dump(dayresult, dayresultfile)
    dayresultfile.close()

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

def fourth_details():
    global fourth_text
    global fourth_item
    fourth_text.set(selected_item[0])

def fifth_details():
    global fifth_text
    global fifth_item
    fifth_text.set(selected_item[0])

def sixth_details():
    global sixth_text
    global sixth_item
    sixth_text.set(selected_item[0])

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
first_text = StringVar(value = "0")
first_label = Label(app3, text='First',  pady = 5)
first_label.grid(row=2, column=0, sticky = W)
first_entry = Entry(app3, width = 10, textvariable= first_text)
first_entry.grid(row = 2,column=1, sticky = W)

#second
second_text = StringVar(value = "0")
second_label = Label(app3, text='Second',  pady = 5)
second_label.grid(row=3, column=0, sticky = W)
second_entry = Entry(app3, width = 10, textvariable= second_text)
second_entry.grid(row = 3,column=1, sticky = W)

#third
third_text = StringVar(value = "0")
third_label = Label(app3, text='Third',  pady = 5)
third_label.grid(row=4, column=0, sticky = W)
third_entry = Entry(app3, width = 10, textvariable= third_text)
third_entry.grid(row = 4,column=1, sticky = W)

#Fourth
fourth_text = StringVar(value = "0")
fourth_label = Label(app3, text='Fourth',  pady = 5)
fourth_label.grid(row=5, column=0, sticky = W)
fourth_entry = Entry(app3, width = 10, textvariable= fourth_text)
fourth_entry.grid(row = 5,column=1, sticky = W)

#Fifth
fifth_text = StringVar(value = "0")
fifth_label = Label(app3, text='Fifth',  pady = 5)
fifth_label.grid(row=6, column=0, sticky = W)
fifth_entry = Entry(app3, width = 10, textvariable= fifth_text)
fifth_entry.grid(row = 6,column=1, sticky = W)

#Sixth
sixth_text = StringVar(value = "0")
sixth_label = Label(app3, text='Sixth',  pady = 5)
sixth_label.grid(row=7, column=0, sticky = W)
sixth_entry = Entry(app3, width = 10, textvariable= sixth_text)
sixth_entry.grid(row = 7,column=1, sticky = W)


#Listbox for the existing Exhibitors
exhibitor_list = Listbox(app3, height=5, width = 50, border =0)
exhibitor_list.grid(row=10, column = 0, columnspan = 3, rowspan = 6, pady=20, padx = 20)

#listbox scrollbar
scrollbar = Scrollbar(app3)
scrollbar.grid(row=10, column=3, rowspan = 6)

#setscrollbar to listbox
exhibitor_list.configure(yscrollcommand = scrollbar.set)
scrollbar.configure(command = exhibitor_list.yview)

#Bind select item
exhibitor_list.bind('<<ListboxSelect>>',select_item)


#Buttons
first_btn = Button(app3, text='First', width = 12, command = first_details)
first_btn.grid(row = 2, column = 2)

second_btn = Button(app3, text='Second', width = 12, command = second_details)
second_btn.grid(row = 3, column = 2)

third_btn = Button(app3, text='Third', width = 12, command = third_details)
third_btn.grid(row = 4, column = 2)

fourth_btn = Button(app3, text='Fourth', width = 12, command = fourth_details)
fourth_btn.grid(row = 5, column = 2)

fifth_btn = Button(app3, text='Fifth', width = 12, command = fifth_details)
fifth_btn.grid(row = 6, column = 2)

sixth_btn = Button(app3, text='Sixth', width = 12, command = sixth_details)
sixth_btn.grid(row = 7, column = 2)

add_btn = Button(app3, text='Add', width = 12, command = add_details)
add_btn.grid(row = 18, column = 0, pady = 20)


main()