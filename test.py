import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def test_login(driver, username, password, website):
    driver.get(f"{website}/login")
    driver.maximize_window()
    driver.find_element(By.ID, 'name').send_keys(username)
    driver.find_element(By.ID, 'password').send_keys(password)
    driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/div/button').click()

    try:
        alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert_text = alert.text

        if alert_text == "Wrong Login ! Try again...":
            print("Test failed: Wrong Login ! Try again...")
        else:
            print("Test passed: Alert text does not match expected message")
        
        alert.accept()
    except TimeoutException:
        print("Test passed: No alert was raised")

def test_signup(driver, username, email, password, website):
    driver.get(f"{website}/signup")
    driver.maximize_window()

    driver.find_element(By.ID, 'username').clear()
    driver.find_element(By.ID, 'username').send_keys(username)

    driver.find_element(By.ID, 'email').clear()
    driver.find_element(By.ID, 'email').send_keys(email)

    driver.find_element(By.ID, 'password').clear()
    driver.find_element(By.ID, 'password').send_keys(password)

    driver.find_element(By.ID, 'confirmPassword').clear()
    driver.find_element(By.ID, 'confirmPassword').send_keys(password)

    driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/div/button').click()

    try:
        alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert_text = alert.text

        if alert_text == "Could not signup user for some reason!":
            print("Test failed: User already exists!")
        else:
            print("Test passed: Alert text does not match expected message")
        
        alert.accept()
    except TimeoutException:
        print("Test passed: No alert was raised")

def remove_from_favorite(driver, website):
    test_login(driver, "admin", "123456", website)
    time.sleep(5)
    driver.get(f"{website}/settings")
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/table/tbody/tr/td[2]/button'))).click()

    alert = WebDriverWait(driver, 5).until(EC.alert_is_present())

    alert_text = alert.text

    if alert_text == "Deleted article from favorite list successfully!":
        print("it works!")
    else:
        print("Alert text does not match")

    alert.accept()
def add_to_favorite(driver, website):
    test_login(driver, "admin", "123456", website)
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/div/button'))).click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/ul/li[2]/button'))).click()

    alert = WebDriverWait(driver, 5).until(EC.alert_is_present())

    alert_text = alert.text

    if alert_text == "Added to favorites!":
        print("it works!")
    else:
        print("Alert text does not match")

    alert.accept()



def add_to_menu():
    print("Enter 1 to test login")
    print("Enter 2 to test signup")
    print("Enter 3 to add to favorite")
    print("Enter 4 to remove from favorite")

def main():
    driver = webdriver.Edge()
    website = 'http://localhost:5173'
    choice = '1'
    # input("Enter your choice: ")
    if choice == "1":
        username = "admin"
        password = "123456"
        test_login(driver, username, password, website)
        time.sleep(5)
    elif choice == "2":
        username = 'testuser'
        email = 'ab@gmail.com'
        password = 'password123'
        test_signup(driver, username, email, password, website)
        time.sleep(5)
    elif choice == "3":
        add_to_favorite(driver, website)
        time.sleep(5)
    elif choice == "4":
        remove_from_favorite(driver, website)
        time.sleep(5)
    else:
        print("Invalid choice")

    driver.quit()

if __name__ == "__main__":
    main()
