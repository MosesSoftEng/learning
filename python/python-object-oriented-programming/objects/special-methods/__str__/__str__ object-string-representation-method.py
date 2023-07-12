"""
Module that defines a Car class without defined __str__ special method.
"""


class Car:
    """
    A class representing a car object.

    Attributes:
        brand (str): The brand or manufacturer of the car.
        model (str): The model name of the car.
    """

    def __init__(self, brand: str, model: str) -> None:
        """
        Initializes a Car object with the specified brand and model.

        Args:
            brand (str): The brand or manufacturer of the car.
            model (str): The model name of the car.
        """
        self.brand: str = brand
        self.model: str = model


# Create a Ferrari belinetta car object
belinetta: Car = Car("Ferrari", "belinetta")

# Display default human-readable string representation
#   of Ferrari belinetta car object.
print(str(belinetta))

# or

print(belinetta)
