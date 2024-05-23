import random 

from main import *


def test_create_product_success() -> None:
    result = get_product('banana', 1.12)
    expected = {'name': 'banana', 'price': 1.12, 'quantity': 1}
    if not result == expected:
        print('Test create_product: ❌')
    else:
        print('Test create_product: ✅')


def test_create_product_list_success() -> None:
    result = create_product_list(['banana'])
    expected = [get_product('banana', default_prices['fruit'])]
    if not result == expected:
        print('Test create_product_list: ❌')
    else:
        print('Test create_product_list: ✅')


def test_calculate_payment_success() -> None:
    result = calculate_cost(get_product('apples', 1.25), 2)
    expected = 2.50
    if not result == expected:
        print('Test calculate_payment: ❌')
    else:
        print('Test calculate_payment: ✅')


if __name__ == '__main__':
    test_create_product_success()
    test_create_product_list_success()
    test_calculate_payment_success()
