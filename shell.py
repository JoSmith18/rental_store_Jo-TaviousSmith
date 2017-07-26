from disk import *
from core import *

print("\tHello Welcome To The Best Character Rental\n   Our Characters Are Guranteed To Rock The Kids Mental")

input()

menu = loadinventory()

brand = input('What Brand Would You Like To Choose From?\n')

print(give_brand(menu, brand))