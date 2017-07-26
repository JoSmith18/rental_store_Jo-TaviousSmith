def give_brand(menu, brand):
    characters = ''
    for item in menu:
        if item["Brand"] == brand:
            characters += ('Character: {}, Price: {:.2f}\n'.format(item["Character"], item["Price"]))
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
      
        
            
        

    