import time
from faker import Faker
import unittest
import requests
from selenium.common.exceptions import WebDriverException as WDE
from selenium.webdriver import Keys
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.edge.service import Service
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import amazon_help as HP

fake = Faker()


class ChromeSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def test_amazon_create_login(self):
        driver = self.driver
        driver.get(HP.main_url)
        time.sleep(3)
        HP.check_API_code()
        wait = WebDriverWait(driver, 3)
        HP.assert_title(driver, "Amazon.com. Spend less. Smile more.")

        driver.find_element(By.ID, "nav-link-accountList").click()
        driver.find_element(By.ID, "createAccountSubmit").click()
        driver.find_element(By.ID, "ap_customer_name").send_keys(fake.name())
        driver.find_element(By.ID, "ap_email").send_keys(fake.email())

        fakepassword = fake.password()
        driver.find_element(By.ID, "ap_password").send_keys(fakepassword)

        # password_confirm
        driver.find_element(By.ID, "ap_password_check").send_keys(fakepassword)
        driver.find_element(By.ID, "continue").click()
        HP.assert_title(driver, "Authentication required")
        print("Login process is working")

        # go back on 3 pages
        driver.execute_script("window.history.go(-3)")
        time.sleep(3)
        acct_reg_expected_title = "Amazon.com. Spend less. Smile more."
        acct_reg_actual_title = driver.title
        if acct_reg_expected_title == acct_reg_actual_title:
            print('"Account registration" page Title is correct:', driver.title)
        else:
            print('"Account registration" page Title is wrong:', driver.title)

        driver.quit()

    def test_negative_login(self):
        driver = self.driver
        driver.get(HP.main_url)
        time.sleep(3)
        wait = WebDriverWait(driver, 3)
        HP.assert_title(driver, "Amazon.com. Spend less. Smile more.")

        # verifying if user can create account without paswords
        driver.find_element(By.ID, "nav-link-accountList").click()
        driver.find_element(By.ID, "createAccountSubmit").click()
        driver.find_element(By.ID, "ap_customer_name").send_keys(fake.name())
        driver.find_element(By.ID, "ap_email").send_keys(fake.email())
        fakepassword = fake.password()
        driver.find_element(By.ID, "ap_password").send_keys(fakepassword)
        driver.find_element(By.ID, 'continue').click()
        time.sleep(5)
        n = driver.find_element(By.ID, "auth-password-missing-alert")
        print(n, n.text)

        if n.text == "Minimum 6 characters required":
            print("Error message 'Minimum 6 characters required' present")
        else:
            print("Failed:No Minimum 6 characters required present")

    def tearDown(self):
        self.driver.quit()


class EdgeSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        self.driver.maximize_window()

    def test_amazon_create_login(self):
        driver = self.driver
        driver.get(HP.main_url)
        time.sleep(3)
        wait = WebDriverWait(driver, 3)
        HP.assert_title(driver, "Amazon.com. Spend less. Smile more.")

        driver.find_element(By.ID, "nav-link-accountList").click()
        driver.find_element(By.ID, "createAccountSubmit").click()
        driver.find_element(By.ID, "ap_customer_name").send_keys(fake.name())
        driver.find_element(By.ID, "ap_email").send_keys(fake.email())

        fakepassword = fake.password()
        driver.find_element(By.ID, "ap_password").send_keys(fakepassword)

        # password_confirm
        driver.find_element(By.ID, "ap_password_check").send_keys(fakepassword)
        driver.find_element(By.ID, "continue").click()
        HP.assert_title(driver, "Authentication required")
        print("Login process is working")

        # go back on 3 pages
        driver.execute_script("window.history.go(-3)")
        time.sleep(3)
        acct_reg_expected_title = "Amazon.com. Spend less. Smile more."
        acct_reg_actual_title = driver.title
        if acct_reg_expected_title == acct_reg_actual_title:
            print('"Account registration" page Title is correct:', driver.title)
        else:
            print('"Account registration" page Title is wrong:', driver.title)

        driver.quit()

    def test_negative_login(self):
        driver = self.driver
        driver.get(HP.main_url)
        time.sleep(3)
        wait = WebDriverWait(driver, 3)
        HP.assert_title(driver, "Amazon.com. Spend less. Smile more.")

        # verifying if user can create account without paswords
        driver.find_element(By.ID, "nav-link-accountList-nav-line-1").click()
        driver.find_element(By.ID, "createAccountSubmit").click()
        driver.find_element(By.ID, "ap_customer_name").send_keys(fake.name())
        driver.find_element(By.ID, "ap_email").send_keys(fake.email())
        driver.find_element(By.ID, 'continue').click()
        n = driver.find_element(By.XPATH, "//div[@class='a-alert-content'][contains(.,'Minimum 6 characters')]")
        if n == driver.find_element(By.XPATH,
                                    "//div[@class='a-alert-content'][contains(.,'Minimum 6 characters')]"):
            print("Error message 'Minimum 6 characters required' present")
        else:
            print("Failed:No Minimum 6 characters required present")

    def tearDown(self):
        self.driver.quit()


class FirefoxSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        self.driver.maximize_window()

    def test_amazon_create_login(self):
        driver = self.driver
        driver.get(HP.main_url)
        time.sleep(3)
        wait = WebDriverWait(driver, 3)
        HP.assert_title(driver, "Amazon.com. Spend less. Smile more.")

        driver.find_element(By.ID, "nav-link-accountList").click()
        driver.find_element(By.ID, "createAccountSubmit").click()
        driver.find_element(By.ID, "ap_customer_name").send_keys(fake.name())
        driver.find_element(By.ID, "ap_email").send_keys(fake.email())

        fakepassword = fake.password()
        driver.find_element(By.ID, "ap_password").send_keys(fakepassword)

        # password_confirm
        driver.find_element(By.ID, "ap_password_check").send_keys(fakepassword)
        driver.find_element(By.ID, "continue").click()
        HP.assert_title(driver, "Authentication required")
        print("Login process is working")

        # go back on 3 pages
        driver.execute_script("window.history.go(-3)")
        time.sleep(3)
        acct_reg_expected_title = "Amazon.com. Spend less. Smile more."
        acct_reg_actual_title = driver.title
        if acct_reg_expected_title == acct_reg_actual_title:
            print('"Account registration" page Title is correct:', driver.title)
        else:
            print('"Account registration" page Title is wrong:', driver.title)

        driver.quit()

    def test_negative_login(self):
        driver = self.driver
        driver.get(HP.main_url)
        time.sleep(3)
        wait = WebDriverWait(driver, 3)
        HP.assert_title(driver, "Amazon.com. Spend less. Smile more.")

        # verifying if user can create account without paswords
        driver.find_element(By.ID, "nav-link-accountList-nav-line-1").click()
        driver.find_element(By.ID, "createAccountSubmit").click()
        driver.find_element(By.ID, "ap_customer_name").send_keys(fake.name())
        driver.find_element(By.ID, "ap_email").send_keys(fake.email())
        driver.find_element(By.ID, 'continue').click()
        n = driver.find_element(By.XPATH, "//div[@class='a-alert-content'][contains(.,'Minimum 6 characters')]")
        if n == driver.find_element(By.XPATH,
                                    "//div[@class='a-alert-content'][contains(.,'Minimum 6 characters')]"):
            print("Error message 'Minimum 6 characters required' present")
        else:
            print("Failed:No Minimum 6 characters required present")

    def tearDown(self):
        self.driver.quit()
