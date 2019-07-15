class User():
    def __init__(self, first_name, last_name, age, sex):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
        self.login_attempts = 0
        
    def describe_user(self):
        print(f"{self.first_name} {self.last_name} is a {self.age} years old {self.sex}")
        
    def greet_user(self):
        print(f"Welcome, {self.first_name} {self.last_name}!")
        
    def increment_login_attempts(self):
        self.login_attempts += 1
        
    def reset_login_attempts(self):
        self.login_attempts = 0
        
user1 = User("Pablo", "Perez", 34, "Male")

user1.increment_login_attempts()
print(user1.login_attempts)
user1.increment_login_attempts()
print(user1.login_attempts)
user1.increment_login_attempts()
print(user1.login_attempts)

user1.reset_login_attempts()
print(user1.login_attempts)