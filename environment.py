import unittest
import datetime
from selenium import webdriver


class EnvironmentSetup(unittest.TestCase):

    # setup method to open the browser instance
    def setUp(self):
        self.driver = webdriver.Chrome()
        print("*" * 90)
        print("Test Run Started at: " + str(datetime.datetime.now()))
        print("Chrome Browser Environment Set Up")
        print("*" * 90)
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()

    # tearDown method to close the browser instance and quit after execution
    def tearDown(self):
        if (self.driver != None):
            print("*" * 90)
            print("Test Environment Destroyed")
            print("Test Run Completed at: " + str(datetime.datetime.now()))
            self.driver.close()
            self.driver.quit()
