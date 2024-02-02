import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login(driver, username, password, website):
    driver.get(f"{website}/login")
    driver.maximize_window()
    driver.find_element(By.ID, 'name').send_keys(username)
    driver.find_element(By.ID, 'password').send_keys(password)
    driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/div/button').click()

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

    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/div/div/div/button'))).click()

def main():
    driver = webdriver.Edge()
    website = 'http://localhost:5173'
    choice = input("Enter 1 to test login or 2 to test signup: ")
    if choice == "1":
        username = "yahiaa05"
        password = "AdminAdmin123@"
        test_login(driver, username, password, website)
        time.sleep(5)
    elif choice == "2":
        username = 'testuser'
        email = 'ab@gmail.com'
        password = 'password123'
        test_signup(driver, username, email, password, website)
        time.sleep(5)
    else:
        print("Invalid choice")

    driver.quit()

if __name__ == "__main__":
    main()
