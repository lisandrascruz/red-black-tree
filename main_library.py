from user import *
from book import *
from library import *

def main():
    userGabi = User('Gabi', '12345678954', '81999984782')
    bookAlgoritmos = Book('Algoritmos', '10', 'Korm', '3a')
    loan = Library('Gabi', 'bookAlgoritmos', '23/01/2018', None)

    print("A usuária ", userGabi.name, "está com o livro ", bookAlgoritmos.title, "desde a data ", loan.loanDate, '.')
    
main()
