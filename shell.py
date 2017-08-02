from disk import *
from core import *

def return_character(menu,brand):
    """ [{}], '' -> 
    Takes brand and menu and return the 
    character if given a valid brand
    >>> return_character([{'Brand': 'Marvel', 'Character': 'IronMan', 'Stock': 4, 'Price': 85.00, 'Rented': 0, 'Value': 430}],'Marvel')
    'IronMan'
    """
    selection = give_character(menu, brand)
    while True:
        characters = input("\n{}\n*Exact Spelling*\nWhat Character Will You Be Returning?\n".format(selection))
        for item in menu:
            if characters == item["Character"]:
                return characters    
    else:
        print("Invalid Character!!")

def return_brand(menu):
    """ [{}] -> ''
    Takes in a menu and if 
    given valid brand
    returns brand
    """
    while True:
        print(selection_of_brand(menu))
        brand = input("\nWhat Brand Is Your Character From?\n").title()
        valid_brand = selection_of_brand(menu)
        if verify_brand(valid_brand, brand):
            return brand
    else:
        print("Invalid Brand")

def true_name():
    """ -> ''
    Return name if valid without numbers
    """
    while True:
        name = input("Hello, What Is Your Name For Security Purposes\n")
        if valid_name(name):
            return name

def true_brand(menu):
    """ [{}] -> ''
    Takes in menu and return
    brand when given valid response
    """
    while True:
        print(selection_of_brand(menu))
        brand = input('What Brand Would You Like To Choose From?\n\n').title()
        valid_brand = (selection_of_brand(menu))
        if verify_brand(valid_brand, brand):
            return brand
        else:
            print('Invalid Brand')
def true_character(menu,brand):
    """([{}],'')->''
    Takes in a menu and brand
    and return characters when
    given valid answer
    """
    while True:
        selection = give_brand(menu, brand)
        characters = input('\n\tWhat Character Would You Like?\n{}\t\t\t Exact Spelling\n\t\t\t*Price Per Hour*\n'.format(selection))
        for item in menu:
            if characters == item["Character"]:
                return characters
        else:
            print('Invalid Character')

def valid_time():
    """ None -> int
    Until valid time is given keep asking
    when valid response given return response
    """
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
def valid_decision():
    """ -> ''
    Returns a valid decision
    """
    while True:
        decision = input("\tAre You:\nRenting or Returning?\n")
        if decision.strip().title() == 'Renting'.strip().title() or decision.strip().title() == 'Returning'.strip().title():
            return decision
        else:
            print("Sorry Pick Again")
def customer_main():
    print("\tHello Welcome To The Best Character Rental\n   Our Characters Are Guranteed To Rock The Kids Mental")

    input()

    decision = valid_decision()
    
    if decision.strip().title() == 'Renting'.strip().title():

        menu = loadinventory()
    
        brand = true_brand(menu)

        characters = true_character(menu, brand)

        time = valid_time()

        price = add_rental_fee(time, characters, menu)
        
        new_menu = change_inventory(characters,menu)

        update_inventory(new_menu)
        
        print("NO-REFUNDS")
        
        tax = round(add_tax(price), 2)
        
        deposit = find_deposit(characters, menu)
        
        new_cost = tax + price + deposit
        
        print("\tThat\'ll Be:\n Brand: {}\n\t_____\n Character: {}\n\t_____\n Time: {}hr\n Deposit: {}\n Price: {}\n Tax: {}\n Total: {:.2f}".format(brand, characters, int(time), deposit, price, tax, new_cost))
        
        log_rental(characters, time, new_cost)
    
    elif decision.strip().title() == 'Returning'.strip().title():
        
        menu = loadinventory()

        brand = return_brand(menu)

        character = return_character(menu, brand)
        
        new_menu = add_into_stock(character,menu)
        
        update_inventory(new_menu)
        
        deposit = find_deposit(character, menu)
        
        print("You\'re deposit was {:.2f} here is it back".format(deposit))

        print('\nThank You Please Rent With Us Again!')
        
        log_return(character, deposit)

def employee_main():
    
    name = true_name()
    actions = input("\nWhat Action Would You Like To Take:\n 1. All Transaction History\n 2. Restock\n 3. Character Transaction History\n 4. Total Revenue\n")

    if actions.strip() == '1'.strip():
        
        print(open_history())
   
    elif actions.strip() == '2'.strip():

        menu = loadinventory()

        brand = return_brand(menu)

        selection = give_character(menu, brand)

        character = input("\n{}\nWhat Character Would You Like To Restock?\n".format(selection))
            
        num = int(input("\nHow Many Will You Add\n"))

        new_menu = restock_character(character, menu, num)
        
        update_inventory(new_menu)
        
        print("The Action Was Completed")
    
    elif actions.strip() == '3'.strip():

        menu = loadinventory()

        brand = return_brand(menu)

        selection = give_character(menu, brand)
        
        character = input("\n{}\nWhat Character Would You Like To Look Up?\n".format(selection))
        
        history = load_history()
        
        print(get_history(character,history))
    
    elif actions.strip() == '4'.strip():
        history = load_history()
        print(round(find_revenue(history), 2))
    
    else:
        print("Sorry Start Over")
        employee_main()

def main():
    while True:
        choice = input("Are You an Employee or Customer?\n")
        if choice.strip().title() == "Employee".strip().title():
            employee_main()
            exit()
        elif choice.strip().title() == "Customer".strip().title():
            customer_main()
            exit()
        else:
            print("Invalid Choice")

if __name__ == '__main__':
    main()
