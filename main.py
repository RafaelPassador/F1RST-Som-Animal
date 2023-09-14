'''
Rafael Passador
09/23
Desafio F1RST - Enghenaria de Dados
'''

from animal_sound import AnimalSound

#Função principal que recebe a entrada do usuário e chama as funções necessárias1
def main():
    animal_sound = AnimalSound()

    while True:
        user_input = input("Digite '1' para GATO, '2' para CACHORRO, 'histórico' para ver o histórico ou 'sair' para encerrar: ")

        if user_input == '1':
            output = animal_sound.make_sound(1)
            print(f"Output: {output}")
        elif user_input == '2':
            output = animal_sound.make_sound(2)
            print(f"Output: {output}")
        elif user_input == 'histórico':
            output = animal_sound.show_history()
            print(f"Output: {output}")
        elif user_input == 'sair':
            break
        else:
            print("Entrada inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    main()
