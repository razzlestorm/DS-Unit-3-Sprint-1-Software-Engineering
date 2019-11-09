
from random import randint, uniform
from acme import Product

# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    """generate a given number of products (default
      30), randomly, and return them as a list"""
    products = []
    for ii in range(num_products):
        prod_name = (
                    f'{ADJECTIVES[randint(0, len(ADJECTIVES)-1)]} '
                    f'{NOUNS[randint(0, len(NOUNS)-1)]}'
                    )
        prod_price = randint(5, 100)
        prod_weight = randint(5, 100)
        prod_flammability = uniform(0.0, 2.5)
        products.append(Product(prod_name, price=prod_price,
                        weight=prod_weight, flammability=prod_flammability))
    return products


def inventory_report(products):
    """takes a list of products, and prints a "nice" summary"""
    '''For the report, you should calculate and print the following values:

    - Number of unique product names in the product list
    - Average (mean) price, weight, and flammability of listed products'''
    nameset = set()
    total_price = 0
    total_weight = 0
    total_flammability = 0.0
    for product in products:
        nameset.add(product.name)
        total_price += product.price
        total_weight += product.weight
        total_flammability += product.flammability
    print("ACME CORPORATION OFFICIAL INVENTORY REPORT")
    print(f"Unique product names: {len(nameset)}")
    print(f"Average price: {total_price / len(products)}")
    print(f"Average weight: {total_weight / len(products)}")
    print(f"Averge flammability: {total_flammability / len(products)}")


if __name__ == '__main__':
    inventory_report(generate_products())
