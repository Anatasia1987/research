from tkinter import*
root = Tk()
root.geometry("500x300")

#Heading
Label (root, text="Submit Tickets", font="arial 15 bold").grid (row= 0, column=3)

#Field Name
name = Label(root, text="Name")
staffID = Label(root, text="StaffID")
email = Label(root, text="Email")
description = Label(root, text="Description")
response = Label(root, text="Response")

#Packing Fields
name.grid(row=1, column = 2)
staffID.grid(row=2, column = 2)
email.grid(row=3, column = 2)
description.grid(row=4, column = 2)
response.grid(row=5, column = 2)

#Variable for storing data
namevalue = StringVar
staffIDvalue = StringVar
emailvalue = StringVar
descriptionvalue = StringVar
responsevalue = StringVar
checkvalue = IntVar

#Entry field
nameentry = Entry(root, textvariable=namevalue)
staffIDentry = Entry(root, textvariable=staffIDvalue)
emailentry = Entry(root, textvariable=emailvalue)
descriptionentry = Entry(root, textvariable=descriptionvalue)
responseentry = Entry(root, textvariable=responsevalue)

nameentry.grid(row=1,column=3)
staffIDentry.grid(row=2,column=3)
emailentry.grid(row=3,column=3)
descriptionentry.grid(row=4,column=3)
responseentry.grid(row=5,column=3)

#Creating checkbox
checkbtn = Checkbutton(text = "Do you want to change password?", variable = checkvalue)
checkbtn.grid(row=6, column= 3)

root.mainloop()
