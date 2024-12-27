# Python compound interest calculator

# Get Principle Amount:
# Ask the user to input the principal amount.
# If the principal is less than 0, display an error message and ask again.
# Get Interest Rate:
# Ask the user to input the interest rate.
# If the rate is less than 0, display an error message and ask again.
# Get Time:
# Ask the user to input the time in years.
# If the time is less than 0, display an error message and ask again.
# Calculate Total Balance:
# Use the formula:
# Total=Principal×(1+Rate100)Time\text{Total} = \text{Principal} \times (1 + \frac{\text{Rate}}{100})^{\text{Time}}Total=Principal×(1+100Rate​)Time
# Display the total balance after the given time.


principle = 0
rate = 0
time = 0

while True:
    principle = float(input('Enter the principle amount: '))
    if principle < 0:
        print("Principle can't be less than zero")
    else:
        break

while True:
    rate = float(input('Enter the interest rate: '))
    if rate < 0:
        print("Interest rate can't be less than zero")
    else:
        break

while True:
    time = int(input('Enter the time in year: '))
    if time < 0:
        print("Time can't be less than zero")
    else:
        break

total = principle * pow((1 + rate / 100), time)
print(f"Balance after {time} year/s : ${total:.2f}")