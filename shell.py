from disk import *
from core import *

def main():

    print("\tHello Welcome To The Best Character Rental\n   Our Characters Are Guranteed To Rock The Kids Mental")

    input()

    menu = loadinventory()

    print(selection_of_brand(menu))

    brand = input('What Brand Would You Like To Choose From?\n\n')

    selection = give_brand(menu, brand)

    characters = input('\n\tWhat Character Would You Like?\n{}\t*Price Per Hour*\n'.format(selection))

if __name__ == '__main__':
    main()
