from datetime import datetime, timedelta
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from time import sleep
from faker import Faker
from random import randint

URL = "https://form.123formbuilder.com/5012215"
fake = Faker()
# elements xpaths
f_name = "//body/form[@id='form']/div[1]/div[2]/div[1]/div[1]/div[1]/input[1]"
l_name = "//body/form[@id='form']/div[1]/div[2]/div[1]/div[1]/div[1]/input[2]"
email = "//body/form[@id='form']/div[1]/div[2]/div[2]/div[1]/div[1]/input[1]"
phone = "//body/form[@id='form']/div[1]/div[2]/div[3]/div[1]/div[1]/input[1]"
quantity = "//body/form[@id='form']/div[1]/div[2]/div[5]/div[1]/div[1]/div[1]/input[1]"
street = "//body/form[@id='form']/div[1]/div[2]/div[7]/div[1]/div[1]/input[1]"
street2 = "//body/form[@id='form']/div[1]/div[2]/div[7]/div[1]/div[2]/input[1]"
city = "//body/form[@id='form']/div[1]/div[2]/div[7]/div[1]/div[3]/input[1]"
region = "//body/form[@id='form']/div[1]/div[2]/div[7]/div[1]/div[3]/input[2]"
zipcode = "//body/form[@id='form']/div[1]/div[2]/div[7]/div[1]/div[4]/input[1]"
month = "//div[@id='date-00000012-month']"
day = "//div[@id='date-00000012-day']"
year = "//div[@id='date-00000012-year']"
country = "//body/form[@id='form']/div[1]/div[2]/div[7]/div[1]/div[4]/div[1]/input[1]"
country_check = "div[contains(text(),'Country')]"
check = ["//body/form[@id='form']/div[1]/div[2]/div[9]/div[1]/div[", "]/div[1]/label[1]/label[1]"]
check_input = "//body/form[@id='form']/div[1]/div[2]/div[9]/div[1]/div[4]/div[1]/input[1]"
dropdown = "//body/form[@id='form']/div[1]/div[2]/div[8]/div[1]/div[1]/div[1]/select[1]"
radio = ["//span[contains(text(),'# Product ", "')]"]
capcha = "//body/form[@id='form']/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]"
submit = "//span[contains(text(),'Submit order')]"


def fill_fields():
    fields_data = {
        f_name: fake.first_name(),
        l_name: fake.last_name(),
        email: fake.email(),
        phone: randint(1000000000, 9999999999),
        quantity: randint(1, 99999),
        street: fake.street_address(),
        street2: fake.building_number(),
        city: fake.city(),
        region: fake.state(),
        zipcode: fake.postcode()
    }

    print("FIELD DATA =", fields_data)
    print(type(fields_data))
    iter =0
    for xpath, data in fields_data.items():
        iter +=1
        print(iter)
        print(xpath, data)
        print(type(xpath), type(data))
        drv.find_element("xpath", xpath).send_keys(data)
        sleep(1)

    for key in fields_data.keys():
        print(key)

    exit()

def fill_date():
    date_ = fake.date_between_dates(datetime.now() + timedelta(1), datetime.now() + timedelta(100))
    date_ = {"month": [drv.find_element("xpath", month), date_.strftime("%m")],
             "day": [drv.find_element("xpath", day), date_.strftime("%d")],
             "year": [drv.find_element("xpath", year), date_.strftime("%Y")]
             }

    actions = ActionChains(drv)
    for d in date_.values():
        actions.move_to_element(d[0])
        actions.click()
        actions.send_keys(d[1])
    actions.perform()
    sleep(1)


def fill_country():
    actions = ActionChains(drv)
    actions.move_to_element(drv.find_element("xpath", country))
    actions.click()
    actions.send_keys(fake.country())
    actions.send_keys(Keys.TAB)
    actions.send_keys(Keys.PAGE_DOWN)
    actions.perform()
    sleep(1)
    try:
        drv.find_element("xpath", country_check)
        fill_country()
    except Exception:
        print("Country accepted")


def fill_radio():
    drv.find_element("xpath", radio[0] + str(randint(1, 6)) + radio[1]).click()


def fill_check():
    one = False
    for i in range(1, 5):
        if not randint(0, 1): continue
        one = True
        print(i)
        drv.find_element("xpath", check[0] + str(i) + check[1]).click()
        if i == 4:
            inp = drv.find_element("xpath", check_input)
            sleep(1)
            inp.send_keys(fake.word())
        sleep(1)
    if not one: return fill_check()


def fill_drop():
    select = Select(
        drv.find_element("xpath", dropdown))
    select.select_by_index(randint(0, 2))


def main():
    drv.get(URL)
    try:
        title = drv.title
        assert "Online Order Form" in drv.title
        print('Title Assertion test pass')
    except Exception as e:
        print('Title Assertion test failed', format(e))
    fill_fields()
    fill_date()
    fill_country()
    fill_radio()
    fill_drop()
    fill_check()
    drv.find_element("xpath", capcha).click()

    sleep(5)
    try:
        drv.find_element("xpath", submit).click()
    except:
        print("enter the capcha!!")
    sleep(10)
    drv.close()
    sleep(2)


if __name__ == "__main__":
    for n in range(1):
        print("Test :", n)
        drv = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        drv.maximize_window()
        try:
            main()
            print("Test", n, "- passed")
        except:
            print("Test", n, "- failed")