# Banking Application

This is a comprehensive banking application developed in Python. It includes functionalities such as creating accounts, depositing and withdrawing money, changing PINs, applying for loans, and viewing account details and mini statements.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Modules](#modules)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- **Create Account**: Allows users to create a new bank account.
- **Enquiry**: Users can check their balance and recent transactions.
- **Deposit**: Users can deposit money into their account.
- **Withdraw**: Users can withdraw money from their account.
- **Change PIN**: Users can change their ATM PIN.
- **Apply for Loans**: Users can apply for various types of loans such as home, gold, education, and crop loans.
- **Mini Statements**: Users can view their recent transactions.

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/banking-application.git
    ```

2. Change to the project directory:

    ```sh
    cd banking-application
    ```

3. Install the required dependencies (if any):

    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the main script:

    ```sh
    python Main.py
    ```

2. Follow the on-screen instructions to use the banking application.

## Modules

### Main.py

This is the main script that provides a menu for the user to interact with the application.

### createAccount.py

Contains functions to create a new bank account and manage account details in a JSON file.

### enquiry.py

Contains functions for account balance enquiry and viewing mini statements.

### Loans.py

Contains functions to apply for various types of loans and calculate EMI and total payable amounts.

### pinChange.py

Contains functions to change the ATM PIN.

### Withdraw_deposite.py

Contains functions to deposit and withdraw money and update the transactions in a JSON file.