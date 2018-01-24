from red_black_tree import *

class Book (object):

    def __init__(self, title=None, qtd=None, author=None, edition=None):
        self.title = title
        self.qtd = qtd
        self.author = author
        self.edition = edition
