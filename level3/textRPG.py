import os
import random

icons = {
    'heart': '\U00002764️ ',
    'swords': '\u2694\uFE0F',
    'shield': '\U0001f6e1\uFE0F'
}

title = '''
  _____ _____ _____ _____ _____ _____ _____  
 |_____|_____|_____|_____|_____|_____|_____| 
(_)_____         _     ____  ____   ____  (_)
| |_   _|____  _| |_  |  _ \|  _ \ / ___| | |
| | | |/ _ \ \/ / __| | |_) | |_) | |  _  | |
| | | |  __/>  <| |_  |  _ <|  __/| |_| | | |
| | |_|\___/_/\_\\__|  |_| \_\_|    \____| | |
|_|                                       |_|
(_)____ _____ _____ _____ _____ _____ ____(_)
 |_____|_____|_____|_____|_____|_____|_____| 
 '''
# The monsters visual resource
monsters = {
    'rat': '''⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣶⣶⣦⡴⢶⣶⣶⣆⠸⠿⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⣻⣿⣷⣾⣿⣿⡿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣤⠄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⣾⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣾⣿⣿⣿⣿⣿⠿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⠀⣿⣿⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣟⠛⠻⣿⣿⣿⣿⣦⡈⠉⠛⠻⡆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣦⡈⢻⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣧⠈⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣀⡀⠸⣿⣿⣿⣿⣟⣀⣉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣾⡿⠟⠛⠀⠉⠛⠛⠛⠛⠛⠛⠛⠛⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢿⣧⣀⠀⠀⠀⠀⢀⣀⣠⣤⠶⠶⠶⠶⢶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠉⠛⠛⠛⠛⠉⠉⠀⠀⠀⠀⠀⣀⡼⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀''',
    'goblin': '''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⣿⣿⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⡼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢧⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠢⣤⣀⡀⠀⠀⠀⢿⣧⣄⡉⠻⢿⣿⣿⡿⠟⢉⣠⣼⡿⠀⠀⠀⠀⣀⣤⠔⠀
⠀⠀⠈⢻⣿⣶⠀⣷⠀⠉⠛⠿⠶⡴⢿⡿⢦⠶⠿⠛⠉⠀⣾⠀⣶⣿⡟⠁⠀⠀
⠀⠀⠀⠀⠻⣿⡆⠘⡇⠘⠷⠠⠦⠀⣾⣷⠀⠴⠄⠾⠃⢸⠃⢰⣿⠟⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠋⢠⣾⣥⣴⣶⣶⣆⠘⣿⣿⠃⣰⣶⣶⣦⣬⣷⡄⠙⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢋⠛⠻⠿⣿⠟⢹⣆⠸⠇⣰⡏⠻⣿⠿⠟⠛⡙⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⢧⡀⠠⠄⠀⠈⠛⠀⠀⠛⠁⠀⠠⠄⢀⡼⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⢻⣦⡀⠃⠀⣿⡆⢰⣿⠀⠘⢀⣴⡟⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣦⡀⠘⠇⠸⠃⢀⣴⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣷⣄⣠⣾⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⣿⣿⠟⠋⠀⠀⠀⠀⠀⠀⠀
    ''',
    'slime': '''
        
             ⣶⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⣿⣿⠻⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⣿⣿⡀⠈⠛⢿⣿⣿⣁⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⠟⠛⠛⠿⡄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⡟⢡⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⠀⣀⣉⣤⣤⣤⡀⣤⣄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠻⣿⣦⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⣠⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⣽⣿⣷⣄⠀⠀⠀⠀
⠀⠀⣾⡿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣿⣿⣿⣿⣷⣄⠀⠀
⠀⢀⣼⡀⠀⠀⠈⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⣿⠃⠀
'''
}

# dict of all items used in the game
items = {
    'healing':{
        'lifegem': {
            'hp': 15  
        },
        'health potion': {
            'hp': 25
        }
    }
}

# functions created to decrease writing the same code
# receive an function as parameter, and execute after press enter

def pressEnter(func):
    code = input()
    if code == '':
        func()

# the main character class

class Hero:
    # a dictionary with all 3 levels stats for the hero, hp, damage and armor
    levels = {
        'beginner': {
            'life': 20,
            'damage': 8,
            'armor': 10
        },
        'medium': {
            'life': 30,
            'damage': 12,
            'armor': 15
        },
        'advanced': {
            'life': 40,
            'damage': 16,
            'armor': 20
        }
    }
    def __init__(self, name):
        self.level = 'beginner'
        self.life = self.levels[self.level]["life"]
        self.damage = self.levels[self.level]["damage"]
        self.armor = self.levels[self.level]["armor"]
        self.actions = ["attack", "defense", "items", "check", "run"]
        self.items = {}
        self.name = name
    
    # function to view all items in the hero bag and use them
    
    def checkItems(self):
        if len(self.items) > 0:
            print(" Items ".center(26, '='))
            print()
            for item, count in self.items.items():
                print(f'{item} {count}x')
            print()
    
            while True:
                print("[i] to use an item")
                print("[Enter] to return")
                print()
                code = input()
                code = code.lower()
                if code == 'i':
                    item = input("Enter the item name: ")
                    if item in self.items:
                        self.useItem(item)
                        print(f"{item} used!")
                    else:
                        print("Invalid Name!")
                else:
                    break
    
        else:
            print('Empty bag!')
            print('[Enter] to return')
            while True:
                code = input()
                if code == '':
                    break
    
        self.itemsChecked = True

    # function to use the item, receive an item as parameter
    # realize the item effect
    
    def useItem(self, item):
        for item_type, item_data in items.items():
            if item in item_data:
                self.life += item_data[item]["hp"]
                print(f"+{item_data[item]['hp']} HP")
                del self.items[item]  # Remova o item do inventário após o uso

# class for all monsters in the game

class Monster:
    # a dictionary with the stats of the monster for each level
    levels = {
        'beginner': {
            'names': ['slime', 'goblin', 'rat'],
            'life': 10,
            'damage': 5,
            'armor': 3
        },
        'medium': {
            'names': ['big slime', 'skeleton', 'thief'],
            'life': 16,
            'damage': 8,
            'armor': 6
        },
        'advanced': {
            'names': ['giant slime', 'armored skeleton', 'warrior'],
            'life': 20,
            'damage': 10,
            'armor': 8
        },
    }
    
    def __init__(self, level):
        self.life = self.levels[level]['life']
        self.damage = self.levels[level]['damage']
        self.armor = self.levels[level]['armor']
        self.name = random.choice(self.levels[level]['names'])

# the dungeon class

class Dungeon:
    def __init__(self):
        self.current = 1

# the level class, use the dungeon class inside

class Level:
    def __init__(self):
        self.dungeon = Dungeon()

# function to get the corret name length
def getHeroName(prompt):
    while True:
        user_input = input(prompt)
        if len(user_input) <= 10:
            return user_input
        else:
            print("This name is too big! [Limit: 10 digits]")

# the main game class

class Game:
    def __init__(self):
        self.escaped = 0;
        self.inBattle = False
        self.lastActions = []
        self.part = 1
        self.parts = {
            1: self.partOne,
            2: self.partTwo,
            3: self.partThree,
        }
        self.opening()
    
    # function that exhibits all the game opening
    # also get the hero name and starts the game
    
    def opening(self):
        print(title)
        print()
        print(' Press [enter] to start '.center(43, '-'))
        code = input()
        if code == '':
            self.clear()
            print("- Let's begin our adventure")
            print("- What is the name of our hero? ")
            print()
            name = getHeroName("Your answer: ")
            if name == '':
                name = 'Hero'
            self.clear()
            print(f"Wonderful! nice to meet you, {name}")
            self.hero = Hero(name)
            print('- So...')
            print('- You will start your journey, lost inside of a cave')
            print("- You don't remember anything... ")
            print()
            print("Press [enter} to begin")
            pressEnter(self.parts[self.part])
        
    # function to resume the game after pause to check monster or item
    def resumeGame(self):
        self.clear()
        self.printMenu()
        self.resumeLevel()
    
    # function to print the current dungeon and avoid repeated code
    def printDungeon(self):
        print("- Dungeon", self.level.dungeon.current)
        
    # function to create and inicialize the next level
    def createLevel(self):
        self.level = Level()
        self.printDungeon()
        self.createMonster()
        self.printActions()
        self.inBattle = True
        self.battle()
        
    # function used in "resumeGame" function, to return to game
    def resumeLevel(self):
        self.printDungeon()
        print(f'- A {self.monster.name} appears!')
        self.printActions()
        self.inBattle = True
        self.battle()
        
    #function who stores all the game stats and exhibits it
    def printMenu(self):
        self.clear()
        name = self.hero.name.capitalize()
        hp = self.hero.life
        damage = self.hero.damage
        armor = self.hero.armor
        padName = name.center(len(name) + 2)
        padHeart = f'{icons["heart"]} {int(hp)}'.center(4)
        padSword = f'{icons["swords"]}  {int(damage)}'.center(4)
        padShield = f'{icons["shield"]}  {int(armor)}'.center(4)
        stats = f'{padHeart} {padSword} {padShield}'
        print(padName.center(26, '='))
        print(stats.center(29, ' '))
        print("=".center(26, '='))
     
     # print the player actions menu  
    def printActions(self):
        print()
        actions = self.hero.actions
        for act in actions:
            print(f'[{act[0]}] {act}')
        print()
        
    # function to create and store a monster in the game
    def createMonster(self):
        print()
        self.monster = Monster(self.hero.level)
        self.showMonster()
        print(f'- A {self.monster.name} appears!')
    
    # function to clear the console
    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    # exhibits the current monster stats
    def checkMonster(self):
        self.clear()
        self.inBattle = False
        print(' Stats '.center(26, '='))
        print(f'Name: {self.monster.name.capitalize()}')
        print()
        print(f'{icons["heart"]} {self.monster.life}')
        print(f'{icons["swords"]}  {self.monster.damage}')
        print(f'{icons["shield"]}  {self.monster.armor}')
        print()
        print('Press [enter} to return')
        pressEnter(self.resumeGame)
    
    # gets the player action and execute it
    def heroTurn(self):
        self.hero.itemsChecked = False
        
        action = input('Choose an action: ')
        action = action.lower()
        
        actions = {
             "a": self.heroAttack,
             "d": self.heroDefense,
             "i": self.hero.checkItems,
             "c": self.checkMonster,
             "r": self.runAway
        }
        
        if action in actions:
            actions[action]()
            
    # function to monster action         
    def monsterTurn(self):
        self.hero.life -= self.monster.damage
        self.lastActions.append(f'{self.monster.name} Attacked! -{self.monster.damage}')
    
    # >> All player actions
    def heroAttack(self):
        self.lastActions.append(f'{self.hero.name} Attacked! -{self.hero.damage}')
        self.monster.life -= self.hero.damage
            
    def heroDefense(self):
        self.lastActions.append(f'{self.hero.name} Defended!')
        self.monster.damage = self.monster.damage/2
    
    def runAway(self):
        if self.monster.life < 10:
            self.lastActions.append('Escaped!')
            self.escaped += 1
        else:
            self.lastActions.append('Cannot escape!')
    
    # refresh the game layout
    def showGameLayout(self, actions):
        self.clear()
        self.printMenu()
        self.printDungeon()
        print()
        self.showMonster()
        print(f'- A {self.monster.name} appears')
        print()
        self.printActions()
        for act in actions:
            print(act)
        print()
        
    def showMonster(self):
        if self.monster.name in monsters:
            print(monsters[self.monster.name].ljust(30, ' '))
        

    def battle(self):
        self.escaped = 0  # Reinicie 'escaped' no início da batalha
        while self.inBattle and self.hero.life > 0 and self.monster.life > 0 and self.escaped == 0:
            self.resetStats()
            self.heroTurn()
            self.showGameLayout(self.lastActions)
            if self.monster.life <= 0 or self.escaped == 1:
                print('You win!')
                self.hero.life += self.hero.levels[self.hero.level]["life"] / 5
                self.inBattle = False
                self.part += 1
                self.lastActions = []
                if self.part not in self.parts:
                    print("Dungeon completed!")
                    self.bossFight()
                    break
                elif self.part in self.parts:
                    print('Press [enter} to continue')
                    pressEnter(self.parts[self.part])
                    break
            if not self.hero.itemsChecked:
                self.monsterTurn()
                self.showGameLayout(self.lastActions)
            if self.hero.life <= 0:
                print(f'{self.monster.name} venceu a batalha!')
                self.gameOver()
                break
        
    def gameOver(self):
        self.clear()
        print('Game Over..')
        
    def resetStats(self):
        if self.monster.name in Monster.levels[self.hero.level]["names"]:
            self.monster.damage = Monster.levels[self.hero.level]["damage"]
    
    # ==> STAGE FUNCTIONS <== #
    
    def partOne(self):
        self.clear()
        self.printMenu()
        self.createLevel()
    
    def partTwo(self):
        self.clear()
        if self.monster.life <= 0:
            print(f'- After killing the {self.monster.name}')
            print('- you found an strange object in the body...')
            print('- you have found a lifegem!')
            self.hero.items['lifegem'] = 1
        
        print("- nice! you have killed your first monster")
        print("- Lets continue exploring the cave...")
        
        print()
        print('Press [enter} to continue')
        pressEnter(self.clear)
        self.printMenu()
        self.createLevel()
    
    def partThree(self):
        self.clear()
        self.printMenu()
        self.createLevel()
    
    def bossFight(self):
        self.clear()
        self.printMenu()
        print("Boss fight reached")
game = Game()