from random import randint


class Product:
    """
    An ACME Product

    Parameters
    ----------
    - `name` (string)
        no default
    - `price` (integer)
        default value 10
    - `weight` (integer)
        default value 20
    - `flammability` (float)
        default value 0.5
    - `identifier` (integer)
        automatically genererated as a random (uniform) number
        anywhere from 1000000 to 9999999, includisve)(inclusive).
    """
    def __init__(self, name, price=10, weight=20, flammability=0.5,
                 identifier=randint(1000000, 9999999)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def stealability(self):
        """
        Calculates the price divided by the weight, and then returns a message.

        Returns
        -------
        A message string indicating how stealable.
        """
        stealable = self.price / self.weight
        message = str
        if stealable < 0.5:
            message = "Not so stealable..."
        elif stealable >= 1.0:
            message = "Very stealable!"
        else:
            message = "Kinda stealable."
        return message

    def explode(self):
        """
        Calculates the flammability times the weight and returns a message.

        Returns
        -------
        A message string indicating explode level.
        """
        explodable = self.flammability * self.weight
        if explodable < 10:
            message = "...fizzle."
        elif explodable >= 50:
            message = "...BABOOM!!"
        else:
            message = "...boom!"
        return message


class BoxingGlove(Product):
    """
    A Subclass exclusivley for ACME boxing gloves
    """
    def __init__(self, name, price=10, weight=10, flammability=0.5,
                 identifier=randint(1000000, 9999999)):
        Product.__init__(self, name, price, weight, flammability)

    def stealability(self):
        """
        Calculates the price divided by the weight, and then returns a message.

        Returns
        -------
        A message string indicating how stealable.
        """
        stealable = self.price / self.weight
        message = str
        if stealable < 0.5:
            message = "Not so stealable..."
        elif stealable >= 1.0:
            message = "Very stealable!"
        else:
            message = "Kinda stealable."
        return message

    def explode(self):
        """
        Boxing gloves are non-explodeable.

        Returns
        -------
        A message string indicating explode level.
        """
        message = "...it's a glove."
        return message

    def punch(self):
        """
        A calculates punch severity.

        Returns
        -------
        A message string indicating punch severity.
        """
        if self.weight < 5:
            message = "That tickles."
        elif self.weight >= 15:
            message = "OUCH!"
        else:
            message = "Hey that hurt!"
        return message
