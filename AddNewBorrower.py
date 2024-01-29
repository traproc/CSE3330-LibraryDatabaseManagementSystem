from tkinter import *
import sqlite3

def addNewBorrower():
    global cnum, name, address, phone, root

    # create tkinter window
    root = Tk()
    root.title("Library")
    root.geometry("1000x800")

    #Entries
    cnum = Entry(root, width = 80)
    cnum.grid(row = 0, column = 1, padx = 20)

    name = Entry(root, width = 80)
    name.grid(row = 1, column = 1)

    address = Entry(root, width = 80)
    address.grid(row = 2, column = 1)

    phone = Entry(root, width = 80)
    phone.grid(row = 3, column = 1)

    #Labels
    cnum_label = Label(root, text = 'Card Number: ')
    cnum_label.grid(row = 0, column = 0)

    name_label = Label(root, text = 'Name: ')
    name_label.grid(row = 1, column = 0)

    address_label = Label(root, text = 'Address: ')
    address_label.grid(row = 2, column = 0)

    phone_label = Label(root, text = 'Phone Number: ')
    phone_label.grid(row = 3, column = 0)

    info_label = Label(root, text = "Instructions: Enter the fields above to add a new borrower.")
    info_label.grid(row = 48, column = 1)

    #Buttons
    add_btn = Button(root, text ='Add', command = add)
    add_btn.grid(row = 49, column = 1, columnspan = 1, pady = 0, padx = 10, ipadx = 140)

    back_btn = Button(root, text ='Back', command = root.destroy)
    back_btn.grid(row = 50, column = 1, columnspan = 1, pady = 0, padx = 10, ipadx = 140)

    #executes tinker components
    root.mainloop()

def add():
    x = 6
    add_conn = sqlite3.connect('mydb.db')
    add_cur = add_conn.cursor()
    card_no = cnum.get()
    full_name = name.get()
    full_address = address.get()
    phone_no = phone.get()
    if card_no == "":
        add_cur.execute("INSERT INTO BORROWER(Name, Address, Phone) VALUES('"+full_name+"','"+full_address+"','"+phone_no+"')")
    else:
        add_cur.execute("INSERT INTO BORROWER VALUES('"+card_no+"','"+full_name+"','"+full_address+"','"+phone_no+"')")

    add_cur.execute("SELECT * FROM BORROWER ORDER BY Card_No")
    cnum_label = Label(root, text = 'Card Number')
    cnum_label.grid(row = 4, column = 0)

    name_label = Label(root, text = 'Name')
    name_label.grid(row = 4, column = 1)

    fee_label = Label(root, text = 'Address')
    fee_label.grid(row = 4, column = 2)

    phone_label = Label(root, text = 'Phone Number')
    phone_label.grid(row = 4, column = 3)

    dash1_label = Label(root, text = '------------')
    dash1_label.grid(row = 5, column = 0)

    dash2_label = Label(root, text = '---------------------------------------------------------------------------------------------')
    dash2_label.grid(row = 5, column = 1)

    dash3_label = Label(root, text = '--------------------------------------------------')
    dash3_label.grid(row = 5, column = 2)

    dash4_label = Label(root, text = '----------------------')
    dash4_label.grid(row = 5, column = 3)

    output_records = add_cur.fetchall()
    for output_record in output_records:
        for i in range(4):
            Label(root, text = str(output_record[i])).grid(row = x,column = i)
        x += 1

    #commit changes
    add_conn.commit()
    #close the DB connection
    add_conn.close()