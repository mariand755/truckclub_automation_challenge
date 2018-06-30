from time import sleep
from environment import EnvironmentSetup
from page_object.business_page import Business


class BusinessTest(EnvironmentSetup):

    def test_verify_if_object_exists(self):
        self.visit_page()

        business = Business(self.driver)
        self.assertTrue(business.get_mission().is_displayed(), True)
        self.write_to_console("Mission Statement for Business is Displayed")

    def test_negative_scenario(self):
        self.visit_page()

        business = Business(self.driver)
        if business.get_mission().is_displayed():
            self.write_to_console("Mission Statement for Business is Displayed")
            business.contact_us()
            self.write_to_console("Clicked on Contact Us Button")
            business.submit()
            self.write_to_console("Clicked on Submit Button")
            self.assertTrue(business.get_error_message().is_displayed(), True)
            self.write_to_console("Verified that Error Messages Appears if We Try to Submit Form Without Filling Mandatory Fields")

    def visit_page(self):
        self.driver.get("https://www.trunkclub.com/business")
        self.driver.set_page_load_timeout(20)

    def write_to_console(self, message):
        print(message)
        sleep(2)

# Use following code if you are going to run test case individually.
# if __name__ == '__main__':
#     unittest.main()
