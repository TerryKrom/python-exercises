# jogo da forca
import random

words = [
    {
        "hint": "Animal",
        "words": ["camelo", "macaco", "girafa", "panda", "galinha"]
    },
    {
        "hint": "Fruta",
        "words": ["banana", "laranja", "melancia", "morango", "abacate"]
    },
    {
        "hint": "Esporte",
        "words": ["futebol", "volei", "basquete", "surf", "boxe"]
    },
]

print("="*10 +" Bem vindo ao jogo da forca! "+ "="*10)
# variables initialization
errors = 0
guesses = []

# chosen = random.choice(words)["words"][random.randint(0, len(words[0]))]

chosenDict = random.choice(words)
chosenWord = random.choice(chosenDict["words"])
hint = chosenDict["hint"]

splited = []
spaces = []
wordGuesses = []

for letter in chosenWord:
    splited.append(letter)
    spaces.append("_")
    
def findAndReplace(guess):
    indices = []
    for i, char in enumerate(chosenWord):
        if char == guess:
            indices.append(i)
    for indice in indices:
        spaces[indice] = guess

print("Dica: ", hint)
while True:
    print('\n')
    print("Palavra: ", spaces)    
    print("Erros: ", errors)
    print("Letras Jogadas: ", guesses)
    print("Palavras Tentadas: ", wordGuesses)
    if errors == 5:
        print("Fim de jogo!")
        break
    
    guess = input("Palpite atual: ")
    guess = guess.lower()
    print('\n')
    
    if len(guess) == 1:
    
        if guess in guesses:
            print("Letra ja foi escolhida!")
        else:
            if guess not in chosenWord:
                print("Letra errada! ")
                errors += 1
            if guess in chosenWord:
                print(f"Letra {guess} está correta! ")
                findAndReplace(guess)
            
            if "_" not in spaces:
                print("Você Ganhou!")
                print(f"A palavra era: {chosenWord}")
                break
        guesses.append(guess)
    else:
        if guess == chosenWord:
            print("Certa resposta! fim de jogo!")
            break
        else:
            print("Chute errado!")
            errors+=1
            wordGuesses.append(guess)