class Property:
    def __init__(self, area: float, rooms: int, price: float, address: str):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address
class House(Property):
    def __init__(self, area: float, rooms: int, price: float, address: str, plot: int):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return f"House at {self.address}, Area: {self.area} sqm, Rooms: {self.rooms}, Price: ${self.price}, Plot size: {self.plot} sqm"

class Flat(Property):
    def __init__(self, area: float, rooms: int, price: float, address: str, floor: int):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return f"Flat at {self.address}, Area: {self.area} sqm, Rooms: {self.rooms}, Price: ${self.price}, Floor: {self.floor}"

house1 = House(120.5, 4, 250000, "123 Main St", 500)
flat1 = Flat(80.0, 3, 150000, "456 Elm St", 2)
print(house1)
print(flat1)