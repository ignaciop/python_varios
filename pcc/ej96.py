class Restaurant():
    def __init__(self, name, type):
        self.restaurant_name = name
        self.cuisine_type = type
        
    def describe_restaurant(self):
        print(f"{self.restaurant_name} is of type {self.cuisine_type}")
        
    def open_restaurant(self):
        print(f"{self.restaurant_name} is open!")

class IceCreamStand(Restaurant):
    def __init__(self, name, flavors):
        super().__init__(name, "Ice Cream Stand")
        self.flavors = flavors
        
    def show_flavors(self):
        print(f"{self.restaurant_name} has the following flavors:\n")
        
        for f in self.flavors:
            print(f"\t{f}\n")
            
res = Restaurant("Plaza del Carmen", "variado")
res.describe_restaurant()
res.open_restaurant()

ics = IceCreamStand("Fortunato", ["Frutilla", "Vainilla", "Maracuya"])
ics.describe_restaurant()
ics.open_restaurant()
ics.show_flavors()        