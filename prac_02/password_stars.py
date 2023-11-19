min_password_length = 8

while True:
    password = str(input("Enter a password: "))
    if len(password) < min_password_length:
        print(f"Invalid input")
    else:
        break

print("*" * len(password))



