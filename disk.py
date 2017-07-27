from datetime import *
def loadinventory():
    with open("inventory.txt", "r") as inventory:
        key_1, key_2, key_3, key_4, key_5, key_6 = inventory.readline().strip().split(', ')
        characters = inventory.readlines()
    menu = []
    for item in characters:
        Brand, Character, Stock, Price, Rented, Value = item.strip().split(', ')
        dictionary = {key_1: Brand, key_2: Character, key_3: int(Stock), key_4: float(Price), key_5: float(Rented), key_6: float(Value)}
        menu.append(dictionary)
    return menu

def update_inventory(menu):
    message = 'Brand, Character, Stock, Price, Rented, Value\n'
    for item in menu:
        message += '{}, {}, {}, {:.2f}, {}, {:.2f}\n'.format(item["Brand"], item["Character"], int(item["Stock"]), float(item["Price"]), int(item["Rented"]), float(item["Value"]))
    with open("inventory.txt", "w") as files:
        files.write(message)

def log_rental(Characters, time, total):
    with open("history.txt", "a") as history:
        history.write('\n{}, {}hr, {:.2f}'.format(Characters, time, total))

def log_return(character, deposit):
    with open("history.txt", "a") as history:
        today = datetime.now()
        history.write('\n{}, {}, -{}'.format(character, today.strftime('%H:%M:%S'), deposit))

def open_history():
    with open("history.txt", "r") as log:
        history = log.read()
    return history

def load_history():
    with open("history.txt", "r") as log:
        key_1, key_2, key_3 = log.readline().strip().split(', ')
        history = log.readlines()
    loaded = []
    for item in history:
        Character, Time, Total = item.strip().split(', ')
        dictionary = {key_1: Character, key_2: int(Time), key_3: float(Total)}
        loaded.append(dictionary)
    return loaded 