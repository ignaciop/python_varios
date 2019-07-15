guests = ["Juan", "Pedro", "Pablo"]
message = "is invited to dinner.\n"

guest = guests.pop(0)
invite = f"{guest} {message}"
print(invite)

guest = guests.pop(0)
invite = f"{guest} {message}"
print(invite)

guest = guests.pop()
invite = f"{guest} {message}"
print(invite)
