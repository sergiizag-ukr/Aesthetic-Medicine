from dataclasses import dataclass

@dataclass
class Service:
    name: str
    price: float
    duration_minutes: int

    def price_per_hour(self):
        return self.price / (self.duration_minutes / 60)

    def formatted(self):
        return f"{self.name} - {self.price} грн. {self.duration_minutes} хв."