from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
from selenium.webdriver.support.ui import WebDriverWait
from tests_data import Valid_Data
from tests_data import Invalid_Data
from tests.locators import RTPanelNaviBar
from tests.locators import RTAutorizationLocators
from tests.locators import RTAutorizationAllerts
from tests.locators import RTRegistrationLocators
import allure

fake_name = Faker().name()
fake_email = Faker().email()
fake_password = Faker().password()

@allure.story('HWMod28')
class TestValidRegistrationRT:

    def setup(self):
        self.open()

    def open(self):
        self.driver = webdriver.Chrome('A:\chromedriver\cd\chromedriver_107')
        self.driver.get("https://b2c.passport.rt.ru")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_BUTTON_REGISTER)))


    def close(self):
        self.driver.quit()

    def teardown(self):
        self.close()


# 9
    @allure.feature('Авторизация с не корректным Email')
    def test_autorization_invalid_email(self):
        self.driver.find_element(By.ID, RTAutorizationLocators.LOCATOR_RT_AUTORIZATION_USER).send_keys(
            Invalid_Data.fake_email)
        self.driver.find_element(By.ID, RTAutorizationLocators.LOCATOR_RT_AUTORIZATION_PASSWORD).send_keys(
            Invalid_Data.fake_password)
        self.driver.find_element(By.ID, RTAutorizationLocators.LOCATOR_RT_AUTORIZATION_BUTTON_LOGIN).click()
        assert self.driver.find_element(By.XPATH, RTAutorizationAllerts.LOCATOR_RT_AUTORIZATION_ALLERTS_ERROR)
        assert self.driver.find_element(By.XPATH, RTAutorizationAllerts.LOCATOR_ERROR_TEXT_INVALID_EMAIL)



