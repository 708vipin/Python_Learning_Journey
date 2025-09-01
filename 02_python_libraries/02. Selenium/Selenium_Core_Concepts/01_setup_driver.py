"""
01_setup_driver.py
-------------------
This script demonstrates how to set up and launch a Selenium WebDriver.
We will use Chrome browser with webdriver-manager to handle driver installation.
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Setup Chrome WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open a webpage
driver.get("https://www.python.org")

# Print the page title
print("Page Title:", driver.title)

# Close the browser
driver.quit()
