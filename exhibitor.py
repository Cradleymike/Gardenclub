from tkinter import *

# Build a management system for the exhibitor details

#create window object
app = Tk()

app.title('Colley Gate Garden Club - Exhibitor ')
app.geometry('700x400')


#Exhibitor details - number
number_text = StringVar()
number_label = Label(app, text='Number', font = 'Bold', pady = 20)
number_label.grid(row=0, column=0, sticky = W)
number_entry = Entry(app, textvariable= number_text)
number_entry.grid(row = 0,column=1)

#Exhibitor details - first name
fname_text = StringVar()
fname_label = Label(app, text='First Name', font = 'Bold', pady = 5)
fname_label.grid(row=1, column=0, sticky = W)
fname_entry = Entry(app, textvariable= fname_text)
fname_entry.grid(row = 1,column=1)

#Exhibitor details - last name
lname_text = StringVar()
lname_label = Label(app, text='Last Name', font = 'Bold', pady = 5)
lname_label.grid(row=1, column=3, sticky = W)
lname_entry = Entry(app, textvariable= lname_text)
lname_entry.grid(row = 1,column=4)

#Exhibitor details - phone number
phone_text = StringVar()
phone_label = Label(app, text='Phone No.', font = 'Bold', pady = 5)
phone_label.grid(row=2, column=0, sticky = W)
phone_entry = Entry(app, textvariable= phone_text)
phone_entry.grid(row = 2,column=1)


#child check box - true or false


#Exhibitor details - DOB
dob_text = StringVar()
dob_label = Label(app, text='Date of Birth', font = 'Bold', pady = 5)
dob_label.grid(row=3, column=0, sticky = W)
dob_entry = Entry(app, textvariable= lname_text)
dob_entry.grid(row = 3,column=1)







#start program
app.mainloop()