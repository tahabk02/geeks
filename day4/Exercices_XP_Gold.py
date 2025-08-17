class BankAccount:
    def __init__(self, username, password, balance=0):
        self.username = username
        self.password = password
        self.balance = balance
        self.authenticated = False

    def authenticate(self, username, password):
        if self.username == username and self.password == password:
            self.authenticated = True
            print(f"{self.username} successfully authenticated.")
            return True
        else:
            print("Authentication failed.")
            return False

    def deposit(self, amount):
        if not self.authenticated:
            raise Exception("Please authenticate first!")
        if amount <= 0:
            raise Exception("Deposit amount must be positive!")
        self.balance += amount
        print(f"{amount} deposited. New balance: {self.balance}")

    def withdraw(self, amount):
        if not self.authenticated:
            raise Exception("Please authenticate first!")
        if amount <= 0:
            raise Exception("Withdraw amount must be positive!")
        if amount > self.balance:
            raise Exception("Insufficient funds!")
        self.balance -= amount
        print(f"{amount} withdrawn. New balance: {self.balance}")

# ---------------------------


class MinimumBalanceAccount(BankAccount):
    def __init__(self, username, password, balance=0, minimum_balance=0):
        super().__init__(username, password, balance)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if not self.authenticated:
            raise Exception("Please authenticate first!")
        if amount <= 0:
            raise Exception("Withdraw amount must be positive!")
        if (self.balance - amount) < self.minimum_balance:
            raise Exception("Cannot withdraw: minimum balance requirement!")
        self.balance -= amount
        print(f"{amount} withdrawn. New balance: {self.balance}")


# ---------------------------

class ATM:
    def __init__(self, account_list, try_limit=2):
        if not isinstance(account_list, list) or not all(isinstance(acc, (BankAccount, MinimumBalanceAccount)) for acc in account_list):
            raise Exception("account_list must contain BankAccount or MinimumBalanceAccount instances only")
        if not isinstance(try_limit, int) or try_limit <= 0:
            print("Invalid try_limit. Setting default try_limit = 2")
            try_limit = 2

        self.account_list = account_list
        self.try_limit = try_limit
        self.current_tries = 0

        self.show_main_menu()

    def show_main_menu(self):
        while True:
            print("\n--- ATM Main Menu ---")
            print("1. Log in")
            print("2. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                username = input("Enter username: ")
                password = input("Enter password: ")
                self.log_in(username, password)
            elif choice == "2":
                print("Exiting ATM. Goodbye!")
                break
            else:
                print("Invalid choice. Try again.")

    def log_in(self, username, password):
        for account in self.account_list:
            if account.username == username and account.authenticate(username, password):
                self.show_account_menu(account)
                return
        
        
        self.current_tries += 1
        print(f"Login failed. Attempt {self.current_tries}/{self.try_limit}")
        if self.current_tries >= self.try_limit:
            print("Maximum login attempts reached. Shutting down ATM.")
            exit()

    def show_account_menu(self, account):
        while True:
            print(f"\n--- Account Menu ({account.username}) ---")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                try:
                    amount = int(input("Enter deposit amount: "))
                    account.deposit(amount)
                except Exception as e:
                    print(f"Error: {e}")

            elif choice == "2":
                try:
                    amount = int(input("Enter withdraw amount: "))
                    account.withdraw(amount)
                except Exception as e:
                    print(f"Error: {e}")

            elif choice == "3":
                print("Exiting account menu.")
                break
            else:
                print("Invalid choice. Try again.")

# ---------------------------

if __name__ == "__main__":
    acc1 = BankAccount("alice", "alice123", 1000)
    acc2 = MinimumBalanceAccount("bob", "bob123", 500, minimum_balance=100)

    atm_machine = ATM([acc1, acc2], try_limit=3)
