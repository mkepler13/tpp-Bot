import random
import time
import win32api
import win32con

# List of words
words = ["UP", "DOWN", "LEFT", "RIGHT"]
#words = ["UP", "DOWN", "LEFT", "RIGHT", "START"] 

# Function to type a word and press Enter, then type 'a' and press Enter
def type_word(word):
    for letter in word:
        win32api.keybd_event(ord(letter), 0, 0, 0)  # Key down
        win32api.keybd_event(ord(letter), 0, win32con.KEYEVENTF_KEYUP, 0)  # Key up
    win32api.keybd_event(win32con.VK_RETURN, 0, 0, 0)  # Press Enter
    win32api.keybd_event(win32con.VK_RETURN, 0, win32con.KEYEVENTF_KEYUP, 0)  # Release Enter
    time.sleep(1)  # Wait for X seconds
    win32api.keybd_event(ord('A'), 0, 0, 0)  # Key down 'A'
    win32api.keybd_event(ord('A'), 0, win32con.KEYEVENTF_KEYUP, 0)  # Key up 'A'
    win32api.keybd_event(win32con.VK_RETURN, 0, 0, 0)  # Press Enter
    win32api.keybd_event(win32con.VK_RETURN, 0, win32con.KEYEVENTF_KEYUP, 0)  # Release Enter
    time.sleep(1)  # Wait for X seconds

# Main loop
while True:
    # Choose a random word
    random_word = random.choice(words)
    # Type the word and 'a', then wait
    type_word(random_word)
