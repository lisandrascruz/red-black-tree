from user import *
from book import *

class Library (object):

    name = None
    book = None
    loanDate = None
    deliveryDate = None

    def __init__(self, user, book, loanDate, deliveryDate):
        self.user = user
        self.book = book
        self.loanDate = loanDate
        self.deliveryDate = deliveryDate

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

    def deleteUser(treeUsers, key=None):
        key = input("Digite a chave da(o) usuária(o) que deseja remover: ")
        key = int(key)
        treeUsers.deleteNode(key)
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

    def deleteBook(treeBooks, key=None):
        key = input("Digite a chave do livro que deseja remover: ")
        key = int(key)
        treeBooks.deleteNode(key)
        found = treeBooks.search(key)
        if found:
            print ('Livro não removido:', found.value.title ,'\n\n')
        else:
            print ("Livro removido.", '\n\n')
