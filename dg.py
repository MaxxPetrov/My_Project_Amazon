from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import unittest
from faker import Faker
import time

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager, EdgeChromiumDriverManager

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver = webdriver.Ie(service=Service(IEDriverManager().install()))
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))

faker_class = Faker()


class FirefoxSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        self.driver.maximize_window()

    def test_amazon_create_login(self):
        driver = self.driver
        self.driver.get("https://testpages.herokuapp.com/")