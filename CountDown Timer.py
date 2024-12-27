# Count Down Timer

# Input: Ask the user to enter the time in seconds.
# Loop:
# Start from the entered time and count down to 0.
# For each value:
# Calculate the seconds using x%60x \% 60x%60.
# Calculate the minutes using int(x/60)%60\text{int}(x / 60) \% 60int(x/60)%60.
# Calculate the hours using int(x/3600)\text{int}(x / 3600)int(x/3600).
# Display the time in the format HH:MM:SS.
# Wait for 1 second.
# Output: Once the countdown reaches 0, print "HAPPY NEW YEAR 🎉🎉🎉".

import time

my_time = int(input('Enter the time in seconds: '))

for x in range(my_time, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f'{hours:02}:{minutes:02}:{seconds:02}')
    time.sleep(1)

print("HAPPY NEW YEAR🎉🎉🎉")

