from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bandit.core.manager import BanditManager
from bandit.core.config import BanditConfig
from trufflehog3 import search as truf_search
from trufflehog3 import models
import time
import os
import sys

DEBUG = False
LOGGING = True

def debug(string):
    if DEBUG == True:
        print('\033[93m' + str(string) + '\033[0m')

def log(string):
    if LOGGING == True:
        print('\033[93m' + str(string) + '\033[0m')

<<<<<<< HEAD
def alert(string):
    print('\033[91m' + str(string) + '\033[0m')
=======
password = "jakshqiuhiuqh"
user = "admin"

def login(user, pw):
    print(f"User: {user} Password: {pw}")

login(user, password)

print(btns)
>>>>>>> 2af802080e4a9de2c6318fcd9bbe595482eac692

def scan_with_bandit(file_path):
    config = BanditConfig()
    manager = BanditManager(config, 'file')
    manager.discover_files([file_path], True)
    manager.run_tests()
    scan_results = manager.get_issue_list()
    for result in scan_results:
        if str(result).startswith("Issue: 'Possible hardcoded password:"):
            alert(result)

<<<<<<< HEAD
def scan_with_trufflehog(filePath):
    rule = models.Pattern(
        id="bad-password-letmein",
        message="Bad Password 'letmein'",
        pattern="password",
        severity="high",
        )
    file = models.File(
        path=filePath,
        )
    for issue in truf_search.search(file, [rule]):
        print(issue.context)


def scan_folder(backURL, start_y=1):
    debug("Neuer Aufruf von scan_folder()")
    time.sleep(1)
    try:
        textarea = driver.find_element(By.CSS_SELECTOR, "#read-only-cursor-text-area")
        log("I found a file: " + driver.current_url)

        # Saving File
        debug("Saving File....")
        with open("FileToScan", "w") as file:
            file.write(textarea.get_attribute("value"))
        
        log("Scanning File...")
        #scan_with_bandit("FileToScan")
        scan_with_trufflehog("FileToScan")

        debug("Done! Going back!")
        try:
            driver.get(backURL)
        except Exception as e:
            print(str(e))
    except:
        log("I am in a Folder: " + driver.current_url)
        for y in range(start_y, 30):  # Für jeden Ordner der aktuellen Liste
            try:
                # Gehe eine Ebene tiefer
                folder = driver.find_element(By.CSS_SELECTOR, f"#folder-row-{y} > td:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > a:nth-child(1)")
                foldername = folder.get_attribute("innerHTML")
                log(f"Now clicking: {foldername}")
                back = driver.current_url
                folder.click()

                # Starte Scan der neuen Ebene
                scan_folder(back)
                time.sleep(1)  # Optional, um dem Browser Zeit zum Laden zu geben

            except:  # Am Ende des Ordners angekommen
                driver.get(backURL)
                break  # Beende die Schleife, wenn ein Fehler auftritt

os.system("cls")
password = "iqwfdq17268_testpasswort"
#username = "Kamillendampf"

username = input("GitHub Username: ")

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument("--log-level=3")

driver = webdriver.Chrome(options=chromeOptions)
driver.get(f'https://github.com/{username}?tab=repositories')

# Die Repos 1 bis 200 durchgehen
for x in range(1, 200): # Übersicht aller Repos
    try:
        repo = driver.find_element(By.CSS_SELECTOR, f"li.col-12:nth-child({x}) > div:nth-child(1) > div:nth-child(1) > h3:nth-child(1) > a:nth-child(1)")
        log(f"Klicke Repo #{x} an.")
        back = driver.current_url
        repo.click()
        time.sleep(5)

        scan_folder(back)

    except:
        log("Done!")
        driver.quit()
        input("Press ENTER to exit...")
        sys.exit(0)

# Hier ein PW im Code, dass es gefunden werden kann
password = "18r&§2n38)=/n23@mur"
user = "admin"

print(f"User {user} has password {password}")
=======
# Ende des Programms
print("Done.")
>>>>>>> 2af802080e4a9de2c6318fcd9bbe595482eac692
