import pandas as pd
import database 

def wait_for_user():
    input("Press Enter to continue ....")

def load_dataframe():
    
    conn = database.connect()

    df = pd.read_sql("SELECT * FROM expenses",conn)
    conn.close()

    return df

def total_spent():
    df = load_dataframe()
    total = df["amount"].sum()
    print("Total Spent: ",total)
    wait_for_user()

def average_spent():
    df = load_dataframe()
    avg = df["amount"].mean()
    print("Average Spent: ",avg)
    wait_for_user()

def maximum_spent():
    df = load_dataframe()
    maximum = df["amount"].max()
    print("Maximum Spent: ",maximum)
    wait_for_user()

def minimum_spent():
    df = load_dataframe()
    minimum = df["amount"].min()
    print("Minimum Spent: ",minimum)
    wait_for_user()

def total_transactions():
    df = load_dataframe()
    total = len(df)
    print("Total Transactions: ",total)
    wait_for_user()

def category_summary():
    df = load_dataframe()
    total = df.groupby("category")["amount"].sum()
    print("Category Summary:")
    print(total)
    wait_for_user()

def monthly_summary():
    df = load_dataframe()
    df["date"] = pd.to_datetime(df["date"])
    report = df.groupby(df["date"].dt.month_name())["amount"].sum()
    print("Monthly Summary")
    print(report)
    wait_for_user()

def top_5_spent():
    df = load_dataframe()
    top = df.nlargest(5,"amount")
    print("Top 5 Expenses")
    print(top)
    wait_for_user()

def complete_summury():
    total_spent()
    average_spent()
    maximum_spent()
    minimum_spent()
    total_transactions()
    category_summary()
    monthly_summary()
    top_5_spent()