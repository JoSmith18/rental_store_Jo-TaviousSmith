from core import *

def test_give_brand():
    assert give_brand([{'Brand': 'Marvel', 'Character': 'IronMan', 'Stock': 4, 'Price': 85.00, 'Rented': 0, 'Value': 430}, {'Brand': 'Disney', 'Character': 'daffy', 'Stock': 4, 'Price': 85.00, 'Sold': 0}], 'Marvel') == 'Character: IronMan, Deposit: 43.0, Price: 85.00\n'

def test_selection_of_brand():
    assert selection_of_brand([{'Brand': 'Marvel', 'Character': 'IronMan', 'Stock': 4, 'Price': 85.00, 'Sold': 0}, {'Brand': 'Disney', 'Character': 'daffy', 'Stock': 4, 'Price': 85.00, 'Sold': 0}]) == {'Marvel', 'Disney'}

def test_rental_fee():
    assert add_rental_fee(2, 'IronMan', [{'Brand': 'Marvel', 'Character': 'IronMan', 'Stock': 4, 'Price': 85.00, 'Sold': 0}, {'Brand': 'Disney', 'Character': 'daffy', 'Stock': 4, 'Price': 85.00, 'Sold': 0}]) == 170.00

def test_add_tax():
    assert add_tax(70) == 4.9

def test_change_inventory():
    assert change_inventory('IronMan', [{'Brand': 'Marvel', 'Character': 'IronMan', 'Stock': 4, 'Price': 85.00, 'Rented': 0}, {'Brand': 'Disney', 'Character': 'daffy', 'Stock': 4, 'Price': 85.00, 'Rented': 0}]) == [{'Brand': 'Marvel', 'Character': 'IronMan', 'Stock': 3, 'Price': 85.00, 'Rented': 1}, {'Brand': 'Disney', 'Character': 'daffy', 'Stock': 4, 'Price': 85.00, 'Rented': 0}]

def test_verify_brand():
    assert verify_brand({'Marvel', 'Disney', 'SpongeBob'}, 'D.C') == False
    assert verify_brand({'Marvel', 'Disney', 'SpongeBob'}, 'Disney') == True

def test_find_deposit():
    assert find_deposit('IronMan', [{'Brand': 'Marvel', 'Character': 'IronMan', 'Stock': 3, 'Price': 85.00, 'Rented': 1, 'Value': 430}, {'Brand': 'Disney', 'Character': 'daffy', 'Stock': 4, 'Price': 85.00, 'Rented': 0, 'Value': 230}]) == 430 * .10

def test_add_into_stock():
    assert add_into_stock('IronMan',[{'Brand': 'Marvel', 'Character': 'IronMan', 'Stock': 3, 'Price': 85.00, 'Rented': 1, 'Value': 430}, {'Brand': 'Disney', 'Character': 'daffy', 'Stock': 4, 'Price': 85.00, 'Rented': 0, 'Value': 230}]) == [{'Brand': 'Marvel', 'Character': 'IronMan', 'Stock': 4, 'Price': 85.00, 'Rented': 1, 'Value': 430}, {'Brand': 'Disney', 'Character': 'daffy', 'Stock': 4, 'Price': 85.00, 'Rented': 0, 'Value': 230}]

def test_restock_character():
    assert restock_character("IronMan", [{'Brand': 'Marvel', 'Character': 'IronMan', 'Stock': 3, 'Price': 85.00, 'Rented': 1, 'Value': 430}, {'Brand': 'Disney', 'Character': 'daffy', 'Stock': 4, 'Price': 85.00, 'Rented': 0, 'Value': 230}], 10) == [{'Brand': 'Marvel', 'Character': 'IronMan', 'Stock': 13, 'Price': 85.00, 'Rented': 1, 'Value': 430}, {'Brand': 'Disney', 'Character': 'daffy', 'Stock': 4, 'Price': 85.00, 'Rented': 0, 'Value': 230}]