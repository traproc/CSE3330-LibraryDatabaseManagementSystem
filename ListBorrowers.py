from tkinter import *
import sqlite3

def listBorrowers():
    global cnum, name, root

    # create tkinter window
    root = Tk()
    root.title("Library")
    root.geometry("800x700")

    #Entries
    cnum = Entry(root, width = 80)
    cnum.grid(row = 0, column = 1, padx = 20)

    name = Entry(root, width = 80)
    name.grid(row = 1, column = 1)

    #Labels
    cnum_label = Label(root, text = 'Card Number: ')
    cnum_label.grid(row = 0, column = 0)

    name_label = Label(root, text = 'Name: ')
    name_label.grid(row = 1, column = 0)

    info_label = Label(root, text = "Instructions: Enter the fields above to list borrowers that have a book loan. \nYou can search either by a card number, name, part of the name, or with no filters/criteria.")
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
    full_name = name.get()
    search_conn = sqlite3.connect('mydb.db')
    search_cur = search_conn.cursor()

    if card_number == "" and full_name == "":
        search_cur.execute("SELECT DISTINCT Card_No, Borrower_Name, IIF(LateFeeBalance > 0, FORMAT(\"$%.2f\", LateFeeBalance), \"$0.00\") FROM vBookLoanInfo ORDER BY LateFeeBalance")
    elif full_name == "":
        search_cur.execute("SELECT DISTINCT Card_No, Borrower_Name, IIF(LateFeeBalance > 0, FORMAT(\"$%.2f\", LateFeeBalance), \"$0.00\") FROM vBookLoanInfo WHERE Card_No = '"+card_number+"' ORDER BY Card_no")
    elif card_number == "":
        search_cur.execute("SELECT DISTINCT Card_No, Borrower_Name, IIF(LateFeeBalance > 0, FORMAT(\"$%.2f\", LateFeeBalance), \"$0.00\") FROM vBookLoanInfo WHERE Borrower_Name = '"+full_name+"' OR Borrower_Name LIKE '%"+full_name+"%' ORDER BY Card_no")
    else:
        search_cur.execute("SELECT DISTINCT Card_No, Borrower_Name, IIF(LateFeeBalance > 0, FORMAT(\"$%.2f\", LateFeeBalance), \"$0.00\") FROM vBookLoanInfo WHERE Card_No = '"+card_number+"' AND (Borrower_Name = '"+full_name+"' OR Borrower_Name LIKE '%"+full_name+"%') ORDER BY Card_no")

    cnum_label = Label(root, text = 'Card Number')
    cnum_label.grid(row = 3, column = 0)

    name_label = Label(root, text = 'Name')
    name_label.grid(row = 3, column = 1)

    fee_label = Label(root, text = 'Late Fee Balance')
    fee_label.grid(row = 3, column = 2)

    dash1_label = Label(root, text = '------------')
    dash1_label.grid(row = 4, column = 0)

    dash2_label = Label(root, text = '---------------------------------------------------------------------------------------------')
    dash2_label.grid(row = 4, column = 1)

    dash3_label = Label(root, text = '---------------')
    dash3_label.grid(row = 4, column = 2)

    output_records = search_cur.fetchall()
    for output_record in output_records:
        for i in range(3):
            Label(root, text = str(output_record[i])).grid(row = x,column = i)
        x += 1