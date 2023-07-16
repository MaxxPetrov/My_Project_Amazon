from datetime import datetime, timedelta
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService, Service
from time import sleep
from faker import Faker
from random import randint


Url = "https://form.123formbuilder.com/6479270/flight-attendant-job-application-form"
fake = Faker()

title = "//div[contains(text(),'Title')]"
initials = "//input[@type='text'][contains(@placeholder,'Initials')]"
f_name = "//input[@type='text'][contains(@placeholder,'First')]" or "//body/form[@id='form']/div[1]/div[2]/div[2]/div[1]/div[1]/input[1]"
middle = "//input[@type='text'][contains(@placeholder,'Middle')]"
l_name = "//body/form[@id='form']/div[1]/div[2]/div[2]/div[1]/div[2]/input[2]"
street_address = "//input[@placeholder='Street Address']"
street_address2 = "//input[@placeholder='Street Address Line 2']"
city = "//input[@placeholder='City']" 
region = "//input[@placeholder='Region']"
zipcode = "//input[@placeholder='Postal / Zip Code']"
country = "//input[@placeholder='Country']"
email = "//input[@type='email']"
DOB = "//div[contains(@data-role,'expander')]"
phone = "//input[@type='text'][contains(.,'Format 3 3 4')]"
mother_first = "(//input[contains(@data-role,'i123-input')])[12]"
c = "(//input[contains(@data-role,'i123-input')])[13]"
father_first = "(//input[contains(@data-role,'i123-input')])[14]"
father_last = "(//input[contains(@data-role,'i123-input')])[15]"
any_text1 = "//textarea[@id='textarea-00000018']"
any_text2 = "//textarea[@id='textarea-0000001a']"
apply_btn = "//span[contains(text(),'APPLY')]"


def fill_fields():
    inputs = drv.find_elements("tag name", "input")
    print(len(inputs), inputs)

    fields_data = {
        0: fake.first_name(),
        1: fake.last_name(),
        2: fake.email(),
        4: randint(1000000000, 9999999999),
        5: fake.street_address(),
        6: fake.building_number(),
        7: fake.city(),
        8: fake.state(),
        9: fake.postcode(),
        10: fake.first_name(),
    }
    index = 0
    for elem in inputs:
        elem.clear()
        print(index)
        elem.send_keys(fields_data[index])
        print(elem)
        index += 1
        sleep(5)

    sleep(10)
    return ()

    fields_data = {
        f_name: fake.first_name(),
        l_name: fake.last_name(),
        email: fake.email(),
        phone: randint(1000000000, 9999999999),
        street_address: fake.street_address(),
        street_address2: fake.building_number(),
        city: fake.city(),
        region: fake.state(),
        zipcode: fake.postcode(),
        mother_first: fake.first_name(),

    }

    for xpath, data in fields_data.items():
        drv.find_element("xpath", xpath).send_keys(data)
        drv.find_element()
        sleep(1)

    for key in fields_data.keys():
        print(key)

def calculate(x, y):
    print("Solution:")
    #201 code line
    print(x+y)

drv = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
drv.maximize_window()
drv.get(Url)
fill_fields()


calculate(234, 23432)
sleep(20)
# any code
calculate(23, 3423)
exit()


