import os
import random

icons = {
    'heart': '\U00002764️ ',
    'swords': u"\u2694\uFE0F",
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
    'rat': '''
      ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣶⣶⣦⡴⢶⣶⣆⠸⠿⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⣻⣿⣷⣾⣿⣿⡿⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣤⠄⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⣾⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⢀⣴⣾⣿⣿⣿⣿⣿⠿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⠀⣿⣿⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣟⠛⠻⣿⣿⣿⣿⣦⡈⠉⠛⠻⡆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣦⡈⢻⣿⣿⣿⠇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣧⠈⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣀⡀⠸⣿⣿⣿⣿⣟⣀⣉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣾⡿⠟⠛⠀⠉⠛⠛⠛⠛⠛⠛⠛⠛⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢿⣧⣀⠀⠀⠀⠀⢀⣀⣠⣤⠶⠶⠶⠶⢶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠉⠛⠛⠛⠛⠉⠉⠀⠀⠀⠀⠀⣀⡼⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ''', 
    'goblin': '''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⣿⣿⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
          ⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢧⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠢⣤⣀⡀⠀⠀⠀⢿⣧⣄⡉⠻⢿⣿⣿⡿⠟⢉⣠⣼⡿⠀⠀⠀⠀⣀⣤⠔⠀
⠀⠀⠈⢻⣿⣶⠀⣷⠀⠉⠛⠿⠶⡴⢿⡿⢦⠶⠿⠛⠉⠀⣾⠀⣶⣿⡟⠁⠀⠀
⠀⠀⠀⠀⠻⣿⡆⠘⡇⠘⠷⠠⠦⠀⣾⣷⠀⠴⠄⠾⠃⢸⠃⢰⣿⠟⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠋⢠⣾⣥⣴⣶⣶⣆⠘⣿⣿⠃⣰⣶⣶⣦⣬⣷⡄⠙⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢋⠛⠻⠿⣿⠟⢹⣆⠸⠇⣰⡏⠻⣿⠿⠟⠛⡙⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⢧⡀⠠⠄⠀⠈⠛⠀⠀⠛⠁⠀⠠⠄⢀⡼⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⢻⣦⡀⠃⠀⣿⡆⢰⣿⠀⠘⢀⣴⡟⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣦⡀⠘⠇⠸⠃⢀⣴⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣷⣄⣠⣾⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⣿⣿⠟⠋
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
    ''',
    'knight': '''
            {}
           .--.
         ./.--.\.
          |====| 
          |`::`|  
      .-;`\..../`;_.-^-._
     /  |...::..|`   :   `|
    |   /   ::  |   .:.   |
    ;--'\...::..|..:::::..|
    <__> >._::_.| ':::::' |
    |  |/   ^^  |   ':'   |
    \::/|       \    :    /
    |||\|        \   :   / 
        |___/\___|`-.:.-`
         \_ || _/    `
         <_ >< _>
         |  ||  |
         |  ||  |
        _\.:||:./_
      ./____/\____\.
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
# receive a function as parameter, and execute after press enter

def pressEnter(func):
    code = input()
    if code == '':
        func()
    else:
        pressEnter(func)

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
                if self.items[item] == 0:
                    del self.items[item]  # Remova o item do inventário após o uso
                else:
                    self.items[item] -= 1

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
        
# the boss class

class Boss:
    bosses = {
        'knight': {
            'life': 30,
            'damage': 8,
            'armor': 10,
            'actions': {}
        }
    }
    
    def __init__(self, name, game):
        self.name = name
        self.life = self.bosses[name]['life']
        self.damage = self.bosses[name]['damage']
        self.armor = self.bosses[name]['armor']
        self.setActions(self.name)
        self.game = game
        
    def setActions(self, name):
        if name == 'knight':
            self.addActions('shieldbash', self.shieldbash)
            self.addActions('punch', self.punch)
            self.addActions('defense', self.defense)
    
    def addActions(self, act, func):
        self.bosses[self.name]["actions"][act] = func
    
    def shieldbash(self):
        damage = int(self.game.boss.damage/2)
        self.game.hero.life -= damage
        self.game.boss.armor += 4
        act = f"{self.name} uses Shield Bash! -{damage}HP\n- armor increased!"
        self.game.lastActions.append(act)
        pass
    
    def punch(self):
        damage = int(self.game.boss.damage+2)
        self.game.hero.life -= damage
        act = f"{self.name} uses Punch! -{damage}HP"
        self.game.lastActions.append(act)
        pass
        
    def defense(self):
        self.game.hero.damage = self.game.hero.damage/2
        act = f"{self.name} defended yourself! -{int(self.game.hero.damage/2*2)}ATK"
        self.game.lastActions.append(act)
        pass
    
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
        self.escaped = 0
        self.inBattle = False
        self.inBoss = False
        self.bossesKilled = []
        self.boss = None
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
        
        pressEnter(self.clear)
        
        print('- You wake up in a dark, cold, and damp place with only the distant')
        print('  echo of water droplets dripping in the depths of a cave.')
        print()
        pressEnter(self.clear)
        
        print('- Your mind is blank, with no memory of who you are \n  or how you ended up in this gloomy place.')
        print()
        pressEnter(self.clear)
        
        print('- Disoriented and frightened, you feel an urgent need to find answers \n  because something tells you that your life depends on it...')
        print()
        pressEnter(self.clear)
        
        print("- As you explore the dark walls of the cave, you come across a small opening.")
        print("- Inside it, a faint light illuminates an aged piece of paper.") 
        print("- When you pick it up, you notice it's a letter. With trembling hands, you unfold it, and at that moment, the words:") 
        print()
        name = getHeroName("Your name is: ")
        if name == '':
            name = 'Hero'
        self.hero = Hero(name)
        print()
        print("Press [enter] to begin")
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
    
    def createBossLevel(self):
        self.level = Level()
        self.createBoss()
        self.inBattle = True
        self.inBoss = True
        self.showBossLayout(self.lastActions)
        self.battle()
        
    # function used in "resumeGame" function, to return to game
    def resumeLevel(self):
        self.printDungeon()
        print(f'- A {self.monster.name} appears!')
        self.printActions()
        self.inBattle = True
        if self.inBoss:
            self.showBossLayout(self.lastActions)
        else:
            self.showGameLayout(self.lastActions)
        
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
        
    # ==> CREATE MONSTER AND BOSS <== #
    # function to create and store a monster in the game
    def createMonster(self):
        print()
        self.monster = Monster(self.hero.level)
        self.showMonster()
        print(f'- A {self.monster.name} appears!')
    
    def createBoss(self):
        self.boss = Boss('knight', self)
        self.monster = self.boss
    # ============================== #
    
    # function to clear the console
    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
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
        
        if action == '' or action not in actions:
            self.heroTurn()
            
        if action in actions:
            actions[action]()
            self.resetStats()
            
    # function to monster action         
    def monsterTurn(self):
        if self.boss:
            bossActions = self.boss.bosses[self.boss.name]["actions"]
            acts = []
            for act in bossActions:
                acts.append(act)
            act = random.choice(acts)
            bossActions[act]()
        else:
            damage = int((self.monster.damage - self.hero.armor*0.10))
            self.hero.life -= damage
            self.lastActions.append(f'{self.monster.name} Attacked! -{damage}')
    
    # >> All player actions << #
    def heroAttack(self):
        damage = int(self.hero.damage - self.monster.armor*0.10)
        self.lastActions.append(f'{self.hero.name} Attacked! -{damage}')
        if self.inBoss:
            self.boss.life -= damage
        else:
            self.monster.life -= damage
            
    def heroDefense(self):
        self.lastActions.append(f'{self.hero.name} Defended!')
        self.monster.damage = self.monster.damage/2
    
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
    
    def runAway(self):
        if self.monster.life < 10:
            self.lastActions.append('Escaped!')
            self.escaped += 1
        else:
            self.lastActions.append('Cannot escape!')
    
    # ======================= #
    # refresh the game layout
    def showGameLayout(self, actions):
        self.clear()
        self.printMenu()
        self.printDungeon()
        print()
        self.showMonster()
        print(f'- A {self.monster.name} appears')
        self.printActions()
        if len(actions) > 4:
            actions.pop(0)
        
        for act in actions:
            print(act)
        print()
    
    def showBossLayout(self, actions):
        self.clear()
        self.printMenu()
        self.showBoss()
        self.printActions()
        if len(actions) > 4:
            actions.pop(0)
        
        for act in actions:
            print(act)
        print()
    
    def showBoss(self):
        print(f" {self.boss.name} ".center(26, '='))
        name = self.boss.name.capitalize()
        hp = self.boss.life
        damage = self.boss.damage
        armor = self.boss.armor
        padName = name.center(len(name) + 2)
        padHeart = f'{icons["heart"]} {int(hp)}'.center(4)
        padSword = f'{icons["swords"]}  {int(damage)}'.center(4)
        padShield = f'{icons["shield"]}  {int(armor)}'.center(4)
        stats = f'{padHeart} {padSword} {padShield}'
        print(stats.center(29, ' '))
        print()
        print(monsters[self.boss.name])
        
    def showMonster(self):
        if self.monster.name in monsters:
            print(monsters[self.monster.name].ljust(30, ' '))
    
    def showWinMessage(self):
        self.clear()
        self.printMenu()
        self.printDungeon()
        print()
        self.showMonster()
        print()
        print('You win!')
        lifeEarned = self.hero.levels[self.hero.level]["life"] / 5
        self.hero.life +=  lifeEarned
        print(f'+{int(lifeEarned)} HP!')
        print()
        
    def battle(self):
        self.escaped = 0  # Reinicie 'escaped' no início da batalha
        while self.inBattle or self.inBoss and self.hero.life > 0 and self.monster.life > 0 and self.escaped == 0:
            self.resetStats()
            self.heroTurn()
            if self.inBoss:
                self.showBossLayout(self.lastActions)
            else:
                self.showGameLayout(self.lastActions)
            
            # when you escape or kill the monster, the battle ends
            if self.monster.life <= 0 or self.escaped == 1:
                self.showWinMessage()
                self.inBattle = False
                self.part += 1
                self.lastActions = []
                
                # if your current par is not on the stages, you're in a bossFight
                if self.part not in self.parts:
                    print("Dungeon completed!")
                    if self.boss == None:
                        print("Press [Enter] to continue")
                        pressEnter(self.bossFight)
                        break
                    
                    # if you kill the boss, the battle ends
                    if self.boss.life <=0 or self.monster.life <=0:
                        self.inBattle = False
                        self.inBoss = False
                        self.bossesKilled.append(self.monster.name)
                        self.clear()
                        print(f"{self.monster.name} killed!")
                        print("Press [Enter] to continue")
                        pressEnter(self.gameOver)
                        break
                    
                # if yout current part is in the game parts, the game continues
                elif self.part in self.parts:
                    print('Press [enter} to continue')
                    pressEnter(self.parts[self.part])
                    break
            # the monster will not attack the player after check his items
            if not self.hero.itemsChecked:
                self.monsterTurn()
                if self.inBoss:
                    self.showBossLayout(self.lastActions)
                else:
                    self.showGameLayout(self.lastActions)
            
            # if yout life turn to 0, game over
            if self.hero.life <= 0:
                print(f'{self.monster.name} wins!')
                print("You lose...")
                self.gameOver()
                break
        
    def gameOver(self):
        self.clear()
        print('Game Over..')
        
    def resetStats(self):
        if self.monster.name in Monster.levels[self.hero.level]["names"]:
            self.monster.damage = Monster.levels[self.hero.level]["damage"]
        if self.hero.damage < self.hero.levels[self.hero.level]["damage"]:
            self.hero.damage = self.hero.levels[self.hero.level]["damage"]
    
    # ==> STAGE FUNCTIONS <== #
    def partOne(self):
        self.clear()
        print()
        print("- After wake up and recover your sights")
        print("- You hear noises coming from behind a rock...")
        print()
        print('Press [enter] to continue')
        pressEnter(self.clear)
        self.printMenu()
        self.createLevel()
    
    def partTwo(self):
        self.clear()
        if self.monster.life <= 0:
            print()
            print(f'- After killing the {self.monster.name}')
            print('- you found an strange object in the body...')
            print('- you have found a lifegem!')
            self.hero.items['lifegem'] = 1
        print()
        print("- nice! you have killed your first monster")
        print("- Lets continue exploring the cave...")
        
        print()
        print('Press [enter] to continue')
        pressEnter(self.clear)
        self.printMenu()
        self.createLevel()
    
    def partThree(self):
        self.clear()
        print(f'- After killing the {self.monster.name}')
        print('- you found an strange object in the body...')
        print('- you have found a lifegem!')
        self.hero.items['lifegem'] += 1
        print()
        print('Press [enter] to continue')
        pressEnter(self.clear)
        self.printMenu()
        self.createLevel()
    
    def bossFight(self):
        self.clear()
        self.printMenu()
        self.createBossLevel()
    # <=====================> #
        
game = Game()