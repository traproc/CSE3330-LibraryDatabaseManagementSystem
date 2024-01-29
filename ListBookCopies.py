from tkinter import *
import sqlite3

def listBookCopies():
    global btitle, root

    # create tkinter window
    root = Tk()
    root.title("Library")
    root.geometry("600x600")

    #Entries
    btitle = Entry(root, width = 80)
    btitle.grid(row = 0, column = 1, padx = 20)

    #Labels
    bid_label = Label(root, text = 'Book Title: ')
    bid_label.grid(row = 0, column = 0)

    info_label = Label(root, text = "Instructions: Given a book title the query will list \nthe number of copies loaned out per branch.")
    info_label.grid(row = 48, column = 1)

    #Buttons
    search_btn = Button(root, text ='Search', command = search)
    search_btn.grid(row = 49, column = 1, columnspan = 1, pady = 1, padx = 20, ipadx = 200)

    back_btn = Button(root, text ='Back', command = root.destroy)
    back_btn.grid(row = 50, column = 1, columnspan = 1, pady = 1, padx = 20, ipadx = 200)

    #executes tinker components
    root.mainloop()

def search():
    x = 3
    book_title = btitle.get()
    search_conn = sqlite3.connect('mydb.db')
    search_cur = search_conn.cursor()
    search_cur.execute("SELECT BL.Branch_Id, COUNT(BL.Book_Id) FROM BOOK_LOANS BL, BOOK B WHERE BL.Book_Id = B.Book_Id AND B.Title = '"+book_title+"' GROUP BY Branch_Id")

    brid_label = Label(root, text = 'Branch ID')
    brid_label.grid(row = 1, column = 0)

    noc_label = Label(root, text = 'Number of Copies Loaned')
    noc_label.grid(row = 1, column = 1)

    dash1_label = Label(root, text = '------------')
    dash1_label.grid(row = 2, column = 0)

    dash2_label = Label(root, text = '---------------------------------------------------------------------------------------------')
    dash2_label.grid(row = 2, column = 1)

    output_records = search_cur.fetchall()
    for output_record in output_records:
        for i in range(2):
            Label(root, text = str(output_record[i])).grid(row = x,column = i)
        x += 1

    #commit changes
    search_conn.commit()
    #close the DB connection
    search_conn.close()