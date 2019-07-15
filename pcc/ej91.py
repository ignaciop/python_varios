class Restaurant():
    def __init__(self, name, type):
        self.restaurant_name = name
        self.cuisine_type = type
        
    def describe_restaurant(self):
        print(f"{self.restaurant_name} is of type {self.cuisine_type}")
        
    def open_restaurant(self):
        print(f"{self.restaurant_name} is open!")
        
res = Restaurant("Plaza del Carmen", "variado")
print(res.restaurant_name)
print(res.cuisine_type)
res.describe_restaurant()
res.open_restaurant()
        