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

    #def insertBook():

    #def deleteBook():
