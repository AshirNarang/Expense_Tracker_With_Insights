    # 💰 Expense Tracker with Insights

A command-line expense tracking application built in Python with a MySQL backend. Add, search, update, and delete your expenses, generate reports, and import/export your data as CSV — all from a clean terminal interface.

## Features

- ➕ **Add Expenses** — log date, category, amount, and description
- 📋 **View All Expenses** — see your full expense history at a glance
- 🔍 **Search Expenses** — by ID, category, or amount
- ✏️ **Update Expenses** — edit any existing record
- 🗑️ **Delete Expenses** — remove records with a confirmation prompt
- 📊 **Reports** — generate summary insights from your spending
- 📤 **Export to CSV** — export all data, or filter by category/amount
- 📥 **Import from CSV** — load expense data from an existing file
- 🗄️ **MySQL Backend** — persistent, structured storage

## Tech Stack

- **Language:** Python 3.14
- **Database:** MySQL
- **Libraries:** `mysql-connector-python`

## Project Structure

```
Expense_Tracker_with_Insights/
├── main.py              # Entry point — app loop and menu routing
├── tracker.py            # Core logic — menus, input handling, CSV import/export
├── database.py            # Database layer — all SQL queries
├── reports.py             # Report/insight generation
├── config_example.py     # Template for local configuration
├── config.py              # Your local config (not tracked in git)
├── requirements.txt
└── README.md
```

## Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/AshirNarang/Expense_Tracker_With_Insights.git
cd Expense_Tracker_With_Insights
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure your database
Copy the example config and fill in your own MySQL credentials:
```bash
cp config_example.py config.py
```
Then edit `config.py`:
```python
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "your_password_here"
DB_NAME = "expense_tracker"

file_opened = False
csv_file = ""
```

> ⚠️ `config.py` is excluded via `.gitignore` and should never be committed — it holds your real credentials.

### 4. Make sure MySQL is running
The app will automatically create the database and table on first run.

### 5. Run the app
```bash
python main.py
```

## Usage

On launch, you'll see a menu:
```
1. Add Expenses
2. View Expenses
3. Search Expenses
4. Update Expenses
5. Delete Expenses
6. Reports
7. Export CSV
8. Import CSV
9. Exit
```
Follow the on-screen prompts to navigate.

## Roadmap

- [ ] **v2:** Pandas-powered data analysis and insights
- [ ] **v3:** GUI / Web interface
- [ ] **v4:** Machine Learning-based spending predictions and anomaly detection
- [ ] **v5:** AI-powered insights and recommendations
- [ ] Multi-user support
## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

## Author

**Ashir Narang**