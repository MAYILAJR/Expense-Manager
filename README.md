# Expense Manager

A Python-based expense management application that allows users to manage their income, expenses, and categories while storing financial transactions in a PostgreSQL database.

## Features

- Add expenses and income.
- Display all transactions.
- Calculate total expenses and income.
- Calculate account balance.
- Update transactions.
- Delete transactions.
- Add and manage categories.
- Store transaction data in PostgreSQL.
- Retrieve database credentials securely using HashiCorp Vault.

## Technologies Used

- **Python** – Application development.
- **PostgreSQL** – Database management.
- **Psycopg 3** – PostgreSQL connection.
- **HashiCorp Vault** – Secure database credential management.
- **HVAC** – Python client for HashiCorp Vault.
- **Git and GitHub** – Version control.

## Project Structure

```text
expense_manager/
│
├── main.py
├── expense_manager.py
├── transaction.py
├── category.py
├── database.py
│
├── tests/
│   ├── __init__.py
│   ├── test_categories.py
│   ├── test_connection.py
│   ├── test_vault.py
│   ├── test_insert_transaction.py
│   ├── test_update_transaction.py
│   └── test_delete_transaction.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation

1. Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
```

2. Navigate to the project directory:

```bash
cd expense_manager
```

3. Create a virtual environment:

```bash
python -m venv .venv
```

4. Activate the virtual environment on Windows:

```bash
.venv\Scripts\activate
```

5. Install dependencies:

```bash
pip install -r requirements.txt
```

## Database Configuration

This application uses PostgreSQL to store financial transactions and categories.

Database credentials are retrieved from HashiCorp Vault instead of being hardcoded in the application.

Before running the application, configure PostgreSQL and Vault with the required database credentials and environment variables.

## Running the Application

```bash
python main.py
```

## Running Tests

```bash
python -m tests.test_connection
python -m tests.test_vault
```

Other test files cover transaction and category operations.

## Security

- Database credentials are stored in HashiCorp Vault.
- The application uses a restricted Vault token.
- Sensitive files are excluded using `.gitignore`.

## Author

Developed as a personal software engineering learning project.