from disk import *
from core import *

print("\tHello Welcome To The Best Character Rental\n   Our Characters Are Guranteed To Rock The Kids Mental")

input()

menu = loadinventory()

print(selection_of_brand(menu))

brand = input('What Brand Would You Like To Choose From?\n\n')

selection = give_brand(menu, brand)

purchase = input('\n{}\t*Price Per Hour*'.format(selection))