''' using while loop to keep asking for a username if the
one provided isn't valid '''

real_username = "Kirlin"

print("Welcome to Real_Hostel discovery")
print("Type your username: ")
username = input()

while username != real_username:
    print("Invalid username." + "\n" + "Type correct username." )
    username = input()

print("Welcome, " + username + "!")
