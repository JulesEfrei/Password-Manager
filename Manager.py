import xlrd
import xlwt
import time
from xlutils.copy import copy


def Crea_Mdp():
    global ADMIN_PASSWORD

    mdp = input("Create an admin password ")
    first.write(1, 1, mdp)
    wb.save("BD.xls")
    Access()

def Access():
    global ADMIN_PASSWORD
    global first
    global wb

    book = xlrd.open_workbook('BD.xls', formatting_info=True)
    wb = copy(book)
    feuille_1 = book.sheet_by_index(0)
    first = wb.get_sheet(0)
    rows = feuille_1.nrows

    ADMIN_PASSWORD = feuille_1.cell_value(1, 1)

    if ADMIN_PASSWORD == "":
        Crea_Mdp()

    connect = ".."

    while connect != ADMIN_PASSWORD:
        connect = str(input("What is your master password ? "))
        if connect == "q":
            time.sleep(1)
            break
    

    while connect == ADMIN_PASSWORD:
        print("*"*20)
        print("q  : Quit")
        print("gp : Get Password")
        print("sp : Store Password")
        print("*"*20)

        key = input()

        if key == "q":
            time.sleep(1)
            break
        if key == "gp":
            Find = False
            website = str(input("Website of the password "))
            i = 0
            while i < rows:
                if website.lower().strip() == feuille_1.cell_value(i, 0):
                    Find = True
                    print("Password of {} : {}".format(website, feuille_1.cell_value(i, 1)))
                    print("E-mail for this website : {}".format(feuille_1.cell_value(i, 2)))
                i += 1
    
            if Find == False:
                print("No password found")
    
        if key == "sp":
            website = str(input("Website of your password "))
            password = str(input("Your password "))
            email = str(input("Your E-mail "))
            first.write(rows, 0, website)
            first.write(rows, 1, password)
            first.write(rows, 2, email)
            wb.save("BD.xls")
            Access()