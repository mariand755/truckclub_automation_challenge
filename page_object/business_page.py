from selenium.webdriver.common.by import By


class Business(object):
    def __init__(self, driver):
        self.driver = driver

        # page locators
        mission_statement = "//h1[contains(text(),'Reward. Engage.')]"
        xpath_contact_us_button = '//section[@id="want-to-know-more"]//button'
        xpath_submit_button = '//input[@id= "saveForm"]'

        self.mission = driver.find_element(By.XPATH, mission_statement)
        self.contact_us_button = driver.find_element(By.XPATH, xpath_contact_us_button)
        self.submit_button = driver.find_element(By.XPATH, xpath_submit_button)

    def get_mission(self):
        return self.mission

    def contact_us(self):
        self.contact_us_button.click()

    def submit(self):
        self.submit_button.click()

    def get_error_message(self):
        negative_error = '//div[@class="form-inner"]//label[contains(text(),"Enter your company")]'
        return self.driver.find_element(By.XPATH, negative_error)

