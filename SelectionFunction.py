from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
import unidecode
import time

locXPATH = "/html/body/div[2]/div[5]/a[1]"
understandButtonXPATH = "/html/body/div[4]/div/div[8]/div[5]/div[7]/button"
filterButtonXPATH = "/html/body/div[4]/div/div[8]/div[5]/div[5]/button"
rawPizzaHeaderXPATH = "/html/body/div[4]/div/div[8]/div[5]/div[6]/div[0]/div[1]/a/div/div[2]/h4"

pizzaTypes = ["margherita", "syrova", "sunkova", "capricciosa", "hawaii", "olivova", "marinara", "tunakova",
              "vegetariana", "salamova", "zampionova", "americana", "dabelska", "fantastico", "farmarska", "sedlacka",
              "kureci", "crudo", "brusinkova exclusive", "provensalska exclusive", "albori exclusive",
              "kureci special exclusive"]


def ask_for_pizza_name():
    global isPizzaValid
    wantedPizza = unidecode.unidecode(input("Enter pizza name: ")).lower()
    for pizza in pizzaTypes:
        if pizza == wantedPizza:
            isPizzaValid = True
    if isPizzaValid:
        return wantedPizza
    else:
        print("Invalid pizza name")
        time.sleep(1)
        print()
        ask_for_pizza_name()


def find_pizza_xpath():
    for pizza in pizzaTypes:
        if pizza == selectedPizza:
            return rawPizzaHeaderXPATH.replace(rawPizzaHeaderXPATH[47], str(pizzaTypes.index(pizza) + 2))


def wait_for_element_xpath(element_name, element_xpath):
    try:
        return (WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, element_xpath))
        ))

    except:
        print("Error: couldn't click on --> " + element_name)
        driver.quit()


selectedPizza = ask_for_pizza_name()

PATH = "C:\Program Files (x86)\chromedriver"
driver = webdriver.Chrome(PATH)
driver.maximize_window()
driver.get("https://www.pizzafantastico.cz/")

city = driver.find_element_by_xpath(locXPATH)
city.click()

understandButton = wait_for_element_xpath("understandButton", understandButtonXPATH)
understandButton.click()

filterButton = wait_for_element_xpath("filterButton", filterButtonXPATH)
filterButton.click()

searchField = driver.find_element_by_id("filter-name-input")
searchField.send_keys(selectedPizza)
searchField.send_keys(Keys.RETURN)

pizzaHeaderXPATH = find_pizza_xpath()

pizzaHeader = wait_for_element_xpath("pizzaHeader", pizzaHeaderXPATH)
pizzaHeader.click()
