from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import TestLocators


class TestRegistration:

    def test_registration_new_user():
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")

        driver.find_element(*TestLocators.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.ENTER_LETTER)))
        driver.find_element(*TestLocators.REGISTER_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.REGISTER_LETTER)))

        name = 'Qwertyuiop'
        email = 'kazeka150@gmail.com'
        password = 'somepass'

        driver.find_element(*TestLocators.REG_NAME_INPUT_FIELD).send_keys(name)
        driver.find_element(*TestLocators.REG_EMAIL_INPUT_FIELD).send_keys(email)
        driver.find_element(*TestLocators.REG_PASSWORD_INPUT_FIELD).send_keys(password)
        driver.find_element(*TestLocators.REGISTER_BUTTON_2).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.ENTER_LETTER)))

        driver.find_element(*TestLocators.EMAIL_INPUT_FIELD).send_keys(email)
        driver.find_element(*TestLocators.PASSWORD_INPUT_FIELD).send_keys(password)
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.CREATE_ORDER_BUTTON)))

        driver.find_element(*TestLocators.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.NAME_FIELD)))

        assert driver.find_element(*TestLocators.NAME_FIELD).get_attribute('value') == name

        driver.quit()

    def test_registration_short_pass():
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")

        driver.find_element(*TestLocators.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.ENTER_LETTER)))
        driver.find_element(*TestLocators.REGISTER_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.REGISTER_LETTER)))

        name = 'Qwertyuiop'
        email = 'kazeka1@gmail.com'
        password = '123'

        driver.find_element(*TestLocators.REG_NAME_INPUT_FIELD).send_keys(name)
        driver.find_element(*TestLocators.REG_EMAIL_INPUT_FIELD).send_keys(email)
        driver.find_element(*TestLocators.REG_PASSWORD_INPUT_FIELD).send_keys(password)
        driver.find_element(*TestLocators.REGISTER_BUTTON_2).click()

        assert driver.find_element(*TestLocators.WRONG_PASSWORD)

        driver.quit()
