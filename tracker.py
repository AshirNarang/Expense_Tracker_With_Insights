import database
import csv
import config

def wait_for_user():
    input("Press Enter to continue ....")

def print_record(details):
    for detail in details:
        print("-"*50)
        print("ID: ", detail[0],"\nDate: " ,detail[1],"\nCategory: ", detail[2],"\nTotal Spent: ", detail[3],"\nDescription: " ,detail[4])

def print_main_menu():
    print("-"*50)
    print(" "*15 , "Expence Tracer")
    print("-"*50)
    print("1. Add Expenses \n2. View Expenses \n3. Search Expenses \n4. Update Expenses \n5. Delete Expenses \n6. Reports \n7. Export CSV \n8. Import CSV \n9. Exit")
    
def print_search_menu():
    print("1. Search using ID \n2. Search using Category \n3. Search using Amount \n4. Back")

def print_export_menu():
    print("1. Export All Expenses \n2. Export by Category \n3. Export by Amount Range \n4. Back")

def choose_selection():
    return int(input("Select an Opration:"))

def add_expensise():
    date = input("Date of Expence:(YYYY-MM-DD)")
    category = input("Category of Expence:")
    amt = float(input("Total Expence:"))
    descrption = input("Description:")

    database.insert_expense(date,category,amt,descrption)
    wait_for_user()

def display_all_expense():
    details = database.get_expense()
    print_record(details)
    wait_for_user()

def deleat_expense():
    id = int(input("Enter ID you want to delete:"))
    details = database.get_details(id)
    print_record(details)
    check = input("You want to delete this record from server? (y/n):")
    if check=="Y" or check=="y":
        database.delete_details(id)
        print("Record Deleted Successfully")
    elif check=="N" or check=="n":
        print("Recoed was not deleted")
    else:
        print("Invalid Input")
    wait_for_user()

def search_expensis_by_ID():
    search = input("Search by ID:")
    print("Searching.....")
    details = database.search_details_by_ID(search)
    print_record(details)
    wait_for_user()

def search_expensis_by_category():
    search = input("Search by Category:")
    print("Searching.....")
    details = database.search_details_by_category(search)
    print_record(details)
    wait_for_user()

def search_expensis_by_amount():
    search = input("Search by Amount:")
    print("Searching.....")
    details = database.search_details_by_amount(search)
    print_record(details)
    wait_for_user()

def update_expense():
    id = input("Search by ID:")
    print("Searching.....")
    details = database.search_details_by_ID(id)
    print_record(details)
    wait_for_user()
    date = input("Enter new date:")
    category = input("Enter new category:")
    amt = float(input("Enter new amount:"))
    desc = input("Enter new description:")
    database.update_details(id,date,category,amt,desc)
    details = database.search_details_by_ID(id)
    print_record(details)
    wait_for_user()

def export_data_by_category():
    print("WIP")

def open_csv_file():
    config.csv_file = input("Enter file location: ")

def file_check():
    if config.file_opened==True:
        print("File opened " , config.csv_file)
    else:
        open_csv_file()
        config.file_opened = True
        return config.file_opened

def import_csv():
    config.csv_file = input("Enter file location:")
    config.file_opened = True 

def export_all_data():
    with open(config.csv_file,mode="w+",newline="") as file:
        csv_writer = csv.writer(file)
        row_header = ["ID","Date","Category","Amount","Description"]
        csv_writer.writerow(row_header)
        details = database.get_expense()
        for detail in details:
            csv_writer.writerow(detail)
        print("Data Exported Successfully ...")
        wait_for_user()

def export_data_by_category():
    with open(config.csv_file,mode="w+",newline="") as file:
        csv_writer = csv.writer(file)
        row_header = ["ID","Date","Category","Amount","Description"]
        csv_writer.writerow(row_header)
        search = input("Enter category:")
        details = database.search_details_by_category(search)
        for detail in details:
            csv_writer.writerow(detail)
        print("Data Exported Successfully ...")
        wait_for_user()

def export_data_by_amount():
    with open(config.csv_file,mode="w+",newline="") as file:
        csv_writer = csv.writer(file)
        row_header = ["ID","Date","Category","Amount","Description"]
        csv_writer.writerow(row_header)
        search = input("Enter amount:")
        details = database.search_details_by_amount(search)
        for detail in details:
            csv_writer.writerow(detail)
        print("Data Exported Successfully ...")
        wait_for_user()

