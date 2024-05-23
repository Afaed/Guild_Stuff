fruits = [
    'banana', 'cherry', 'melon', 'oranges', 'peach', 'plum', 
    'kiwi', 'grapes', 'mango', 'nectarine', 'fig', 'date', 
    'satsuma', 'pear', 'blueberry', 'apple'
]

vegetables = [
    'tomatoes', 'lettuce', 'carrots', 'bell pepper', 'onion', 
    'kale', 'spinach', 'beet', 'cucumber', 'eggplant', 'potato',
    'celery', 'argula', 'chickpeas', 'peas', 'leek', 'raddish', 'yam'
]

herbs = [
    'rosemary', 'garlic', 'mustard', 'pepper', 'bay leaves', 'basil', 
    'ginger', 'coriander', 'dill', 'marjoram', 'cinnamon', 'allspaice', 
    'cumin', 'mint', 'oregano', 'thyme', 'parsely', 'sage', 'tumeric',
    'salt'
]

default_prices = {
    'herb': 0.75,
    'vegetable': 2.85,
    'fruit': 1.50
}


def get_product(product_name: str, product_price: float, quantity: int=1) -> dict:
    """Return a product as a dictionary.

    :param product_name: name of the product
    :param product_price: price of the product
    :param quantity: quantity of product, defaults to 1
    :return: product
    """
    # your code here


def create_product_list(products: list) -> list[dict]:
    """Return a list of product dictionaries.
    
    Each product should have the appropriate default price.
    """
    # your code here


def calculate_cost(product: dict, quantity: int=1) -> float:
    # your code here


def get_receipt(products: list[dict], payment: float) -> dict:
    """Return a receipt as a dictionary.
    
    The receipt includes all products purchased. It also has 
    the total cost, payment tendered and the change (difference between the 
    cost and payment).
    """
    # your code here

