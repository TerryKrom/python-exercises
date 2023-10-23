import os

def createHeader(txt):
    print('=' * 8 + f' {txt} ' + '=' * 8)
    print()

class Agenda:
    def __init__(self):
        self.contacts = []
        self.showMenu()
    
    def clearConsole(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        
    def showContacts(self):
        self.clearConsole()
        createHeader("My contacts")
        if len(self.contacts) > 0:
            for contact in self.contacts:
                print('Name: ', contact['name'])
                print('Phone: ', contact['phone'])
        else:
            print("Empty agenda!")
        
        print('Press enter to return')
        code = input()
        if code == '':
            self.showMenu()
            
    def showMenu(self):
        while True:
            self.clearConsole()
            createHeader("Menu")
            print('Enter 1 to add contacts')
            print('Enter 2 to remove contacts')
            print('Enter 3 to show contacts')
            print('Enter 4 to quit')
            try:
                code = int(input())
            except:
                code = 4
                
            if code == 1:
                self.addContact()
            elif code == 2:
                self.removeContact()
            elif code == 3:
                self.showContacts()
            elif code == 4:
                print('Closing...')
                break
            
    def addContact(self):
        self.clearConsole()
        createHeader('Add Contact')
        name = input('Contact name: ')
        phone = input('Phone: ')
        contact = {
            'name': name,
            'phone': phone
        }
        self.contacts.append(contact)
        print(f"{name} added!")
        print("Press enter to return")
        code = input()
        if code == '':
            self.showMenu()
    
    def removeContact(self):
        self.clearConsole()
        createHeader('Remove Contact')
        print("Who you want to delete?")
        name = input('Contact name: ')
        
        # Extrair a lista de nomes dos contatos
        try:
            names = [contact['name'] for contact in self.contacts]
        except:
            print('No contacts added! ')
        
        if name in names:
            print(f"Are you sure you want to delete {name}? (Y/N)")
            confirm = input().lower()
            
            if confirm == 'y':
                # Encontrar o índice do contato a ser removido
                index = names.index(name)
                
                # Remover o contato da lista
                removed_contact = self.contacts.pop(index)
                
                print(f"Contact {name} has been deleted.")
            else:
                print("Deletion canceled.")
        else:
            print(f"Contact {name} not found in your contacts.")

    
agenda = Agenda()