PURPLE_COLOR_BLOCK = ''' 


  ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗██╗ █████╗ ████████╗ ██████╗ 
██╔═══██╗████╗ ████║██╔══██╗████╗  ██║██║██╔══██╗╚══██╔══╝██╔═══██╗
██║██╗██║██╔████╔██║███████║██╔██╗ ██║██║███████║   ██║   ██║   ██║
██║██║██║██║╚██╔╝██║██╔══██║██║╚██╗██║██║██╔══██║   ██║   ██║   ██║
╚█║████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║██║██║  ██║   ██║   ╚██████╔╝
 ╚╝╚═══╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ 
                                                                   
'''

print("\033[95m", PURPLE_COLOR_BLOCK, "\033[0m")

import random
import os

def main():
    print("\033[91mSCRIPT CREATED BY: @MANIATO\033[0m")

    # Chiedi quanti numeri generare
    num_to_generate = get_number_to_generate()
    print("\033[92mHai scelto di generare", num_to_generate, "numeri.\033[0m")

    # Chiedi il prefisso
    prefix = get_prefix()
    print("\033[92mHai scelto il prefisso:", prefix, "\033[0m")

    # Chiedi se aggiungere il 39 davanti ai numeri
    add_39 = ask_add_39()
    if add_39:
        prefix = "39-" + prefix

    # Genera i numeri
    numbers_generated = generate_numbers(num_to_generate, prefix)

    # Salva i numeri su desktop
    save_to_file(numbers_generated)

    print("\033[95mSe desideri donare, puoi farlo all'indirizzo BTC:", "\033[93mbc1qm6s3f8adk5ymudx80dpmw2ky4u8mmxhdqhwepm\033[0m")

def get_number_to_generate():
    while True:
        try:
            num = int(input("\033[92mQuanti numeri vuoi generare? (da 1 a 10000000): \033[0m"))
            if 1 <= num <= 10000000:
                return num
            else:
                print("\033[91mscrivi bene coglione!!\033[0m")
        except ValueError:
            print("\033[91mscrivi bene coglione!!\033[0m")

def get_prefix():
    return input("\033[92mChe prefisso vuoi utilizzare? (es. 334-350-351): \033[0m")

def ask_add_39():
    while True:
        response = input("\033[92mVuoi mettere il 39 davanti ai numeri?\n1) SI E MUOVITI GAY\n2) NO HO PAURA\033[0m\n").lower()
        if response == "1" or response == "si":
            return True
        elif response == "2" or response == "no":
            return False
        else:
            print("\033[91mscrivi bene coglione!!\033[0m")

def generate_numbers(num_to_generate, prefix):
    numbers_generated = []
    for _ in range(num_to_generate):
        random_numbers = ''.join(str(random.randint(0, 9)) for _ in range(7))
        numbers_generated.append(prefix.replace("-", "") + random_numbers)
    return numbers_generated

def save_to_file(numbers_generated):
    desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    file_path = os.path.join(desktop_path, 'NumGenBy@MANIATO.txt')
    with open(file_path, 'w') as file:
        for number in numbers_generated:
            file.write(number + '\n')

if __name__ == "__main__":
    main()
