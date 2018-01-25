class Loan(object):

    def __init__(self, user, book, loanDate, deliveryDate, delivered=None):
        self.user = user
        self.book = book
        self.loanDate = loanDate
        self.deliveryDate = deliveryDate
        self.delivered = delivered

    def showListLoan(listLoan):
        i=0
        while i < len(listLoan):
            loan = listLoan[i]
            print (loan.user.name, " pegou emprestado o livro ", loan.book.title, " em ", loan.loanDate, " para entregar em ", loan.deliveryDate, '. Status: ', loan.delivered, '\n')
            i = i + 1
