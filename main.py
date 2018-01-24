from red_black_tree import *
from library import *
from user import *
from book import *

def main():

    #CRIANDO ARVORES
    treeUsers = RBTree()
    treeBooks = RBTree()

    ## INTERFACE COM USUÁRIO ##
    print("Bem-vinda(o) à Biblioteca UFRPE\n")

    def printChoice():
        print ("Digite 1 para adicionar uma(um) usuária(o)\n 2 para buscá-la(o)\n 3 para removê-la(o)\n")
        print ("Digite 4 para adicionar um livro\n 5 para buscá-lo\n 6 para removê-lo\n")
        print ("Ou digite 0 para sair.\n")
        print ("Obs: A chave dos usuários e dos livros são sequenciais.")

    choice = None
    while choice !='0':
        printChoice()
        choice = input("Digite sua escolha: ")
        if choice == '1':
            Library.addUser(treeUsers)
        elif choice == '2':
            Library.searchUser(treeUsers)
        elif choice == '3':
            Library.deleteUser(treeUsers)
        elif choice == '4':
            Library.addBook(treeBooks)
        elif choice == '5':
            Library.searchBook(treeBooks)
        elif choice == '6':
            Library.deleteBook(treeBooks)
        else:
            print ("Escolha uma opção válida.")

    # #TESTANDO BUSCAR LIVROS
    # print('')
    # print("TESTANDO BUSCAR LIVROS NA ÁRVORE")
    # found = treeBooks.search(20)
    # if found:
    #     print('Livro encontrado: ', found.value.title, '\n\n')
    # else:
    #     print('Livro não encontrado.')
    #
    # #TESTANDO BUSCAR USERS
    # print('')
    # print("TESTANDO BUSCAR USERS NA ÁRVORE")
    # found = treeUsers.search(20)
    # if found:
    #     print('Usuária(o) encontrada(o): ', found.value.name, '\n\n')
    # else:
    #     print('Usuária(o) não encontrada(o).')


main()
