from tkinter import *
import sqlite3

def checkOutBook():
    global bid, brid, cnum, dout, ddate, root

    # create tkinter window
    root = Tk()
    root.title("Library")
    root.geometry("650x300")

    #Entries
    bid = Entry(root, width = 80)
    bid.grid(row = 0, column = 1, padx = 20)

    brid = Entry(root, width = 80)
    brid.grid(row = 1, column = 1)

    cnum = Entry(root, width = 80)
    cnum.grid(row = 2, column = 1)

    dout = Entry(root, width = 80)
    dout.grid(row = 3, column = 1)

    ddate = Entry(root, width = 80)
    ddate.grid(row = 4, column = 1)

    #Labels
    bid_label = Label(root, text = 'Book ID: ')
    bid_label.grid(row = 0, column = 0)

    brid_label = Label(root, text = 'Branch ID: ')
    brid_label.grid(row = 1, column = 0)

    cnum_label = Label(root, text = 'Card Number: ')
    cnum_label.grid(row = 2, column = 0)

    dout_label = Label(root, text = 'Date Out: ')
    dout_label.grid(row = 3, column = 0)

    ddate_label = Label(root, text = 'Due Date: ')
    ddate_label.grid(row = 4, column = 0)

    info_label = Label(root, text = "Instructions: Enter the fields above to check out a book.")
    info_label.grid(row = 48, column = 1)

    #Buttons
    brw_btn = Button(root, text ='Borrow', command = borrow)
    brw_btn.grid(row = 49, column = 1, columnspan = 1, pady = 0, padx = 10, ipadx = 140)

    viewborrower_btn = Button(root, text ='View Borrowers', command = bookcopiestable)
    viewborrower_btn.grid(row = 50, column = 1, columnspan = 1, pady = 0, padx = 10, ipadx = 140)

    viewbookloan_btn = Button(root, text ='View Book Loan Table', command = bookloantable)
    viewbookloan_btn.grid(row = 51, column = 1, columnspan = 1, pady = 0, padx = 10, ipadx = 140)

    back_btn = Button(root, text ='Back', command = root.destroy)
    back_btn.grid(row = 52, column = 1, columnspan = 1, pady = 0, padx = 10, ipadx = 140)

    #executes tinker components
    root.mainloop()

def borrow():
    brw_conn = sqlite3.connect('mydb.db')
    brw_cur = brw_conn.cursor()
    book_id = bid.get()
    branch_id = brid.get()
    card_no = cnum.get()
    date_out = dout.get()
    due_date = ddate.get()
    brw_cur.execute("CREATE TRIGGER IF NOT EXISTS update_num_copies AFTER INSERT ON BOOK_LOANS BEGIN UPDATE BOOK_COPIES SET No_Of_Copies = No_Of_Copies - 1 WHERE Book_Id = '"+book_id+"' AND Branch_Id = '"+branch_id+"'; END;")
    brw_cur.execute("INSERT INTO BOOK_LOANS(Book_Id, Branch_Id, Card_No, Date_Out, Due_Date) VALUES('"+book_id+"','"+branch_id+"','"+card_no+"','"+date_out+"','"+due_date+"')")

    added_label = Label(root, text = 'Book Checked Out')
    added_label.grid(row = 5, column = 1)

    #commit changes
    brw_conn.commit()
    #close the DB connection
    brw_conn.close()

def bookcopiestable():
    x = 2
    bctable = Tk()
    bctable.title("Borrower Table")
    bctable.geometry("900x800")

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

    dash2_label = Label(bctable, text = '---------------------------------------------------------------------------------------------')
    dash2_label.grid(row = 1, column = 1)

    dash3_label = Label(bctable, text = '------------------------')
    dash3_label.grid(row = 1, column = 2)

    back_btn = Button(bctable, text ='Back', command = bctable.destroy)
    back_btn.grid(row = 50, column = 1, columnspan = 1, pady = 1, padx = 10, ipadx = 140)

    bctable_cur.execute("SELECT * FROM BOOK_COPIES")

    output_records = bctable_cur.fetchall()
    for output_record in output_records:
        for i in range(3):
            Label(bctable, text = str(output_record[i])).grid(row = x,column = i)
        x += 1

    bctable_cur.execute("DROP TRIGGER IF EXISTS update_num_copies")

    #close the DB connection
    bctable_conn.close()

    #executes tinker components
    bctable.mainloop()

def bookloantable():
    x = 2
    bltable = Tk()
    bltable.title("Book Loan Table")
    bltable.geometry("1000x800")

    bltable_conn = sqlite3.connect('mydb.db')
    bltable_cur = bltable_conn.cursor()

    bid_label = Label(bltable, text = 'Book ID')
    bid_label.grid(row = 0, column = 0)

    brid_label = Label(bltable, text = 'Branch ID')
    brid_label.grid(row = 0, column = 1)

    cnum_label = Label(bltable, text = 'Card Number')
    cnum_label.grid(row = 0, column = 2)

    dout_label = Label(bltable, text = 'Date Out')
    dout_label.grid(row = 0, column = 3)

    ddate_label = Label(bltable, text = 'Due Date')
    ddate_label.grid(row = 0, column = 4)

    dret_label = Label(bltable, text = 'Date Returned')
    dret_label.grid(row = 0, column = 5)

    dash1_label = Label(bltable, text = '------------')
    dash1_label.grid(row = 1, column = 0)

    dash2_label = Label(bltable, text = '---------------------------------------------------------------------------------------------')
    dash2_label.grid(row = 1, column = 1)

    dash3_label = Label(bltable, text = '-------------')
    dash3_label.grid(row = 1, column = 2)

    dash4_label = Label(bltable, text = '-------------')
    dash4_label.grid(row = 1, column = 3)

    dash5_label = Label(bltable, text = '-------------')
    dash5_label.grid(row = 1, column = 4)

    dash6_label = Label(bltable, text = '-------------')
    dash6_label.grid(row = 1, column = 5)

    back_btn = Button(bltable, text ='Back', command = bltable.destroy)
    back_btn.grid(row = 50, column = 1, columnspan = 1, pady = 1, padx = 10, ipadx = 140)

    bltable_cur.execute("SELECT * FROM BOOK_LOANS ORDER BY Book_Id")

    output_records = bltable_cur.fetchall()
    for output_record in output_records:
        for i in range(6):
            Label(bltable, text = str(output_record[i])).grid(row = x,column = i)
        x += 1

    #close the DB connection
    bltable_conn.close()

    #executes tinker components
    bltable.mainloop()