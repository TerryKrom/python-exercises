# let's count how many times a word appear in a sentence

def word_counter(text):
    # Divida o texto em palavras separadas por espaços
    words = text.split()
    
    # Crie um dicionário para armazenar a contagem de cada palavra
    counter = {}
    
    # Itere pelas palavras no texto
    for word in words:
        # Remove pontuações e converte para letras minúsculas
        word = word.strip('.,!?()[]{}":;')
        word = word.lower()
        
        # Se a palavra já estiver no dicionário, incremente a contagem
        if word in counter:
            counter[word] += 1
        else:
            # Caso contrário, adicione a palavra ao dicionário com contagem 1
            counter[word] = 1
    print('WORD - COUNT')
    for item, value in counter.items():
        print(f"{item} - {value}")