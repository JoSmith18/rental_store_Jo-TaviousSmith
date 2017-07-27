from disk import *
from core import *

def true_brand(menu):
    while True:
        print(selection_of_brand(menu))
        brand = input('What Brand Would You Like To Choose From?\n\n')
        valid_brand = (selection_of_brand(menu))
        if verify_brand(valid_brand, brand):
            return brand
        else:
            print('Invalid Brand')
def true_character(menu,brand):
    while True:
        selection = give_brand(menu, brand)
        characters = input('\n\tWhat Character Would You Like?\n{}\t*Price Per Hour*\n'.format(selection))
        for item in menu:
            if characters == item["Character"]:
                return characters
        else:
            print('Invalid Character')

def valid_time():
    times = ''' Our Times Are:
     \t1. 1hr
\t2. 2hr
\t3. 3hr
\t4. 4hr
                '''
    print('How Long Do You Want To Rent The Character')
    while True:
        time = float(input(times))
        if time == 1 or time == 2 or time ==3 or time == 4:
            return time
        else:
            print("We Can\'t Allow That Time, Pick Another One")
    
    
def main():

    print("\tHello Welcome To The Best Character Rental\n   Our Characters Are Guranteed To Rock The Kids Mental")

    input()

    menu = loadinventory()
   
    brand = true_brand(menu)

    characters = true_character(menu, brand)

    time = valid_time()

    price = add_rental_fee(time, characters, menu)

    print(price)

    new_menu = change_inventory(characters,menu)

    update_inventory(new_menu)

    answer = input("Is That The Only Character\n")


if __name__ == '__main__':
    main()
