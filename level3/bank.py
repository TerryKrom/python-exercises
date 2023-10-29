import os

class Bank:
    def __init__(self):
        self.balance = 0
        
    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def display_menu(self):
        print("Bem-vindo ao Banco Python!")
        print("Escolha uma opção:")
        print("1. Verificar saldo")
        print("2. Depositar dinheiro")
        print("3. Sacar dinheiro")
        print("4. limpar tela")
        print("5. Sair")

    def check_balance(self):
        print(f"Seu saldo atual é: ${self.balance:.2f}")

    def deposit(self):
        amount = float(input("Digite o valor a ser depositado: $"))
        if amount > 0:
            self.balance += amount
            print(f"Você depositou ${amount:.2f}")
            self.check_balance()
        else:
            print("Quantidade inválida. O depósito deve ser maior que zero.")

    def withdraw(self):
        amount = float(input("Digite o valor a ser sacado: $"))
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Você sacou ${amount:.2f}")
            self.check_balance()
        else:
            print("Saldo insuficiente ou quantidade inválida.")

    def run(self):
        while True:
            self.display_menu()
            choice = int(input("Escolha uma opção (1/2/3/4/5): "))
            
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
            
if __name__ == "__main__":
    bank = Bank()
    bank.run()
