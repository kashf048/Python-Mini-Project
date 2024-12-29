# Pseudocode for Alarm Program:
# Import Modules

# Import time, datetime, and pygame for sound playback.
# Define Function: set_alarm(alarm_time)

# Display a message indicating the alarm time.

# Define the sound file (Emergency_Alarm.mp3).

# Set is_running to True.

# While is_running is True:

# Get the current time in the format HH:MM:SS.
# Print the current time.
# If current time equals the alarm time:
# Print a "WAKE UP!" message.
# Initialize the pygame mixer.
# Load and play the alarm sound.
# While the sound is playing:
# Wait for 1 second.
# Set is_running to False.
# Wait for 1 second before checking the time again.
# Main Program

# Ask the user to input the alarm time in the format HH:MM:SS.
# Call the set_alarm function with the entered alarm time.

import time
import datetime
import pygame

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")
    sound_file = "Emergency_Alarm.mp3"
    is_running = True

    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)

        if current_time == alarm_time:
            print("WAKE UP! 😫")

            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                time.sleep(1)

            is_running = False

        time.sleep(1)


if __name__ == "__main__":
    alarm_time = input("Enter the alarm time (HH:MM:SS): ")
    set_alarm(alarm_time)