def give_brand(menu, brand):
    """ [{}], '' -> ['']
    >>> give_brand([{'Brand': 'Marvel', 'Character': 'IronMan', 'Stock': 4, 'Price': 85.00, 'Sold': 0}, {'Brand': 'Disney', 'Character': 'daffy', 'Stock': 4, 'Price': 85.00, 'Sold': 0}], 'Marvel')
    'Character: IronMan, Price: 85.00\n'
    """
    characters = ''
    for item in menu:
        if item["Brand"] == brand:
            characters += ('Character: {}, Price: {:.2f}\n'.format(item["Character"], item["Price"]))
    return characters