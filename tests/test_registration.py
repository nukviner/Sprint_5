from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import TestLocators
from data import name, email, password
from conftest import driver
from helpers import Helpers


class TestRegistration:

    def test_registration_new_user(self, driver):
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.ENTER_LETTER)))
        driver.find_element(*TestLocators.REGISTER_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.REGISTER_LETTER)))
        driver.find_element(*TestLocators.NAME_INPUT_FIELD).send_keys(name)
        driver.find_element(*TestLocators.EMAIL_INPUT_FIELD).send_keys(Helpers.generate_email())
        driver.find_element(*TestLocators.PASSWORD_INPUT_FIELD).send_keys(password)
        driver.find_element(*TestLocators.REGISTER_BUTTON_2).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.ENTER_LETTER)))
        driver.find_element(*TestLocators.EMAIL_INPUT_FIELD).send_keys(email)
        driver.find_element(*TestLocators.PASSWORD_INPUT_FIELD).send_keys(password)
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.CREATE_ORDER_BUTTON)))
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.NAME_FIELD)))
        assert driver.find_element(*TestLocators.NAME_FIELD).get_attribute('value') == name

    def test_registration_short_pass(self, driver):
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.ENTER_LETTER)))
        driver.find_element(*TestLocators.REGISTER_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.REGISTER_LETTER)))
        password = '123'
        driver.find_element(*TestLocators.NAME_INPUT_FIELD).send_keys(name)
        driver.find_element(*TestLocators.EMAIL_INPUT_FIELD).send_keys(email)
        driver.find_element(*TestLocators.PASSWORD_INPUT_FIELD).send_keys(password)
        driver.find_element(*TestLocators.REGISTER_BUTTON_2).click()
        assert driver.find_element(*TestLocators.WRONG_PASSWORD)
