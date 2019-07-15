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

print(f"{guest} can not make it")

guests.remove('Pablo')
guests.append("Lucas")

print(guests)

guest = guests[0]
invite = f"{guest} {message}"
print(invite)

guest = guests[1]
invite = f"{guest} {message}"
print(invite)

guest = guests[2]
invite = f"{guest} {message}"
print(invite)