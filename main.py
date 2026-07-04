import tracker
import database
import reports

database.setup()
database.connect()
while True:
    tracker.print_main_menu()
    choice = tracker.choose_selection()
    if choice==1:
        tracker.add_expensise()
    elif choice==2:
        tracker.display_all_expense()
    elif choice==3:
        tracker.print_search_menu()
        option = tracker.choose_selection()
        if option==1:
            tracker.search_expensis_by_ID()
        elif option==2:
            tracker.search_expensis_by_category()
        elif option==3:
            tracker.search_expensis_by_amount()
        elif option==4:
            print("Exiting....")
        else:
            print("Please Enter a Valid Option")
    elif choice==4:
        tracker.update_expense()
    elif choice==5:
        tracker.deleat_expense()
    elif choice==6:
        tracker.print_reports_menu()
        option = tracker.choose_selection()
        if option==1:
            reports.total_spent()
        elif option==2:
            reports.average_spent()
        elif option==3:
            reports.maximum_spent()
        elif option==4:
            reports.minimum_spent()
        elif option==5:
            reports.total_transactions()
        elif option==6:
            reports.category_summary()
        elif option==7:
            reports.monthly_summary()
        elif option==8:
            reports.top_5_spent()
        elif option==9:
            reports.complete_summury()
        elif option==10:
                print("Exiting....")
        else:
            print("Please Enter a Valid Option")
    elif choice==7:
        tracker.file_check()
        tracker.print_export_menu()
        option = tracker.choose_selection()
        if option==1:
            tracker.export_all_data()
        elif option==2:
            tracker.export_data_by_category()
        elif option==3:
            tracker.export_data_by_amount()
        elif option==4:
            print("Exiting....")
        else:
            print("Please Enter a Valid Option")
    elif choice==8:
        tracker.import_csv()
    elif choice==9:
        print("Exiting....")
        break