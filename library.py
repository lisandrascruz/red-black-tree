from user import *
from book import *
from loan import *

class Library (object):

    def addUser(treeUsers):
        name = input("Digite o nome do usuária(o): ")
        cpf = input("CPF: ")
        phone = ("Contato: ")
        user = User(name, cpf, phone)
        key = treeUsers.getMax() + 1
        nodeUser = RBNode(key=key, value=user)
        treeUsers.insertNode(nodeUser)
        treeUsers.show(nodeUser)
        found = treeUsers.search(key)
        if found:
            print ('Usuária(o) adicionada(o). \n\n')
        else:
            print("Não foi possível adicionar. Tente novamente mais tarde.", '\n\n')

    def searchUser(treeUsers, key=None):
        key = input("Digite a chave da(o) usuária(o) que deseja buscar: ")
        key = int(key)
        found = treeUsers.search(key)
        if found:
            print ("Usuária(o) encontrada(o): ", found.value.name, '\n\n')
        else:
            print ("Usuária(o) não encontrada(o).", '\n\n')

    def searchUserLoan(treeUsers, key):
        key = int(key)
        userLoan = treeUsers.search(key)
        return userLoan

    def deleteUser(treeUsers, key=None):
        key = input("Digite a chave da(o) usuária(o) que deseja remover: ")
        key = int(key)
        node = treeUsers.search(key)
        treeUsers.deleteNode(node)
        found = treeUsers.search(key)
        if found:
            print ('Usuária(o) não removida(o):', found.value.name ,'\n\n')
        else:
            print ("Usuária(o) removida(o).", '\n\n')

    def addBook(treeBooks):
        title = input("Digite o título do livro: ")
        qtd = input("Qual a quantidade de livros: ")
        author = input("Digite o(s) autor(es):  ")
        edition = input("Qual a edição: ")
        book = Book(title, qtd, author, edition)
        key = treeBooks.getMax() + 1
        nodeBooks=RBNode(key=key, value=book)
        treeBooks.insertNode(nodeBooks)
        treeBooks.show(nodeBooks)
        found = treeBooks.search(key)
        if found:
            print('Livro adicionado: ', found.value.title, '\n\n')
        else:
            print("Não foi possível adicionar. Tente novamente mais tarde.")

    def searchBook(treeBooks, key=None):
        key = input("Digite a chave do livro que deseja buscar: ")
        key = int(key)
        found = treeBooks.search(key)
        if found:
            print ("Livro encontrada(o): ", found.value.title, '\n\n')
        else:
            print ("Livro não encontrada(o).", '\n\n')

    def searchBookLoan(treeBooks, key):
        key = int(key)
        bookLoan = treeBooks.search(key)
        return bookLoan

    def deleteBook(treeBooks, key=None):
        key = input("Digite a chave do livro que deseja remover: ")
        key = int(key)
        node = treeBooks.search(key)
        treeBooks.deleteNode(node)
        found = treeBooks.search(key)
        if found:
            print ('Livro não removido:', found.value.title ,'\n\n')
        else:
            print ("Livro removido.", '\n\n')

    def addLoan(treeUsers, treeBooks, listLoan):
        keyUser = input("Digite a chave do usuário que vai realizar o empréstimo: ")
        keyBook = input("Digite a chave do livro: ")
        loanDate = input("Digite a data de empréstimo: ")
        deliveryDate = input("Digite a data de entrega: ")
        user = Library.searchUserLoan(treeUsers, keyUser).value
        book = Library.searchBookLoan(treeBooks, keyBook).value
        loan = Loan(user, book, loanDate, deliveryDate, 'not delivered')
        listLoan.append(loan)
        # Loan.showListLoan(listLoan)

    def deliveredLoan(listLoan):
        name = input("Digite o nome do usuário que vai entregar o livro: ")
        book = input("Digite o título do livro a ser entregue: ")
        i=0
        for i in range(0, len(listLoan)):
            if name == listLoan[i].user.name and book == listLoan[i].book.title:
                listLoan[i].delivered = 'delivered'
            else:
                print("Empréstimo não encontrado.")
