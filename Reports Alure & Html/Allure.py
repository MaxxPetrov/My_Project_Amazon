import AllureReports
from _pytest import unittest

if __name__ == "__main__":
    unittest.main(AllureReports)

    #To run AllureReports use
    #from Terminal:
    #py.test --alluredir=./AllureReports. / test_name.py

    #TogenerateReports use: \
       # allure serve ./AllureReports
