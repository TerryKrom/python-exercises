import os
class MovieMenu:
    def __init__(self):
        self.movies = [
            {
                "title": "Punisher",
                "times": ["10:00 AM", "2:00 PM", "6:00 PM"]
            },
            {
                "title": "Avengers",
                "times": ["11:00 AM", "3:00 PM", "7:00 PM"]
            },
            {
                "title": "Batman",
                "times": ["11:30 AM", "1:30 PM", "8:30 PM"]
            }
        ]
        self.cart = []
        self.show_menu()
    
    def clear_console(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def getTitles(self):
        titles = []
        for movie in self.movies:
            titles.append(movie["title"].lower())
        return titles
        
    def getSessions(self, movie_name):
        sessions = []
        for movie in self.movies:
            if movie["title"].lower() == movie_name:
                sessions = movie["times"]
                break
        return sessions
    
    def show_movies(self):
        self.clear_console()
        print('='*8 + ' Movies ' + '='*8)
        print()
        for session in self.movies:
            print("Title:", session['title'])
            
        print()
        print("Enter 1 to purchase movie ticket")
        print("Enter 2 to return")
        try:
            code = int(input())
        except:
            code = 2
        
        if code == 1:
            movie = input("Enter the name of the movie: ")
            movie = movie.lower()
            titles = self.getTitles()
            if movie in titles:
                sessions = self.getSessions(movie)
                print("Choose the session: ")
                print(sessions)
                session = input('Your session: ')
                if session in sessions:
                    print('Purchase made successfully!')
                    formatMovie = f'{movie.capitalize()} - {session}'
                self.cart.append(formatMovie)
            else:
                print("Filme não encontrado")
        elif code == 2:
            self.show_menu()
            
    def show_menu(self):
        self.clear_console()
        while True:
            print('='*8 + ' Menu ' + '='*8)
            print()
            print("Enter 1 to show movies")
            print("Enter 2 to view your cart")
            print("Enter 3 to quit")
            
            try:
                code = int(input())
            except:
                self.show_menu()
                
            if code == 1:
                self.show_movies()
            elif code == 2:
                self.show_cart()
            elif code == 3:
                print("Quitting...")
                break
    def show_cart(self):
        self.clear_console()
        print('='*8 + ' Cart ' + '='*8)
        print()
        print(self.cart)
        print()
        print("Press enter to return")
        code = input()
        if code == None or code == '':
            self.show_menu()

movie_menu = MovieMenu()