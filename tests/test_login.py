from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import TestLocators


class TestLogin:

    def test_login_from_main():
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*TestLocators.LOGIN_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.ENTER_LETTER)))
        email = 'kazeka7@gmail.com'
        password = 'somepass'
        driver.find_element(*TestLocators.EMAIL_INPUT_FIELD).send_keys(email)
        driver.find_element(*TestLocators.PASSWORD_INPUT_FIELD).send_keys(password)
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.CREATE_ORDER_BUTTON)))
        assert driver.find_element(*TestLocators.CREATE_ORDER_BUTTON)
        driver.quit()

    def test_login_from_lc():
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.ENTER_LETTER)))
        email = 'kazeka7@gmail.com'
        password = 'somepass'
        driver.find_element(*TestLocators.EMAIL_INPUT_FIELD).send_keys(email)
        driver.find_element(*TestLocators.PASSWORD_INPUT_FIELD).send_keys(password)
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.CREATE_ORDER_BUTTON)))
        assert driver.find_element(*TestLocators.CREATE_ORDER_BUTTON)
        driver.quit()

    def test_login_from_registration():
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.ENTER_LETTER)))
        driver.find_element(*TestLocators.REGISTER_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.REGISTER_LETTER)))
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.ENTER_LETTER)))
        email = 'kazeka7@gmail.com'
        password = 'somepass'
        driver.find_element(*TestLocators.EMAIL_INPUT_FIELD).send_keys(email)
        driver.find_element(*TestLocators.PASSWORD_INPUT_FIELD).send_keys(password)
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.CREATE_ORDER_BUTTON)))
        assert driver.find_element(*TestLocators.CREATE_ORDER_BUTTON)
        driver.quit()

    def test_login_from_pass_recovery():
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.ENTER_LETTER)))
        driver.find_element(*TestLocators.RECOVER_PASSWORD_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.RECOVER_PASSWORD_LETTER)))
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.ENTER_LETTER)))
        email = 'kazeka7@gmail.com'
        password = 'somepass'
        driver.find_element(*TestLocators.EMAIL_INPUT_FIELD).send_keys(email)
        driver.find_element(*TestLocators.PASSWORD_INPUT_FIELD).send_keys(password)
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.CREATE_ORDER_BUTTON)))
        assert driver.find_element(*TestLocators.CREATE_ORDER_BUTTON)
        driver.quit()
