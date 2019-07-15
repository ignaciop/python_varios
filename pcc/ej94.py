class Restaurant():
    def __init__(self, name, type, number_served = 0):
        self.restaurant_name = name
        self.cuisine_type = type
        self.number_served = number_served
        
    def describe_restaurant(self):
        print(f"{self.restaurant_name} is of type {self.cuisine_type} and has served {self.number_served} customers")
        
    def open_restaurant(self):
        print(f"{self.restaurant_name} is open!")
        
    def set_number_served(self, number):
        self.number_served = number
        
    def increment_number_served(self):
        self.number_served += 150
        
res = Restaurant("Plaza del Carmen", "variado")
res.describe_restaurant()
res.open_restaurant()

res.number_served = 150
print(res.number_served)
res.describe_restaurant()
        
res.set_number_served(470)
res.describe_restaurant()

res.increment_number_served()
res.describe_restaurant()