from var_dump import var_dump

from linkedlist import LinkedList
from pprint import pprint
from files import Files

def chooser_menu():
    option = input("\nDeseja exibir o menu novamente? Digite 1 para exibir\n")
    if(option=="1"):
        show_menu()
    else:
        return

def show_menu():
    print('|-----------------------------|')
    print('| 1- Exibir arquivos          |')
    print('| 2- Criar novo arquivo       |')
    print('| 3- Inserir palavra          |')
    print('| 4- Ler conteudo do arquivo  |\n')

    option = input('Escolha uma opção do menu\n')
    choose_option(option)


def choose_option(option):
    if option == "1":
        print('Lendo diretório...')
        files = Files()
        found_files = files.read_directory()
        counter = 0
        for index in found_files:
            print('Código do arquivo: {} - nome: {}'.format(counter, index))
            counter = counter + 1
    if option == 2:
        file = input('Digite um nome para o arquivo\n')
        frequency = input('Digite uma frequencia para o arquivo\n')
        files = Files()
        linkedlist =
        files.create_file(file)

    if option == "3":
        word = input('Digite uma palavra\n')
        file = input('Digite o nome do arquivo\n')
        files = Files()
        files.insert_word(word, file)

    if option == "4":
        file = input('Digite o nome do arquivo\n')
        files = Files()
        files.read_file(file)
    chooser_menu()



class Main:
    show_menu()




