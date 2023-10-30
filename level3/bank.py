import os

class Bank:
    def __init__(self):
        self.balance = 0
        
    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def display_menu(self):
        print("Welcome to python Bank!")
        print("Choose and option:")
        print("1. Check Balance")
        print("2. Make a Deposit")
        print("3. Withdraw")
        print("4. Clear the Screen")
        print("5. Quit")

    def check_balance(self):
        print(f"Your balance is: ${self.balance:.2f}")

    def deposit(self):
        amount = float(input("Enter the value: $"))
        if amount > 0:
            self.balance += amount
            print(f"You entered ${amount:.2f}")
            self.check_balance()
        else:
            print("Invalid quantity. The deposit must be greater than zero.")

    def withdraw(self):
        amount = float(input("Enter the amount to be withdrawn: $"))
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"You withdrawn ${amount:.2f}")
            self.check_balance()
        else:
            print("Insufficient balance or invalid quantity.")

    def run(self):
        while True:
            self.display_menu()
            choice = int(input("Choose and option (1/2/3/4/5): "))
            
            actions = {
                1: self.check_balance,
                2: self.deposit,
                3: self.withdraw,
                4: self.clear,
            }
            
            if choice == 5:
                print('closing')
                break
            
            actions[choice]()
            
bank = Bank()
bank.run()
