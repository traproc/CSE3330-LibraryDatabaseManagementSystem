from tkinter import *
import sqlite3

def listBookLoans():
    global dfrom, dto, root

    # create tkinter window
    root = Tk()
    root.title("Library")
    root.geometry("1000x600")

    #Entries
    dfrom = Entry(root, width = 80)
    dfrom.grid(row = 0, column = 1)

    dto = Entry(root, width = 80)
    dto.grid(row = 1, column = 1)

    #Labels
    dfrom_label = Label(root, text = 'Due Date From: ')
    dfrom_label.grid(row = 0, column = 0)

    dto_label = Label(root, text = 'Due Date To: ')
    dto_label.grid(row = 1, column = 0)

    info_label = Label(root, text = "Instructions: Given any due date range the query will list the book loans \nthat were returned late and how many days they were late.")
    info_label.grid(row = 48, column = 1)
    
    #Buttons
    search_btn = Button(root, text ='Search', command = search)
    search_btn.grid(row = 49, column = 1, columnspan = 1, pady = 1, padx = 20, ipadx = 200)

    back_btn = Button(root, text ='Back', command = root.destroy)
    back_btn.grid(row = 50, column = 1, columnspan = 1, pady = 1, padx = 20, ipadx = 200)

    #executes tinker components
    root.mainloop()

def search():
    x = 4
    date_from = dfrom.get()
    date_to = dto.get()
    search_conn = sqlite3.connect('mydb.db')
    search_cur = search_conn.cursor()
    search_cur.execute("SELECT Book_Id, Branch_Id, Card_No, Date_Out, Due_Date, Returned_Date, Cast((JULIANDAY(Returned_Date) - JULIANDAY(Due_Date)) AS Integer) FROM BOOK_LOANS WHERE Due_Date BETWEEN '"+date_from+"' AND '"+date_to+"' AND Late = 1 GROUP BY Book_Id")

    bid_label = Label(root, text = 'Book ID')
    bid_label.grid(row = 2, column = 0)

    brid_label = Label(root, text = 'Branch ID')
    brid_label.grid(row = 2, column = 1)

    cnum_label = Label(root, text = 'Card Number')
    cnum_label.grid(row = 2, column = 2)

    dout_label = Label(root, text = 'Date Out')
    dout_label.grid(row = 2, column = 3)

    ddate_label = Label(root, text = 'Due Date')
    ddate_label.grid(row = 2, column = 4)

    dret_label = Label(root, text = 'Date Returned')
    dret_label.grid(row = 2, column = 5)

    noc_label = Label(root, text = 'Days Late')
    noc_label.grid(row = 2, column = 6)

    dash1_label = Label(root, text = '------------')
    dash1_label.grid(row = 3, column = 0)

    dash2_label = Label(root, text = '---------------------------------------------------------------------------------------------')
    dash2_label.grid(row = 3, column = 1)

    dash3_label = Label(root, text = '-------------')
    dash3_label.grid(row = 3, column = 2)

    dash4_label = Label(root, text = '-------------')
    dash4_label.grid(row = 3, column = 3)

    dash5_label = Label(root, text = '-------------')
    dash5_label.grid(row = 3, column = 4)

    dash6_label = Label(root, text = '-------------')
    dash6_label.grid(row = 3, column = 5)

    dash7_label = Label(root, text = '------------')
    dash7_label.grid(row = 3, column = 6)

    output_records = search_cur.fetchall()
    for output_record in output_records:
        for i in range(7):
            Label(root, text = str(output_record[i])).grid(row = x,column = i)
        x += 1

    #commit changes
    search_conn.commit()
    #close the DB connection
    search_conn.close()