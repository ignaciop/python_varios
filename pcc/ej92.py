class Restaurant():
    def __init__(self, name, type):
        self.restaurant_name = name
        self.cuisine_type = type
        
    def describe_restaurant(self):
        print(f"{self.restaurant_name} is of type {self.cuisine_type}")
        
    def open_restaurant(self):
        print(f"{self.restaurant_name} is open!")
        
res1 = Restaurant("Plaza del Carmen", "variado")
res2 = Restaurant("San Carlos", "pizzeria")
res3 = Restaurant("Pedro 94", "pescaderia")

res1.describe_restaurant()
res2.describe_restaurant()
res3.describe_restaurant()        