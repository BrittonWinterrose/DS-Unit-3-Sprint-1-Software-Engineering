import random
from acme import Product

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', 'Panda']


def generate_products(number_of_products=30):
    """
    Generates the product data entries for n number of products.

    Parameters
    ----------
    number_of_products: int
        An interger indicating the number of products to create.

    Returns
    ---------
    generated_products: list
        A list of each Product's attributes in sub-lists.
    """
    generated_products = []
    adjs = ADJECTIVES
    nouns = NOUNS
    for i in range(number_of_products):
        p_createdid = i
        p_name = random.choice(adjs) + " " + random.choice(nouns)
        p_price = random.randint(5, 100)
        p_weight = random.randint(5, 100)
        p_flammability = random.uniform(0.0, 2.5)
        prod = Product(name=p_name, price=p_price, weight=p_weight,
                       flammability=p_flammability)
        theftable = prod.stealability()
        generated_products.append([p_name, p_price, p_weight, p_flammability,
                                   theftable, p_createdid])
    return generated_products


def inventory_report(product_list):
    """
    Prints the product data report for product list attributes.

    Parameters
    ----------
    product_list: int
        A list of each Product's attributes in sub-lists.

    Output
    ------
    Prints the report.
    """
    names = []
    prices = []
    weights = []
    flammabilitys = []
    theftability = []
    for i in product_list:
        names.append(i[0])
        prices.append(i[1])
        weights.append(i[2])
        flammabilitys.append(i[3])
        theftability.append(i[4])
    print("ACME CORP OFFICIAL INVENTORY REPORT")
    print("Unique Product Names: ", len(set(names)))
    print("Average Price: ", sum(prices) / float(len(prices)))
    print("Average Weight: ", sum(weights) / float(len(weights)))
    print("Average Flammability: ",
          sum(flammabilitys) / float(len(flammabilitys)))
    print("Unique Theft Levels: ", len(set(theftability)))

if __name__ == '__main__':
    inventory_report(generate_products())
