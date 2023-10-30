class UnitConverter:
    def __init__(self):
        self.choices = {
            1: self.kg_to_g,
            2: self.hours_to_minutes,
            3: self.liters_to_ml,
            4: self.quit
        }

    def display_menu(self):
        print("Select the desired conversion:")
        print("1. Convert from kg to g")
        print("2. Convert from hours to minutes")
        print("3. Convert from liters to ml")
        print("4. Quit")

    def kg_to_g(self):
        kg = float(input("Enter the amount in kilograms (kg): "))
        g = kg * 1000
        print(f"{kg} kg is equal to {g} grams (g)")

    def hours_to_minutes(self):
        hours = float(input("Enter the amount in hours: "))
        minutes = hours * 60
        print(f"{hours} hours is equal to {minutes} minutes")

    def liters_to_ml(self):
        liters = float(input("Enter the amount in liters (L): "))
        ml = liters * 1000
        print(f"{liters} liters is equal to {ml} milliliters (mL)")

    def quit(self):
        print("Thank you for using the converter. Goodbye!")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Choose an option (1/2/3/4): ")

            try:
                choice = int(choice)
                if choice in self.choices:
                    self.choices[choice]()
                else:
                    print("Invalid option. Choose a valid option.")
            except ValueError:
                print("Invalid option. Choose a valid option.")


converter = UnitConverter()
converter.run()