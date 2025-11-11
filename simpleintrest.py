# simple_interest.py
# Program to calculate Simple Interest

# Taking user input
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time (in years): "))

# Calculating Simple Interest
simple_interest = (principal * rate * time) / 100

# Displaying the result
print(f"\nSimple Interest = {simple_interest:.2f}")
