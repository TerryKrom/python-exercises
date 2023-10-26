import os
import random

icons = {
    'heart': '\U00002764️ ',
    'swords': '\u2694\uFE0F',
    'shield': '\U0001f6e1\uFE0F'
}

def pressEnter(func):
    code = input()
    if code == '':
        func()

class Hero:
    def __init__(self, name):
        self.level = 'beginner'
        self.life = 20
        self.damage = 8
        self.armor = 10
        self.actions = ["attack", "defense", "items", "check", "run"]
        self.items = []
        self.name = name
        
    def checkItems(self):
        if len(self.items) > 0:
            for item in self.items:
                print(item)
        else:
            print('Empty bag!')
        
class Monster:
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

class Dungeon:
    def __init__(self):
        print('Dungeon 1')
        
class Level:
    def __init__(self):
        self.dungeon = Dungeon()
        print('Level started!')
        
class Game:
    def __init__(self):
        self.inBattle = True
        self.opening()
        
    def opening(self):
        print('- Welcome to Text RPG!')
        print()
        print("- Let's begin our adventure")
        print("- What is the name of our hero? ")
        print()
        name = input('Your answer: ')
        if name == '':
            name = 'Hero'
        self.clear()
        print(f"Wonderful! nice to meet you, {name}")
        self.hero = Hero(name)
        print('- So...')
        print('- You will start your journey, lost inside of a cave')
        print("- You don't remember anything... ")
        print()
        print("Press enter to begin")
        pressEnter(self.startGame)
    
    def startGame(self):
        self.clear()
        self.printMenu()
        self.createLevel()
    
    def resumeGame(self):
        self.clear()
        self.printMenu()
        self.resumeLevel()
        
    def createLevel(self):
        self.level = Level()
        self.createMonster()
        self.printActions()
        self.battle()
        self.inBattle = True
        
    
    def resumeLevel(self):
        print(f'- A {self.monster.name} appears!')
        self.printActions()
        self.battle()
        self.inBattle = True
        
            
    def printMenu(self):
        self.clear()
        name = self.hero.name
        hp = self.hero.life
        damage = self.hero.damage
        armor = self.hero.armor
        print('='*8+f' {name} '+'='*8)
        stats = f'{icons["heart"]} {int(hp)} {icons["swords"]} {int(damage)}  {icons["shield"]} {int(armor)}'
        print(stats.center(26, ' '))
        
    def printActions(self):
        print()
        actions = self.hero.actions
        for act in actions:
            print(f'[{act[0]}] {act}')
        print()
        
    def createMonster(self):
        print()
        self.monster = Monster(self.hero.level)
        print(f'- A {self.monster.name} appears!')
        
    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def checkMonster(self):
        self.clear()
        self.inBattle = False
        print('Stats: ')
        print(f'Name: {self.monster.name}')
        print(f'{icons["heart"]} {self.monster.life}')
        print(f'{icons["swords"]} {self.monster.damage}')
        print(f'{icons["shield"]} {self.monster.armor}')
        print()
        print('Press enter to return')
        pressEnter(self.resumeGame)
    
    def heroTurn(self):
        action = input('Choose an action: ')
        
        actions = {
             "a": self.heroAttack,
             "d": self.heroDefense,
             "i": self.hero.checkItems,
             "c": self.checkMonster,
             "r": self.runAway
        }
        
        if action in actions:
            actions[action]()
        
    e = 0;
    
    def monsterTurn(self):
        self.hero.life -= self.monster.damage
        print(f'{self.monster.name} Attacked! -{self.monster.damage}')
        
    def heroAttack(self):
        print(f'{self.hero.name} Attacked! -{self.hero.damage}')
        self.monster.life -= self.hero.damage
            
    def heroDefense(self):
        print(f'{self.hero.name} Defended!')
        self.monster.damage = self.monster.damage/2
    
    def runAway(self):
        if self.monster.life <= 10:
            print('Escaped!')
            self.e += 1
        else:
            print('Cannot escape!')
            
    def battle(self):
        self.e = 0  # Reinicie 'e' no início da batalha
        while self.inBattle and self.hero.life > 0 and self.monster.life > 0 and self.e == 0:
            self.resetStats()
            self.heroTurn()
            if self.monster.life <= 0:
                print('You win!')
                break
            self.monsterTurn()
            if self.hero.life <= 0:
                print(f'{self.monster.name} venceu a batalha!')
                break
    
        print('Press enter to continue')
        self.inBattle = False
        pressEnter(self.printMenu)
    
    def resetStats(self):
        if self.monster.name in Monster.levels[self.hero.level]["names"]:
            self.monster.damage = Monster.levels[self.hero.level]["damage"]
            
game = Game()