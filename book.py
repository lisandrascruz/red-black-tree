class Book (object):

    title = None
    qtd = None
    author = None
    edition = None

    def __init__(self, title, qtd, author, edition):
        self.title = title
        self.qtd = qtd
        self.author = author
        self.edition = edition

    def insertBook
