# your code here
age = int(input("Enter your age: "))
has_license = input("Do you have a valid driver's license? (yes/no): ").strip().lower()

# Step 2: Use nested if/else to check eligibility
if age >= 18:
    if has_license == "yes":
        # Step 3: Print result
        print("You are eligible for the role.")
    else:
        print("You are not eligible: You must have a valid driver's license.")
else:
    print("You are not eligible: You must be at least 18 years old.")
