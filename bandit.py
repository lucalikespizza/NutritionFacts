import bandit
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

repo = "https://github.com/lucalikespizza/NutritionFacts"
driver.get(repo)

btns = driver.find_elements(By.CLASS_NAME , "react-directory-row undefined")

password = "jakshqiuhiuqh"
user = "admin"

def login(user, pw):
    print(f"User: {user} Password: {pw}")

login(user, password)

print(btns)

# Wenn eine Zeile angeklickt wurde
time.sleep(2)
if driver.current_url.endswith(".py"): 
    driver.get(driver.current_url.replace("https://github.com/", "https://raw.githubusercontent.com"))
time.sleep(2)
driver.back()

# Ende des Programms
print("Done.")
