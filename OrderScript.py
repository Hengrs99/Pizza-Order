from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

PATH = "C:\Program Files (x86)\chromedriver"
driver = webdriver.Chrome(PATH)
driver.maximize_window()
driver.get("https://www.pizzafantastico.cz/")

filterButtonXPATH = "/html/body/div[4]/div/div[8]/div[5]/div[5]/button"
pizzaXPATH = "/html/body/div[4]/div/div[8]/div[5]/div[6]/div[11]/div[1]/a/div/div[2]/h4"
addToBasketButtonXPATH = "/html/body/div[4]/div/div[8]/div[8]/div[1]/div/div[4]/input[1]"
goToBasketButtonXPATH = "/html/body/div[4]/div/div[6]/div[1]/div[4]/div[2]/a"
continueButtonXPATH = "/html/body/div[4]/div/div[8]/div[6]/div/div[6]/div[1]/div[4]/div[2]/a"
continueButton2XPATH = "/html/body/div[4]/div/div[8]/div[10]/div[1]/div[4]/div/div[5]/div[2]/a"
continueButton3XPATH = "/html/body/div[4]/div/div[8]/form/div[1]/div[1]/div[2]/div/div[7]/div[2]/a"
toggleButtonXPATH = "/html/body/div[4]/div/div[8]/form/div[2]/div[1]/div[1]/div/div[7]/div[2]/label/div"


city = driver.find_element_by_class_name("js-multiapp-link")
city.click()

try:
    filterButton = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, filterButtonXPATH))
    )

    filterButton.click()

    searchField = driver.find_element_by_id("filter-name-input")
    searchField.send_keys("Salámová")
    searchField.send_keys(Keys.RETURN)

    pizza = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, pizzaXPATH))
    )

    pizza.click()

    addToBasketButton = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, addToBasketButtonXPATH))
    )

    addToBasketButton.click()

    goToBasketButton = driver.find_element_by_xpath(goToBasketButtonXPATH)
    goToBasketButton.click()

    time.sleep(3)

    continueButton = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, continueButtonXPATH))
    )

    continueButton.click()

    continueButton2 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, continueButton2XPATH))
    )

    continueButton2.click()

    continueButton3 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, continueButton3XPATH))
    )

    continueButton3.click()

    name = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "name"))
    )

    name.send_keys("Petr")
    surname = driver.find_element_by_id("surmane")
    surname.send_keys("Jeřábek")
    email = driver.find_element_by_id("email")
    email.send_keys("hengrs99@seznam.cz")
    telephone = driver.find_element_by_id("telephone")
    telephone.send_keys("736601539")

    toggleButton = driver.find_element_by_xpath(toggleButtonXPATH)
    toggleButton.click()

except:
    driver.quit()