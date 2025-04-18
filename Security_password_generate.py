import string
import random

# Mensajes traducidos
messages = {
    "en": {
        "enter_length": "Enter the password length (between 8 and 16): ",
        "invalid_length": "Please enter a number between 8 and 16.",
        "invalid_number": "Please enter a valid number.",
        "generated_password": "Your generated password is:",
        "generate_another": "Do you want to generate another password? (Yes: Y / No: N): ",
        "generated_passwords": "Generated passwords:",
        "select_password": "Select the number of the password you like the most: ",
        "invalid_choice": "Please select a valid number.",
        "selected_password": "You selected: {} Copy and paste your password in a safe place.",
        "exit": "Press Enter to exit."
    },
    "es": {
        "enter_length": "Introduce la longitud de la contraseña (entre 8 y 16): ",
        "invalid_length": "Por favor, introduce un número entre 8 y 16.",
        "invalid_number": "Por favor, introduce un número válido.",
        "generated_password": "Tu contraseña generada es:",
        "generate_another": "¿Quieres generar otra contraseña? (Sí: S / No: N): ",
        "generated_passwords": "Contraseñas generadas:",
        "select_password": "Selecciona el número de la contraseña que más te gusta: ",
        "invalid_choice": "Por favor, selecciona un número válido.",
        "selected_password": "Has seleccionado: {} Copia y pega tu contraseña en un lugar seguro.",
        "exit": "Presiona Enter para salir."
    },
    "pt": {
        "enter_length": "Insira o comprimento da senha (entre 8 e 16): ",
        "invalid_length": "Por favor, insira um número entre 8 e 16.",
        "invalid_number": "Por favor, insira um número válido.",
        "generated_password": "Sua senha gerada é:",
        "generate_another": "Você quer gerar outra senha? (Sim: S / Não: N): ",
        "generated_passwords": "Senhas geradas:",
        "select_password": "Selecione o número da senha que você mais gosta: ",
        "invalid_choice": "Por favor, selecione um número válido.",
        "selected_password": "Você selecionou: {} Copie e cole sua senha em um lugar seguro.",
        "exit": "Pressione Enter para sair."
    }
}

# Selección de idioma
def select_language():
    while True:
        print("Select a language / Seleccione un idioma / Selecione um idioma:")
        print("1. English")
        print("2. Español")
        print("3. Português")
        choice = input("Enter your choice / Ingrese su elección / Insira sua escolha: ").strip()
        if choice == '1':
            return "en"
        elif choice == '2':
            return "es"
        elif choice == '3':
            return "pt"
        else:
            print("Invalid choice. Please try again. / Elección inválida. Inténtelo de nuevo. / Escolha inválida. Tente novamente.")

language = select_language()
msg = messages[language]

# Generación de contraseñas
def generate_password():
    while True:
        try:
            length = int(input(msg["enter_length"]))
            if 8 <= length <= 16:
                break
            else:
                print(msg["invalid_length"])
        except ValueError:
            print(msg["invalid_number"])

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

passwords = []

# Generar y guardar contraseñas
while True:
    password = generate_password()
    passwords.append(password)
    print(msg["generated_password"], password)
    
    while True:
        another = input(msg["generate_another"]).strip().lower()
        if another in ['y', 'n', 's']:
            break
        else:
            print("Invalid input. Please enter 'Y' or 'N'. / Entrada inválida. Por favor, ingrese 'Y' o 'N'. / Entrada inválida. Por favor, insira 'Y' ou 'N'.")
    
    if another in ['n']:
        break

# Mostrar contraseñas generadas
print("\n" + msg["generated_passwords"])
for i, pwd in enumerate(passwords, 1):
    print(f"{i}. {pwd}")

# Selección de contraseña
while True:
    try:
        choice = int(input("\n" + msg["select_password"]))
        if 1 <= choice <= len(passwords):
            print(msg["selected_password"].format(passwords[choice - 1]))
            break
        else:
            print(msg["invalid_choice"])
    except ValueError:
        print(msg["invalid_number"])

# Salida
input(msg["exit"] + " Exit...")
