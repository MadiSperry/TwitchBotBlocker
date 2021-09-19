'''
This semi-automatic code is designed to open twitch.tv in a browser in order to ban 
some known follower and viewer bots.
Input: None
Output: Ban messages to twitch chat and to terminal to ensure the program is working properly
Author: MadiSperry
'''

# Organize imports
from selenium import webdriver
from time import sleep

# CONFIG VARIABLES
# Your Personal Account Info
username = ""
password = ""
# Other Config Variables
streamerUsername = ""   #This is the username of the streamer you want to block these bots for(You must be a moderator for this streamer)
directory = "" # The folder where the text file is located
delay = 5

# Define remaining variables
website = "https://www.twitch.tv/"
counter = 0

# Open browser, maximize the window, and open website
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(website)

# Delay for the page to fully load
sleep(delay)

# Locate and click the login button
logInButton = browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/nav/div/div[3]/div[3]/div/div[1]/div[1]/button')
logInButton.click()

# Delay of 1 second for the buttons on the login page to load
sleep(1)

# Locate the usernameBox and passwordBox
usernameBox = browser.find_element_by_xpath('//*[@id="login-username"]')
passwordBox = browser.find_element_by_xpath('//*[@id="password-input"]')

# Send Personal Information to the usernameBox and passwordBox and hit enter
usernameBox.send_keys(username)
passwordBox.send_keys(password + "\n")

# Delay to allow time for user to manually pass 2-Factor Auth.
sleep(45)           # Recommended delay = 30-60

# Open the requested streamer's channel. If streamer is offline, there
# will be a button that says "Chat" that needs to be clicked before the delay ends
browser.get(website + streamerUsername)

# Delay in case streamer is offline and "Chat" needs to be clicked
sleep(delay)

# Defines the chatBox for this program to click in
chatBox = browser.find_element_by_tag_name('textarea')

# Opens the file in a read-only format and names it 'f'
f = open(directory + "banlist.txt", "r")

# Creates a loop where for every username in the file 'f', 
# the command "/ban [username]" is ran with a short delay between commands
delay = 0.1         # Recommended delay = 0.1
for username in f:
    chatBox.send_keys("/ban " + username)
    print("Banning: " + username)
    counter += 1
    sleep(delay)

# Creates a banMessage
banMessage = "Banned " + str(counter) + " Follower and Viewer bots!\n"

# Sends the above banMessage to the chatBox and to terminal
chatBox.send_keys(banMessage)
print(banMessage)

# Creates a short delay before closing the browser to allow time for message to be read before closing
sleep(10)
browser.close()
