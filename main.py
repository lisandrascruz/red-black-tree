# -*- coding: utf-8 -*-
from red_black_tree import *
from library import *
from user import *
from book import *
from loan import *

def main():

    #CRIANDO ARVORES
    treeUsers = RBTree()
    treeBooks = RBTree()

    #CRIANDO LISTA DE EMPRÉSTIMOS#
    listLoan = []

    ## INTERFACE COM USUÁRIO ##
    print("Bem-vinda(o) à Biblioteca UFRPE\n")

    def printChoice():
        print ("Digite 1 para adicionar uma(um) usuária(o)\n 2 para buscá-la(o)\n 3 para removê-la(o)\n")
        print ("Digite 4 para adicionar um livro\n 5 para buscá-lo\n 6 para removê-lo\n")
        print ("Digite 7 para cadastrar um empréstimo\n 8 para removê-lo\n 9 para visualizar todos os empréstimos\n")
        print ("Digite 10 para relatório de usuários\n 11 para relatório de livros \n")
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
        elif choice == '7':
            Library.addLoan(treeUsers, treeBooks, listLoan)
        elif choice == '8':
            Library.deliveredLoan(listLoan)
        elif choice == '9':
            Loan.showListLoan(listLoan)
        elif choice == '10':
            Library.userReport(listLoan)
        elif choice == '11':
            Library.bookReport(listLoan)
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
