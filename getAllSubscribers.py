# Import necessary modules and packages
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import loginInfo

# Initialize the Firefox browser
browser = webdriver.Firefox()

# Open Instagram website
browser.get("https://www.instagram.com/")

# Pause for 5 seconds to allow page to load
time.sleep(5)

# Find the username and password input fields
username = browser.find_element(By.NAME, "username")
password = browser.find_element(By.NAME, "password")

# Enter the login information from the loginInfo module
username.send_keys(loginInfo.username)
password.send_keys(loginInfo.password)

# Find and click the login button
loginButton = browser.find_element(By.XPATH, "/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button")
loginButton.click()

# Pause for 15 seconds to allow login and redirect
time.sleep(10)

# Find and click the profile button
profileButton = browser.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[8]/div/div/a")
profileButton.click()

# Pause for 5 seconds to allow profile page to load
time.sleep(5)

# Find and click the followings button
followingsButton = browser.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[3]/a") 
followingsButton.click()

# Pause for 5 seconds to allow followings list to load
time.sleep(5)

# JavaScript code to scroll to the bottom of the followings list
jscommand = """
    followings = document.querySelector("._aano") 
    followings.scrollTo(0, followings.scrollHeight) 
    var lenOfPage=followings.scrollHeight;
    return lenOfPage;
"""

# Execute the JavaScript code to scroll to the bottom of the followings list
lenOfPage = browser.execute_script(jscommand)

match = False

# Scroll until the end of the followings list is reached
while match == False:

    # Set the length of the page to the lastCount variable 
    lastCount = lenOfPage

    # Pause for 1 second before checking scroll position again
    time.sleep(1)

    # Execute the JavaScript code to check the scroll position
    lenOfPage = browser.execute_script(jscommand)

    if lastCount == lenOfPage:
        
        # If the scroll could not go any further, set the match variable as True and end the loop
        match = True

# Pause for 5 seconds to allow the followings list to load completely
time.sleep(5)

# Define an empty followingsList
followingsList = []

# Find all following elements and extract the text
followings = browser.find_elements(By.CSS_SELECTOR, ".x9f619.xjbqb8w.x1rg5ohu.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1n2onr6.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.x1q0g3np.xqjyukv.x6s0dn4.x1oa3qoh.x1nhvcw1")

for following in followings:

    # Add all following elements in the followings to the followingsList
    followingsList.append(following.text)

# Write the followings list to a file
with open("followings.txt", "w", encoding = "utf-8") as file:

    for following in followingsList:

        file.write(following + "\n")

# Close the browser
browser.close()




