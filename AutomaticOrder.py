from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
import time
import unidecode

loc1XPATH = "/html/body/div[2]/div[5]/a[1]"
loc2XPATH = "/html/body/div[2]/div[5]/a[2]"
loc3XPATH = "/html/body/div[2]/div[5]/a[3]"
understandButtonXPATH = "/html/body/div[4]/div/div[8]/div[5]/div[7]/button"
filterButtonXPATH = "/html/body/div[4]/div/div[8]/div[5]/div[5]/button"
rawPizzaHeaderXPATH = "/html/body/div[4]/div/div[8]/div[5]/div[6]/div[0]/div[1]/a/div/div[2]/h4"
addToBasketButtonXPATH = "/html/body/div[4]/div/div[8]/div[8]/div[1]/div/div[4]/input[1]"
goToBasketButtonXPATH = "/html/body/div[4]/div/div[6]/div[1]/div[4]/div[2]/a"
continueButtonXPATH = "/html/body/div[4]/div/div[8]/div[6]/div/div[6]/div[1]/div[4]/div[2]/a"
continueButton2XPATH = "/html/body/div[4]/div/div[8]/div[10]/div[1]/div[4]/div/div[5]/div[2]/a"
continueButton3XPATH = "/html/body/div[4]/div/div[8]/form/div[1]/div[1]/div[2]/div/div[7]/div[2]/a"
toggleButtonXPATH = "/html/body/div[4]/div/div[8]/form/div[2]/div[1]/div[1]/div/div[7]/div[2]/label/div"

loc1 = "Roztoky"
loc2 = "Děčín"
loc3 = "Příbram"

pizzaTypes = ["margherita", "syrova", "sunkova", "capricciosa", "hawaii", "olivova", "marinara", "tunakova",
              "vegetariana", "salamova", "zampionova", "americana", "dabelska", "fantastico", "farmarska", "sedlacka",
              "kureci", "crudo", "brusinkova exclusive", "provensalska exclusive", "albori exclusive",
              "kureci special exclusive"]


def wait_for_element_xpath(element_name, element_xpath):
    try:
        return (WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, element_xpath))
        ))

    except:
        print("Error: couldn't click on --> " + element_name)
        driver.quit()


def wait_for_element_id(element_name, element_id):
    try:
        return (WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.ID, element_id))
        ))

    except:
        print("Error: couldn't click on --> " + element_name)
        driver.quit()


def treat_user_input(input_text):
    modifiedInput = unidecode.unidecode(input(input_text)).lower()
    return modifiedInput


def announce_invalid_info(invalid_info):
    print("Invalid " + invalid_info)
    time.sleep(1)
    print()


def prepare_default_order():
    global locXPATH
    global selectedPizza
    global personalInfo

    locXPATH = loc1XPATH
    selectedPizza = ask_for_pizza_name()

    personalInfo = ["Petr", "Jeřábek", "hengrs99@seznam.cz", "736601539"]


def prepare_custom_order():
    global locXPATH
    global selectedPizza
    global personalInfo

    locXPATH = find_loc_xpath()
    selectedPizza = ask_for_pizza_name()

    print()

    personalInfo = [ask_for_personal_info("name"), ask_for_personal_info("surname"), ask_for_personal_info("e-mail"),
                    ask_for_personal_info("phone number")]


def ask_for_personal_info(info_type):
    info = input("Enter your " + info_type + ": ")

    treat_personal_info_input(info, info_type)
    return info


def treat_personal_info_input(info, info_type):
    if info_type == "e-mail":
        if info.find("@") == -1:
            announce_invalid_info("email")
            ask_for_personal_info("email")
    elif info_type == "phone number":
        for char in info:
            if not char.isdigit():
                announce_invalid_info("phone number")
                ask_for_personal_info("phone number")

        if len(info) > 9 or len(info) < 9:
            announce_invalid_info("phone number")
            ask_for_personal_info("phone number")


def set_up_order():
    orderType = treat_user_input("Enter type of order (default/custom): ")

    if orderType == "default" or orderType == "" or orderType == "1":
        prepare_default_order()
    elif orderType == "custom" or orderType == "2":
        prepare_custom_order()
    else:
        announce_invalid_info("order type")
        set_up_order()


def find_loc_xpath():
    global locXPATH

    loc = treat_user_input("Enter shop location (" + loc1 + "/" + loc2 + "/" + loc3 + "): ")

    if loc == unidecode.unidecode(loc1).lower() or loc == "1":
        locXPATH = loc1XPATH
    elif loc == unidecode.unidecode(loc2).lower() or loc == "2":
        locXPATH = loc2XPATH
    elif loc == unidecode.unidecode(loc3).lower() or loc == "3":
        locXPATH = loc3XPATH
    elif loc == "":
        locXPATH = loc1XPATH
    else:
        announce_invalid_info("location")
        find_loc_xpath()

    return locXPATH
# TODO This method should be separated to ask_for_loc() and find_loc_xpath()


def ask_for_pizza_name():
    global isPizzaValid

    wantedPizza = treat_user_input("Enter pizza name: ")
    for pizza in pizzaTypes:
        if pizza == wantedPizza:
            isPizzaValid = True
    if isPizzaValid:
        return wantedPizza
    else:
        announce_invalid_info("pizza name")
        ask_for_pizza_name()


def find_pizza_xpath():
    for pizza in pizzaTypes:
        if pizza == selectedPizza:
            return rawPizzaHeaderXPATH.replace(rawPizzaHeaderXPATH[47], str(pizzaTypes.index(pizza) + 2))


set_up_order()

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
# TODO Pizza sometimes doesn't show up, needs to be fixed
pizzaHeader.click()

addToBasketButton = wait_for_element_xpath("addToBasketButton", addToBasketButtonXPATH)
# TODO User should be able to choose amount of pizzas he wants
addToBasketButton.click()

goToBasketButton = driver.find_element_by_xpath(goToBasketButtonXPATH)
goToBasketButton.click()

time.sleep(3)

continueButton = wait_for_element_xpath("continueButton", continueButtonXPATH)
continueButton.click()

continueButton2 = wait_for_element_xpath("continueButton2", continueButton2XPATH)
# TODO User should be able to choose where he wants to pick up pizza (home or shop)
continueButton2.click()

continueButton3 = wait_for_element_xpath("continueButton3", continueButton3XPATH)
# TODO User should be able to pay either with cash or online
continueButton3.click()

name = wait_for_element_id("name", "name")
name.send_keys(personalInfo[0])

surname = driver.find_element_by_id("surmane")
surname.send_keys(personalInfo[1])

email = driver.find_element_by_id("email")
email.send_keys(personalInfo[2])

telephone = driver.find_element_by_id("telephone")
telephone.send_keys(personalInfo[3])

toggleButton = driver.find_element_by_xpath(toggleButtonXPATH)
toggleButton.click()
