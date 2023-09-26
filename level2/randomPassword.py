import random
import string

def generate_strong_password(length=12):
    # Define os critérios para a senha forte
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = "!@#$%^&*()_+-=[]{}|;:,.<>?/\\"

    # Crie uma lista contendo pelo menos um caractere de cada critério
    password_characters = (
        random.choice(uppercase_letters) +
        random.choice(lowercase_letters) +
        random.choice(digits) +
        random.choice(special_characters)
    )

    # Preencha o restante da senha com caracteres aleatórios
    password_characters += ''.join(random.choice(string.printable) for _ in range(length - len(password_characters)))

    # Embaralhe a senha para torná-la mais segura
    password_list = list(password_characters)
    random.shuffle(password_list)
    password = ''.join(password_list)

    return password

# Solicita ao usuário o comprimento desejado para a senha
length = int(input("Digite o comprimento desejado da senha: "))

# Gera a senha forte
strong_password = generate_strong_password(length)
print("Senha forte gerada:", strong_password)


# def something(parametro=12):
# parametro opicional
# uppercase_letters = string.ascii_uppercase
# lowercase_letters = string.ascii_lowercase
# digits = string.digits
# special_characters = "!@#$%^&*()_+-=[]{}|;:,.<>?/\\"
# OBTER TODOS OS DIGITOS PRESENTES NO TECLADO
#