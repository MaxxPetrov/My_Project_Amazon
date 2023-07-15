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
mother_lat = "(//input[contains(@data-role,'i123-input')])[13]"
father_first = "(//input[contains(@data-role,'i123-input')])[14]"
father_last = "(//input[contains(@data-role,'i123-input')])[15]"
any_text1 = "//textarea[@id='textarea-00000018']"
any_text2 = "//textarea[@id='textarea-0000001a']"
apply_btn = "//span[contains(text(),'APPLY')]"


def fill_fields():
    fields_data = {
        f_name: fake.first_name(),
        l_name: fake.last_name(),
        email: fake.email(),
        phone: randint(1000000000, 9999999999),
        street_address: fake.street_address(),
        street_address2: fake.building_number(),
        city: fake.city(),
        region: fake.state(),
        zipcode: fake.postcode()
    }

    for xpath, data in fields_data.items():
        drv.find_element("xpath", xpath).send_keys(data)
        sleep(1)

    for key in fields_data.keys():
        print(key)


    exit()


