# Dicionário de mapeamento de código Morse
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    ' ': ' ',  # Espaço
}

# Função para converter texto em código Morse
def text_to_morse(text):
    text = text.upper()  # Converter o texto para maiúsculas
    morse_code = ''
    for char in text:
        if char in morse_code_dict:
            morse_code += morse_code_dict[char] + ' '
        else:
            morse_code += ' '# Usar um espaço em branco para caracteres desconhecidos
    return morse_code

# Função para converter código Morse em texto
def morse_to_text(morse_code):
    morse_code = morse_code.split(' ')
    text = ''
    for code in morse_code:
        for key, value in morse_code_dict.items():
            if code == value:
                text += key
                break
        else:
            text += ' '  # Usar espaço em branco para código Morse desconhecido
    text = text.capitalize()
    return text

print('='*8 + '< Morse Code >' + '='*8)
text = input("Enter text: ")

if '-' in text:
    print(morse_to_text(text))
else:
    print(text_to_morse(text))