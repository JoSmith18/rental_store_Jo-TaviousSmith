from disk import *
from core import *

def true_brand(menu):
    while True:
        brand = input('What Brand Would You Like To Choose From?\n\n')
        valid_brand = (selection_of_brand(menu))
        if verify_brand(valid_brand, brand):
            return brand
        else:
            print('Invalid Brand')

def main():

    print("\tHello Welcome To The Best Character Rental\n   Our Characters Are Guranteed To Rock The Kids Mental")

    input()

    menu = loadinventory()

    print(selection_of_brand(menu))

    brand = true_brand(menu)


    selection = give_brand(menu, brand)

    characters = input('\n\tWhat Character Would You Like?\n{}\t*Price Per Hour*\n'.format(selection))

    times = ''' Our Times Are:
     \t1. 1hr
\t2. 2hr
\t3. 3hr
\t4. 4hr
                '''
    print('How Long Do You Want To Rent The Character')
    time = float(input(times))
    
    price = add_rental_fee(time, characters, menu)

    print(price)

    new_menu = change_inventory(characters,menu)

    update_inventory(new_menu)

    answer = input("Is That The Only Character\n")


if __name__ == '__main__':
    main()
