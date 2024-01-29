from tkinter import *
import sqlite3

def listBooks():
    global cnum, bid, btitle, root

    # create tkinter window
    root = Tk()
    root.title("Library")
    root.geometry("1100x700")

    #Entries
    cnum = Entry(root, width = 80)
    cnum.grid(row = 0, column = 1, padx = 20)

    bid = Entry(root, width = 80)
    bid.grid(row = 1, column = 1, padx = 20)

    btitle = Entry(root, width = 80)
    btitle.grid(row = 2, column = 1)

    #Labels
    cnum_label = Label(root, text = 'Card Number: ')
    cnum_label.grid(row = 0, column = 0)

    bid_label = Label(root, text = 'Book ID: ')
    bid_label.grid(row = 1, column = 0)

    btitle_label = Label(root, text = 'Book Title: ')
    btitle_label.grid(row = 2, column = 0)

    info_label = Label(root, text = "Instructions: Enter the fields above to list books that are being loaned. \nYou must search with card number and any of the following search items:\n book id, books title, part of book title, or with no filters/criteria.")
    info_label.grid(row = 48, column = 1)

    #Buttons
    search_btn = Button(root, text ='Search', command = search)
    search_btn.grid(row = 49, column = 1, columnspan = 1, pady = 1, padx = 20, ipadx = 200)

    back_btn = Button(root, text ='Back', command = root.destroy)
    back_btn.grid(row = 50, column = 1, columnspan = 1, pady = 1, padx = 20, ipadx = 200)

    #executes tinker components
    root.mainloop()

def search():
    x = 5
    card_number = cnum.get()
    book_id = bid.get()
    book_title = btitle.get()
    search_conn = sqlite3.connect('mydb.db')
    search_cur = search_conn.cursor()

    if card_number == "" and book_title == "" and book_id == "":
        search_cur.execute("SELECT B.Book_Id, Book_Title, B.Publisher_Name, Branch_Id, IIF(LateFeeBalance >= 0, FORMAT(\"$%.2f\", LateFeeBalance), \"Non-Applicable\") FROM vBookLoanInfo BI, BOOK B WHERE B.Title = Book_Title ORDER BY LateFeeBalance DESC")
    elif book_title == "":
        search_cur.execute("SELECT B.Book_Id, Book_Title, B.Publisher_Name, Branch_Id, IIF(LateFeeBalance >= 0, FORMAT(\"$%.2f\", LateFeeBalance), \"Non-Applicable\") FROM vBookLoanInfo BI, BOOK B WHERE B.Title = Book_Title AND BI.Card_No = '"+card_number+"' AND B.Book_Id = '"+book_id+"' ORDER BY B.Book_Id")
    elif book_id == "":
        search_cur.execute("SELECT B.Book_Id, Book_Title, B.Publisher_Name, Branch_Id, IIF(LateFeeBalance >= 0, FORMAT(\"$%.2f\", LateFeeBalance), \"Non-Applicable\") FROM vBookLoanInfo BI, BOOK B WHERE B.Title = Book_Title AND BI.Card_No = '"+card_number+"' AND (Book_Title = '"+book_title+"' OR Book_Title LIKE '%"+book_title+"%') ORDER BY B.Book_Id")
    else:
        search_cur.execute("SELECT B.Book_Id, Book_Title, B.Publisher_Name, Branch_Id, IIF(LateFeeBalance >= 0, FORMAT(\"$%.2f\", LateFeeBalance), \"Non-Applicable\") FROM vBookLoanInfo BI, BOOK B WHERE B.Title = Book_Title AND BI.Card_No = '"+card_number+"' AND B.Book_Id = '"+book_id+"' AND (Book_Title = '"+book_title+"' OR Book_Title LIKE '%"+book_title+"%') ORDER BY B.Book_Id")

    bid_label = Label(root, text = 'Book ID')
    bid_label.grid(row = 3, column = 0)

    btitle_label = Label(root, text = 'Book Title')
    btitle_label.grid(row = 3, column = 1)

    pname_label = Label(root, text = 'Publisher Name')
    pname_label.grid(row = 3, column = 2)

    brid_label = Label(root, text = 'Branch ID')
    brid_label.grid(row = 3, column = 3)

    fee_label = Label(root, text = 'Late Fee Balance')
    fee_label.grid(row = 3, column = 4)

    dash1_label = Label(root, text = '------------')
    dash1_label.grid(row = 4, column = 0)

    dash2_label = Label(root, text = '---------------------------------------------------------------------------------------------')
    dash2_label.grid(row = 4, column = 1)

    dash3_label = Label(root, text = '--------------------------------------------------')
    dash3_label.grid(row = 4, column = 2)

    dash4_label = Label(root, text = '------------')
    dash4_label.grid(row = 4, column = 3)

    dash5_label = Label(root, text = '----------------------')
    dash5_label.grid(row = 4, column = 4)

    output_records = search_cur.fetchall()
    for output_record in output_records:
        for i in range(5):
            Label(root, text = str(output_record[i])).grid(row = x,column = i)
        x += 1