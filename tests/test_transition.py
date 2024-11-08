from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import TestLocators
from data import email, password
from conftest import driver


class TestTransition:

    def test_personal_account_transition(self, driver):
        driver.find_element(*TestLocators.LOGIN_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.ENTER_LETTER)))
        driver.find_element(*TestLocators.EMAIL_INPUT_FIELD).send_keys(email)
        driver.find_element(*TestLocators.PASSWORD_INPUT_FIELD).send_keys(password)
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.CREATE_ORDER_BUTTON)))
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.NAME_FIELD)))
        assert driver.find_element(*TestLocators.NAME_FIELD)

    def test_constructor_transition(self, driver):
        driver.find_element(*TestLocators.LOGIN_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.ENTER_LETTER)))
        driver.find_element(*TestLocators.EMAIL_INPUT_FIELD).send_keys(email)
        driver.find_element(*TestLocators.PASSWORD_INPUT_FIELD).send_keys(password)
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.CREATE_ORDER_BUTTON)))
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.NAME_FIELD)))
        driver.find_element(*TestLocators.CONSTRUCTOR_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.CREATE_ORDER_BUTTON)))
        assert driver.find_element(*TestLocators.CREATE_ORDER_BUTTON)

    def test_logo_transition(self, driver):
        driver.find_element(*TestLocators.LOGIN_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.ENTER_LETTER)))
        driver.find_element(*TestLocators.EMAIL_INPUT_FIELD).send_keys(email)
        driver.find_element(*TestLocators.PASSWORD_INPUT_FIELD).send_keys(password)
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.CREATE_ORDER_BUTTON)))
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.NAME_FIELD)))
        driver.find_element(*TestLocators.LOGO_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.CREATE_ORDER_BUTTON)))
        assert driver.find_element(*TestLocators.CREATE_ORDER_BUTTON)

    def test_exit_transition(self, driver):
        driver.find_element(*TestLocators.LOGIN_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.ENTER_LETTER)))
        driver.find_element(*TestLocators.EMAIL_INPUT_FIELD).send_keys(email)
        driver.find_element(*TestLocators.PASSWORD_INPUT_FIELD).send_keys(password)
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.CREATE_ORDER_BUTTON)))
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.NAME_FIELD)))
        driver.find_element(*TestLocators.EXIT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.ENTER_LETTER)))
        assert driver.find_element(*TestLocators.ENTER_LETTER)

    def test_section_transition_bun(self, driver):
        driver.find_element(*TestLocators.SECTION_SAUCE).click()
        driver.find_element(*TestLocators.SECTION_BUN).click()
        assert 'type_current' in driver.find_element(*TestLocators.SECTION_BUN_CUR).get_attribute('class')

    def test_section_transition_sauce(self, driver):
        driver.find_element(*TestLocators.SECTION_SAUCE).click()
        assert 'type_current' in driver.find_element(*TestLocators.SECTION_SAUCE_CUR).get_attribute('class')

    def test_section_transition_filling(self, driver):
        driver.find_element(*TestLocators.SECTION_FILLING).click()
        assert 'type_current' in driver.find_element(*TestLocators.SECTION_FILLING_CUR).get_attribute('class')
