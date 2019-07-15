guests = ["Juan", "Pedro", "Pablo"]
message = "is invited to dinner.\n"

guest = guests[0]
invite = f"{guest} {message}"
print(invite)

guest = guests[1]
invite = f"{guest} {message}"
print(invite)

guest = guests[2]
invite = f"{guest} {message}"
print(invite)

print("I found a bigger dinner table!")

guests.insert(0, "Matias")
guests.insert(2, "Miguel")
guests.append("Enrique")

guest = guests[0]
invite = f"{guest} {message}"
print(invite)

guest = guests[1]
invite = f"{guest} {message}"
print(invite)

guest = guests[2]
invite = f"{guest} {message}"
print(invite)

guest = guests[3]
invite = f"{guest} {message}"
print(invite)

guest = guests[4]
invite = f"{guest} {message}"
print(invite)

guest = guests[5]
invite = f"{guest} {message}"
print(invite)

print("I can only invite 2 people to dinner!")

popped = guests.pop()
print(f"I am sorry {popped}, I can not invite you to dinner")

popped = guests.pop()
print(f"I am sorry {popped}, I can not invite you to dinner")

popped = guests.pop()
print(f"I am sorry {popped}, I can not invite you to dinner")

popped = guests.pop()
print(f"I am sorry {popped}, I can not invite you to dinner")

print(f"{guests[0]} still invited")
print(f"{guests[1]} still invited")

del guests[1]
del guests[0]

print(guests)