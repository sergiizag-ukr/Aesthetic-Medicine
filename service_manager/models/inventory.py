from dataclasses import dataclass


@dataclass
class Inventory:
    name: str
    quantity: int
    price: float

    def total_value(self):
        return self.quantity * self.price

    def is_low_stock(self, threshold):
        return self.quantity < threshold

    def display(self):
        return (
            f"{self.name} | "
            f"Quantity: {self.quantity} | "
            f"Price: {self.price} грн"
        )