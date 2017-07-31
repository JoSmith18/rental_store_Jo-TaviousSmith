def give_brand(menu, brand):
    """ [{}], '' -> ''
    Takes in menu and brand and return a string 
    of the characters of that brand in menu
    >>> give_brand([{'Brand': 'Marvel', 'Character': 'IronMan', 'Stock': 4, 'Price': 85.00, 'Rented': 0, 'Value': 430}, {'Brand': 'Disney', 'Character': 'daffy', 'Stock': 4, 'Price': 85.00, 'Sold': 0}], 'Marvel')
    'Character: IronMan, Deposit: 43.0, Price: 85.00\\n'
    >>> give_brand([{'Brand': 'Marvel', 'Character': 'IronMan', 'Stock': 4, 'Price': 85.00, 'Rented': 0, 'Value': 430}, {'Brand': 'Marvel', 'Character': 'Hulk', 'Stock': 4, 'Price': 85.00, 'Rented': 0, 'Value': 430}], 'Disney')
    ''
    """
    characters = ''
    for item in menu:
        if item["Brand"] == brand and item["Stock"] >= 1:
            characters += ('\tCharacter: {}, Deposit: {}, Price: {:.2f}\n'.format(item["Character"], (item["Value"] * .10), item["Price"]))
    return characters

def selection_of_brand(menu):
    """ [{}] -> set('')
    Takes in the menu and return a set of brands in the menu
    >>> selection_of_brand([{'Brand': 'Marvel', 'Character': 'IronMan', 'Stock': 4, 'Price': 85.00, 'Rented': 0, 'Value': 430}])
    {'Marvel'}
    >>> selection_of_brand([{'Brand': 'Marvel', 'Character': 'IronMan', 'Stock': 4, 'Price': 85.00, 'Rented': 0, 'Value': 430}, {'Brand': 'Disney', 'Character': 'daffy', 'Stock': 4, 'Price': 85.00, 'Sold': 0}]) == {'Marvel', 'Disney'}
    True
    """
    brand = set()
    for item in menu:
        brand.add(item["Brand"])
    return brand

def add_rental_fee(time,characters,menu):
    """ (int,str,[{}]) -> int
    Takes a int, str, and list of dict
    returns an int of multiplying the 
    price * the time of that character found in menu
    >>> add_rental_fee(2, 'IronMan',[{'Brand': 'Marvel', 'Character': 'IronMan', 'Stock': 4, 'Price': 85.00, 'Rented': 0, 'Value': 430}])
    170.0
    >>> add_rental_fee(0, 'IronMan',[{'Brand': 'Marvel', 'Character': 'IronMan', 'Stock': 4, 'Price': 85.00, 'Rented': 0, 'Value': 430}])
    0.0
    """
    for item in menu:
        if item["Character"] == characters:
             price = item["Price"] * time
    return price

def get_history(character, history):
    """ (str, [{}]) -> [{}]
    Takes in a str and list of dict
    and returns the log of that str
    >>> get_history('IronMan',[{'Character': 'IronMan', 'Time': 3, 'Total': 165.45}]) == [{'Character': 'IronMan', 'Time': 3, 'Total': 165.45}]
    True
    >>> get_history('Cinderella',[{'Character': 'IronMan', 'Time': 3, 'Total': 165.45}])
    []
    """
    character_history = []
    for item in history:
        if character == item["Character"] :
            character_history.append(item)
    return character_history


def add_tax(price):
    """ int -> float
    Takes a price and returns the multiplication
    of that int * .07
    >>> add_tax(1)
    0.07
    >>> add_tax(0)
    0.0
    """
    return price * .07

def change_inventory(characters, menu):
    """ (str,[{}]) -> [{}]
    Takes a character and menu and returns
    that charcter stock(-1) and rent(+1) changed
    >>> change_inventory('IronMan',[{'Brand': 'Marvel', 'Character': 'IronMan', 'Stock': 4, 'Price': 85.00, 'Rented': 0, 'Value': 430}]) == [{'Brand': 'Marvel', 'Character': 'IronMan', 'Stock': 3, 'Price': 85.00, 'Rented': 1, 'Value': 430}]
    True
    """
    for item in menu:
        if characters == item["Character"]:
            item["Stock"] -= 1
            item["Rented"] += 1
    return (menu)

def verify_brand(validbrand, brand):
    """ (set(),str) -> bool
    Returns True if brand is in validbrand
    >>> verify_brand({'Marvel'}, 'Disney')
    False
    >>> verify_brand({'Marvel'}, 'Marvel')
    True
    """
    if brand in validbrand:
        return True
    else:
        return False

def find_deposit(characters,menu):
    """ (str,[{}]) -> float
    Look for characters in menu and 
    Return the multiplication of values and .10
    >>> find_deposit('IronMan',[{'Brand': 'Marvel', 'Character': 'IronMan', 'Stock': 4, 'Price': 85.00, 'Rented': 0, 'Value': 430}])
    43.0
    >>> find_deposit('IronMan',[{'Brand': 'Marvel', 'Character': 'IronMan', 'Stock': 4, 'Price': 85.00, 'Rented': 0, 'Value': 0}])
    0.0
    """
    for item in menu:
        if characters == item["Character"]:
            return item["Value"] * .10

def add_into_stock(character, menu):
    """ (str,[{}]) -> [{}]
    Looks for character in menu
    Return the menu with stock + 1
    >>> add_into_stock('IronMan',[{'Brand': 'Marvel', 'Character': 'IronMan', 'Stock': 4, 'Price': 85.00, 'Rented': 0, 'Value': 430}]) == [{'Brand': 'Marvel', 'Character': 'IronMan', 'Stock': 5, 'Price': 85.00, 'Rented': 0, 'Value': 430}]
    True
    >>> add_into_stock('IronMan',[{'Brand': 'Marvel', 'Character': 'IronMan', 'Stock': 4, 'Price': 85.00, 'Rented': 0, 'Value': 430}]) == [{'Brand': 'Marvel', 'Character': 'IronMan', 'Stock': 3, 'Price': 85.00, 'Rented': 0, 'Value': 430}]
    False
    """
    for item in menu:
        if character == item["Character"]:
            item["Stock"] += 1
    return menu

def restock_character(character, menu, num):
    """ (str,[{}],int) -> [{}]
    Looks for charcter in menu
    Returns menu with the sum 
    of num and the stock
    >>> restock_character('IronMan',[{'Brand': 'Marvel', 'Character': 'IronMan', 'Stock': 4, 'Price': 85.00, 'Rented': 0, 'Value': 430}], 2)== [{'Brand': 'Marvel', 'Character': 'IronMan', 'Stock': 6, 'Price': 85.00, 'Rented': 0, 'Value': 430}]
    True
    >>> restock_character('IronMan',[{'Brand': 'Marvel', 'Character': 'IronMan', 'Stock': 4, 'Price': 85.00, 'Rented': 0, 'Value': 430}], 2)== [{'Brand': 'Marvel', 'Character': 'IronMan', 'Stock': 2, 'Price': 85.00, 'Rented': 0, 'Value': 430}]
    False
    """
    for item in menu:
        if character == item["Character"]:
            item["Stock"] += int(num)
    return menu

def find_revenue(history):
    """ [{}] -> float
    Takes history and Return the sum of the totals
    >>> find_revenue([{'Character': 'IronMan', 'Time': 3, 'Total': 165.45},{'Character': 'IronMan', 'Time': 3, 'Total': -165.45}])
    0.0
    >>> find_revenue([{'Character': 'IronMan', 'Time': 3, 'Total': 165.45}])
    165.45
    """
    values=[]
    for items in history:
        values.append(items["Total"])
    return sum(values)

def valid_name(name):
    return name.strip().isalpha()
        
    
        
        


      
        
            
        

    