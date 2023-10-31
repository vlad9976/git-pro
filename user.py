def add_user(user):
    try:
        with open("user.txt", "w") as u:
            u.write(user)
    except FileNotFoundError:
        print("Error Writing To file")


