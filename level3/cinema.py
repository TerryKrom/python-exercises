import os

class Cinema:
    def __init__(self, rows, seats_per_row):
        self.rows = rows
        self.seats_per_row = seats_per_row
        self.seating_matrix = [['[L]' for _ in range(seats_per_row)] for _ in range(rows)]

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        
    def show_seating(self):
        self.clear()
        print("L = Livre")
        print("R = Reservado")
        for row in self.seating_matrix:
            print(" ".join(row))
        print("\n")

    def reserve_seat(self, row, seat):
        if row < 1 or row > self.rows or seat < 1 or seat > self.seats_per_row:
            print("Assento inválido. Tente novamente.")
        elif self.seating_matrix[row - 1][seat - 1] == '[R]':
            print("Este assento já está ocupado.")
        else:
            self.seating_matrix[row - 1][seat - 1] = '[R]'
            print(f"Assento {row}-{seat} reservado com sucesso.")
        
    def available_seats(self):
        self.clear()
        available = []
        for i in range(self.rows):
            for j in range(self.seats_per_row):
                if self.seating_matrix[i][j] == '[L]':
                    available.append((i + 1, j + 1))
        return available

# Exemplo de uso:
cinema = Cinema(6, 6)
while True:
    print("Escolha uma opção:")
    print("1 - Mostrar layout do cinema")
    print("2 - Reservar assento")
    print("3 - Listar assentos disponíveis")
    print("4 - Sair")
    choice = input()

    if choice == '1':
        cinema.show_seating()
    elif choice == '2':
        try:
            row = int(input("Digite o número da fileira: "))
            seat = int(input("Digite o número do assento: "))
            cinema.reserve_seat(row, seat)
        except:
            print('Valor invalido')
    elif choice == '3':
        available_seats = cinema.available_seats()
        if available_seats:
            print("Assentos disponíveis:")
            for seat in available_seats:
                print(f"Fileira {seat[0]}, Assento {seat[1]}")
        else:
            print("Não há assentos disponíveis.")
    elif choice == '4':
        print('Encerrando...')
        break
