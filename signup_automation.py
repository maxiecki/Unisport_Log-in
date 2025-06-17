import pyautogui
import pyperclip
import time
from datetime import datetime, timedelta
# Coordinates via https://www.sportangebot.uni-bonn.de/angebote/aktueller_zeitraum/_Volleyball.html#T121901
# 
# for Wendsday (early): 1537, 690
# for Wendsday (late): 1548, 797
# for Thursday: 
# for Friday: 
# for Sunday: 

# Define the target time
def get_target_time():
    # Get the current date and time
    now = datetime.now()

    # Set the target time for today at 7:00:10 AM
    target_time_today = datetime(now.year, now.month, now.day,7, 0, 5)

    # If it's already past 7:00:10 AM today, schedule it for the next day
    if now >= target_time_today:
        target_time_tomorrow = target_time_today + timedelta(days=1)
        return target_time_tomorrow
    else:
        return target_time_today     

# Get the current time and calculate the difference to the target time
now = datetime.now()
target_time = get_target_time()

# Calculate the time difference in seconds
time_difference = (target_time - now).total_seconds()

# Wait until the target time
print("Control coordinates for the day")
print(f"Current time: {now}")
print(f"Waiting until: {target_time} ({time_difference} seconds from now)")
time.sleep(time_difference)

print("Executing code now")
# Executing code now 


time.sleep(5)
pyautogui.hotkey("ctrl", "t") # new tab
pyperclip.copy("https://www.sportangebot.uni-bonn.de/angebote/aktueller_zeitraum/_Volleyball.html#T121901")
pyautogui.hotkey("ctrl", "v")
pyautogui.press('enter')
time.sleep(2)

pyautogui.moveTo(1537, 690) # Coordinates of the day
pyautogui.click()
time.sleep(2)

pyautogui.press('tab')
pyautogui.press('enter')
time.sleep(2)

pyautogui.moveTo(845, 655) # Move to Log in with password
pyautogui.click()
time.sleep(1)

pyautogui.moveTo(810, 710) # Move to Email
pyautogui.click()
pyperclip.copy("s14mecka@uni-bonn.de") # Email here
pyautogui.hotkey("ctrl", "v")
pyautogui.press('tab')
pyautogui.write('') # Password here
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('enter')
time.sleep(1)

pyautogui.moveTo(388, 179)
pyautogui.click()

pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('space')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('enter')
time.sleep(1)
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('enter')
