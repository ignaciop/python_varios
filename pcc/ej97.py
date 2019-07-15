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
        
class Admin(User):
    def __init__(self, first_name, last_name, age, sex, privileges = []):
        super().__init__(first_name, last_name, age, sex)
        self.privileges = Privileges(privileges)
        
        
class Privileges():
    def __init__(self, privileges):
        self.privileges = privileges
        
    def show_privileges(self):
        print(f"{self.privileges}")
        

user1 = User("Pablo", "Perez", 34, "Male")
user2 = Admin("Maria", "Gonzalez", 65, "Female", ["can add post", "can ban user"])
user3 = Admin("Juan", "Lopez", 32, "Male")


user1.describe_user()
user2.describe_user()
user3.describe_user()
user1.greet_user()
user2.greet_user()
user3.greet_user()
user2.privileges.show_privileges()
user3.privileges.show_privileges()