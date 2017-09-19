from tkinter import *

window = Tk()
window.geometry("500x500")

def onClick():
    firstName = enterName.get()
    lastName = enterlastName.get()
    Balance = enterBalance.get()
    print(firstName , lastName , Balance)
    
titleLabel = Label(window, text = 'New Customer')

nameLabel = Label(window, text = ' First Name ')
enterName = Entry(window)

lastName = Label(window, text = ' Last Name ')
enterlastName = Entry(window)

Balance = Label(window, text = ' Card Balance ')
enterBalance = Entry(window)

clickButton = Button(window, text = 'Submit', command =onClick)

Qlabel = Label(window, text = ' How Helpful was this ')
cL = Listbox(window)
cL.insert(1, 'Yes')
cL.insert(2, 'No')

scale = Label(window, text = ' On a Scale of 1-100 how helpful was this')
Scale = Scale(window)


titleLabel.pack()
nameLabel.pack()
enterName.pack()
lastName.pack()
enterlastName.pack()
Balance.pack()
enterBalance.pack()
Qlabel.pack()
cL.pack()
scale.pack()
Scale.pack()
clickButton.pack()
window.mainloop ()