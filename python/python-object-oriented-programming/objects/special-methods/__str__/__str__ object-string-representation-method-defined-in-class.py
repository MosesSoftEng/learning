"""
Module that defines a Car class with defined __str__ special method.
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

    def __str__(self) -> str:
        """
        Returns a human-readable string representation of the Car object.

        Returns:
            str: The string representation of the Car object.
        """
        return f"{self.model} is a {self.brand} model."


# Create a Ferrari belinetta car object
belinetta: Car = Car("Ferrari", "belinetta")

# Display default human-readable string representation
#   of Ferrari belinetta car object.
print(str(belinetta))

# or

print(belinetta)
