from tkinter import *
import sqlite3

def addNewBook():
    global bid, btitle, publisher, author, root

    # create tkinter window
    root = Tk()
    root.title("Library")
    root.geometry("650x300")

    #Entries
    bid = Entry(root, width = 80)
    bid.grid(row = 0, column = 1, padx = 20)

    btitle = Entry(root, width = 80)
    btitle.grid(row = 1, column = 1)

    publisher = Entry(root, width = 80)
    publisher.grid(row = 2, column = 1)

    author = Entry(root, width = 80)
    author.grid(row = 3, column = 1)

    #Labels
    bid_label = Label(root, text = 'Book ID: ')
    bid_label.grid(row = 0, column = 0)

    btitle_label = Label(root, text = 'Book Title: ')
    btitle_label.grid(row = 1, column = 0)

    publisher_label = Label(root, text = 'Publisher Name: ')
    publisher_label.grid(row = 2, column = 0)

    author_label = Label(root, text = 'Author Name: ')
    author_label.grid(row = 3, column = 0)

    info_label = Label(root, text = "Instructions: Enter the fields above to add a book.")
    info_label.grid(row = 6, column = 1)

    #Buttons
    add_btn = Button(root, text ='Add', command = add)
    add_btn.grid(row = 7, column = 1, columnspan = 1, pady = 1, padx = 10, ipadx = 140)

    viewbook_btn = Button(root, text ='View Book Table', command = booktable)
    viewbook_btn.grid(row = 8, column = 1, columnspan = 1, pady = 1, padx = 10, ipadx = 140)

    viewauthor_btn = Button(root, text ='View Book Author Table', command = bookauthortable)
    viewauthor_btn.grid(row = 9, column = 1, columnspan = 1, pady = 1, padx = 10, ipadx = 140)

    viewbookcopy_btn = Button(root, text ='View Book Copies Table', command = bookcopytable)
    viewbookcopy_btn.grid(row = 10, column = 1, columnspan = 1, pady = 1, padx = 10, ipadx = 140)

    back_btn = Button(root, text ='Back', command = root.destroy)
    back_btn.grid(row = 11, column = 1, columnspan = 1, pady = 1, padx = 10, ipadx = 140)

    #executes tinker components
    root.mainloop()

def add():
    add_conn = sqlite3.connect('mydb.db')
    add_cur = add_conn.cursor()
    book_id = bid.get()
    book_title = btitle.get()
    publisher_name = publisher.get()
    author_name = author.get()
   
    add_cur.execute("INSERT INTO BOOK VALUES('"+book_id+"','"+book_title+"','"+publisher_name+"')")
    add_cur.execute("INSERT INTO BOOK_AUTHORS VALUES('"+book_id+"','"+author_name+"')")
    add_cur.execute("INSERT INTO BOOK_COPIES VALUES('"+book_id+"', 1, 5)")
    add_cur.execute("INSERT INTO BOOK_COPIES VALUES('"+book_id+"', 2, 5)")
    add_cur.execute("INSERT INTO BOOK_COPIES VALUES('"+book_id+"', 3, 5)")
    add_cur.execute("INSERT INTO BOOK_COPIES VALUES('"+book_id+"', 4, 5)")
    add_cur.execute("INSERT INTO BOOK_COPIES VALUES('"+book_id+"', 5, 5)") 

    added_label = Label(root, text = 'Book Added')
    added_label.grid(row = 4, column = 1)

    #commit changes
    add_conn.commit()
    #close the DB connection
    add_conn.close()

def booktable():
    x = 2
    btable = Tk()
    btable.title("Book Table")
    btable.geometry("800x700")

    btable_conn = sqlite3.connect('mydb.db')
    btable_cur = btable_conn.cursor()

    cnum_label = Label(btable, text = 'Book ID')
    cnum_label.grid(row = 0, column = 0)

    name_label = Label(btable, text = 'Book Title')
    name_label.grid(row = 0, column = 1)

    fee_label = Label(btable, text = 'Publisher Name')
    fee_label.grid(row = 0, column = 2)

    dash1_label = Label(btable, text = '------------')
    dash1_label.grid(row = 1, column = 0)

    dash2_label = Label(btable, text = '---------------------------------------------------------------------------------------------')
    dash2_label.grid(row = 1, column = 1)

    dash3_label = Label(btable, text = '--------------------------------------------------')
    dash3_label.grid(row = 1, column = 2)

    back_btn = Button(btable, text ='Back', command = btable.destroy)
    back_btn.grid(row = 50, column = 1, columnspan = 1, pady = 1, padx = 10, ipadx = 140)

    btable_cur.execute("SELECT * FROM BOOK") 

    output_records = btable_cur.fetchall()
    for output_record in output_records:
        for i in range(3):
            Label(btable, text = str(output_record[i])).grid(row = x,column = i)
        x += 1

    #close the DB connection
    btable_conn.close()

    #executes tinker components
    btable.mainloop()

def bookauthortable():
    x = 2
    batable = Tk()
    batable.title("Book Authors Table")
    batable.geometry("400x700")

    batable_conn = sqlite3.connect('mydb.db')
    batable_cur = batable_conn.cursor()

    cnum_label = Label(batable, text = 'Book ID')
    cnum_label.grid(row = 0, column = 0)

    name_label = Label(batable, text = 'Author Name')
    name_label.grid(row = 0, column = 1)

    dash1_label = Label(batable, text = '------------')
    dash1_label.grid(row = 1, column = 0)

    dash2_label = Label(batable, text = '-----------------------------------')
    dash2_label.grid(row = 1, column = 1)

    back_btn = Button(batable, text ='Back', command = batable.destroy)
    back_btn.grid(row = 50, column = 1, columnspan = 1, pady = 1, padx = 10, ipadx = 140)

    batable_cur.execute("SELECT * FROM BOOK_AUTHORS") 

    output_records = batable_cur.fetchall()
    for output_record in output_records:
        for i in range(2):
            Label(batable, text = str(output_record[i])).grid(row = x,column = i)
        x += 1

    #close the DB connection
    batable_conn.close()

    #executes tinker components
    batable.mainloop()

def bookcopytable():
    x = 2
    bctable = Tk()
    bctable.title("Book Copies Table")
    bctable.geometry("700x800")

    bctable_conn = sqlite3.connect('mydb.db')
    bctable_cur = bctable_conn.cursor()

    bid_label = Label(bctable, text = 'Book ID')
    bid_label.grid(row = 0, column = 0)

    brid_label = Label(bctable, text = 'Branch ID')
    brid_label.grid(row = 0, column = 1)

    noc_label = Label(bctable, text = 'Number of Copies')
    noc_label.grid(row = 0, column = 2)

    dash1_label = Label(bctable, text = '------------')
    dash1_label.grid(row = 1, column = 0)

    dash2_label = Label(bctable, text = '-----------------------------------')
    dash2_label.grid(row = 1, column = 1)

    dash3_label = Label(bctable, text = '-----------------------------------')
    dash3_label.grid(row = 1, column = 2)

    back_btn = Button(bctable, text ='Back', command = bctable.destroy)
    back_btn.grid(row = 50, column = 1, columnspan = 1, pady = 1, padx = 10, ipadx = 140)

    bctable_cur.execute("SELECT * FROM BOOK_COPIES") 

    output_records = bctable_cur.fetchall()
    for output_record in output_records:
        for i in range(3):
            Label(bctable, text = str(output_record[i])).grid(row = x,column = i)
        x += 1

    #close the DB connection
    bctable_conn.close()

    #executes tinker components
    bctable.mainloop()
