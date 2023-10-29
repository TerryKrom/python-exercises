class UnitConverter:
    def __init__(self):
        self.choices = {
            1: self.kg_to_g,
            2: self.hours_to_minutes,
            3: self.liters_to_ml,
            4: self.quit
        }

    def display_menu(self):
        print("Selecione a conversão desejada:")
        print("1. Converter de kg para g")
        print("2. Converter de horas para minutos")
        print("3. Converter de litros para ml")
        print("4. Sair")

    def kg_to_g(self):
        kg = float(input("Digite a quantidade em quilogramas (kg): "))
        g = kg * 1000
        print(f"{kg} kg é igual a {g} gramas (g)")

    def hours_to_minutes(self):
        hours = float(input("Digite a quantidade em horas: "))
        minutes = hours * 60
        print(f"{hours} horas é igual a {minutes} minutos")

    def liters_to_ml(self):
        liters = float(input("Digite a quantidade em litros (L): "))
        ml = liters * 1000
        print(f"{liters} litros é igual a {ml} mililitros (mL)")

    def quit(self):
        print("Obrigado por usar o conversor. Adeus!")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Escolha uma opção (1/2/3/4): ")

            try:
                choice = int(choice)
                if choice in self.choices:
                    self.choices[choice]()
                else:
                    print("Opção inválida. Escolha uma opção válida.")
            except ValueError:
                print("Opção inválida. Escolha um número de opção válido.")


if __name__ == "__main__":
    converter = UnitConverter()
    converter.run()
