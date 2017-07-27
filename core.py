def give_brand(menu, brand):
    characters = ''
    for item in menu:
        if item["Brand"] == brand and item["Stock"] >= 1:
            characters += ('Character: {}, Deposit: {}, Price: {:.2f}\n'.format(item["Character"], (item["Value"] * .10), item["Price"]))
    return characters

def selection_of_brand(menu):
    """ [{}] -> set()
    """
    brand = set()
    for item in menu:
        brand.add(item["Brand"])
    return brand

def add_rental_fee(time,characters,menu):
    for item in menu:
        if item["Character"] == characters:
             price = item["Price"] * time
    return price

def add_tax(price):
    return price * .07

def change_inventory(characters, menu):
    for item in menu:
        if characters == item["Character"]:
            item["Stock"] -= 1
            item["Rented"] += 1
    return (menu)

def verify_brand(validbrand, brand):
    if brand in validbrand:
        return True
    else:
        return False

def find_deposit(characters,menu):
    for item in menu:
        if characters == item["Character"]:
            return item["Value"] * .10

def add_into_stock(character, menu):
    for item in menu:
        if character == item["Character"]:
            item["Stock"] += 1
    return menu

def restock_character(character, menu, num):
    for item in menu:
        if character == item["Character"]:
            item["Stock"] += num
    return menu



      
        
            
        

    