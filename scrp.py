import pyautogui
from time import sleep

#Ask for the channel name
channel_name = pyautogui.prompt(text="", title="Enter the Channel name")

#Open Chrome
pyautogui.press("win")  # Open start menu
sleep(2)
pyautogui.write("chrome")
sleep(2)
pyautogui.press("enter")  # Open Chrome
sleep(3)  # Wait for Chrome to open

#Open YouTube
pyautogui.hotkey("ctrl", "t")  # New tab
sleep(2)
pyautogui.write("https://www.youtube.com/")
pyautogui.press("enter")
sleep(3)

#Locate and click the search bar
x, y = pyautogui.locateCenterOnScreen("search.png", confidence=0.8)
pyautogui.moveTo(x, y, duration=1)
pyautogui.click()

#Type and search for the channel
sleep(2)
pyautogui.write(channel_name)
pyautogui.press("enter")
sleep(3)

#Click on the channel logo
x, y = pyautogui.locateCenterOnScreen("logo.png", confidence=0.9)
pyautogui.moveTo(x, y, duration=1)
pyautogui.click()

# Step 7: Click the Subscribe button
sleep(2)
x, y = pyautogui.locateCenterOnScreen("subscribe.png", confidence=0.9)
pyautogui.moveTo(x, y, duration=1)
pyautogui.click()
