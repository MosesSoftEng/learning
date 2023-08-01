"""
Module that defines a Car class with defined __repr__ special method
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

    def __repr__(self) -> str:
        """
        Returns a debuggable string representation of the Car object.

        Returns:
            str: The string representation of the Car object.
        """
        return f"Car('{self.brand}', '{self.model}')"


# Create a Ferrari belinetta car object
belinetta: Car = Car("Ferrari", "belinetta")
belinetta_repr = repr(belinetta)

# Display debuggable string representation
#   of Ferrari belinetta car object.
print(belinetta_repr)

# Recreate Ferrari belinetta car object from
#   string representation using eval() function
belinetta_recreated: Car = eval(belinetta_repr)

print(belinetta_recreated.brand, belinetta_recreated.model)
