class User():
    def __init__(self, first_name, last_name, age, sex):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
        
    def describe_user(self):
        print(f"{self.first_name} {self.last_name} is a {self.age} years old {self.sex}")
        
    def greet_user(self):
        print(f"Welcome, {self.first_name} {self.last_name}!")
        
user1 = User("Pablo", "Perez", 34, "Male")
user2 = User("Maria", "Gonzalez", 65, "Female")

user1.describe_user()
user2.describe_user()
user1.greet_user()
user2.greet_user()