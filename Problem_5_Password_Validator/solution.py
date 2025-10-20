# Ask for name and password
name = input("Enter your name: ")
password = input("Enter your password: ")

#  Initialize checks
errors = []

# Length check (at least 8 characters)
if len(password) < 8:
    errors.append("Password must be at least 8 characters long.")

#  Check for at least one digit
if not any(char.isdigit() for char in password):
    errors.append("Password must contain at least one digit.")

#  Password should not be the same as the name
if password.lower() == name.lower():
    errors.append("Password should not be the same as your name.")

# Output results
if not errors:
    print("Password is strong ")
else:
    print("Password is weak ")
    print("Reasons:")
    for error in errors:
        print(f"- {error}")
