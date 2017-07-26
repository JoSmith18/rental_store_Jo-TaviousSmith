def loadinventory():
    with open("inventory.txt", "r") as inventory:
        key_1, key_2, key_3, key_4, key_5 = inventory.readline().strip().split(', ')
        characters = inventory.readlines()
    menu = []
    for item in characters:
        Brand, Character, Stock, Price, Rented = item.strip().split(', ')
        dictionary = {key_1: Brand, key_2: Character, key_3: float(Stock), key_4: float(Price), key_5: float(Rented)}
        menu.append(dictionary)
    return menu

def update_inventory(menu):
    message = 'Brand, Character, Stock, Price, Rented\n'
    for item in menu:
        message += '{}, {}, {}, {:.2f}, {}\n'.format(item["Brand"], item["Character"], float(item["Stock"]), float(item["Price"]), float(item["Rented"]))
    with open("inventory.txt", "w") as files:
        files.write(message)