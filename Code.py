# -- Tkinter pip install tkinter
from tkinter import *
import sqlite3
from CheckOutBook import *
from AddNewBorrower import *
from AddNewBook import *
from ListBookCopies import *
from ListBookLoans import *
from ListBorrowers import *
from ListBooks import *

# create tkinter window
root = Tk()
root.title('Library')
root.geometry("800x600")
root.configure(bg = '#2E343E')

address_book_connect = sqlite3.connect('mydb.db')
address_book_cur = address_book_connect.cursor()

#Labels
headingLabel = Label(text = "Welcome to the Library", bg = 'gray', fg = 'white', font = ('TKDefaultFont',20))
headingLabel.place(relx = 0.2, rely = 0.1, relwidth = 0.6, relheight = 0.16)

#Buttons
button1 = Button(root, text = "Check out a Book", bg = 'gray', fg = 'white', command = checkOutBook)
button1.place(relx = 0.05, rely = 0.3, relwidth = 0.45, relheight = 0.1)

button2 = Button(root, text = "Add New Borrower", bg = 'gray', fg = 'white', command = addNewBorrower)
button2.place(relx = 0.05, rely = 0.4, relwidth = 0.45, relheight = 0.1)

button3 = Button(root, text = "Add New Book", bg = 'gray', fg = 'white', command = addNewBook)
button3.place(relx = 0.05, rely = 0.5, relwidth = 0.45, relheight = 0.1)

button4 = Button(root, text = "List Book Copies Loaned per Branch", bg = 'gray', fg = 'white', command = listBookCopies)
button4.place(relx = 0.5, rely = 0.3, relwidth = 0.45, relheight = 0.1)

button5 = Button(root, text = "List Book Loans that are Returned Late", bg = 'gray', fg = 'white', command = listBookLoans)
button5.place(relx = 0.5, rely = 0.4, relwidth = 0.45, relheight = 0.1)

button6 = Button(root, text = "List Borrowers with a Book Loan", bg = 'gray', fg = 'white', command = listBorrowers)
button6.place(relx = 0.5, rely = 0.5, relwidth = 0.45, relheight = 0.1)

button6 = Button(root, text = "List Books with a Book Loan", bg = 'gray', fg = 'white', command = listBooks)
button6.place(relx = 0.5, rely = 0.6, relwidth = 0.45, relheight = 0.1)

#executes tinker components
root.mainloop()