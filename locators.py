from selenium.webdriver.common.by import By

class TestLocators:

    #Кнопка "Личный кабинет"
    PERSONAL_ACCOUNT = By.XPATH, "//*[@href='/account']"

    #Кнопка "Зарегистрироваться" на форме входа
    REGISTER_BUTTON = By.XPATH, "//a[@href='/register']"

    #Кнопка "Зарегистрироваться" на форме регистрации
    REGISTER_BUTTON_2 = By.XPATH, "//button[text()='Зарегистрироваться']"

    #Кнопка "Восстановить пароль"
    RECOVER_PASSWORD_BUTTON = By.XPATH, "//*[@href='/forgot-password']"

    #Кнопка "Войти"
    LOGIN_BUTTON = By.XPATH, "//*[text()='Войти']"

    #Надпись "Вход"
    ENTER_LETTER = By.XPATH, "//h2[text()='Вход']"

    #Надпись "Регистрация"
    REGISTER_LETTER = By.XPATH, "//h2[text()='Регистрация']"

    #Надпись "Восстановление пароля"
    RECOVER_PASSWORD_LETTER = By.XPATH, "//h2[text()='Восстановление пароля']"

    #Поле для ввода имени при регистрации
    REG_NAME_INPUT_FIELD = By.XPATH, "//fieldset[1]/div/div/input"

    #Поле для ввода email при регистрации
    REG_EMAIL_INPUT_FIELD = By.XPATH, "//fieldset[2]/div/div/input"

    #Поле для ввода пароля при регистрации
    REG_PASSWORD_INPUT_FIELD = By.XPATH, "//fieldset[3]/div/div/input"

    #Поле для ввода email для входа
    EMAIL_INPUT_FIELD = By.XPATH, "//fieldset[1]/div/div/input"

    #Поле для ввода пароля для входа
    PASSWORD_INPUT_FIELD = By.XPATH, "//fieldset[2]/div/div/input"

    #Кнопка "Оформить заказ"
    CREATE_ORDER_BUTTON = By.XPATH, "//button[text()='Оформить заказ']"

    #Поле "Имя" в профиле
    NAME_FIELD = By.XPATH, "//li[1]/div/div/input"

    #Предупреждение "Некорректный пароль"
    WRONG_PASSWORD = By.XPATH, "//*[@class='input__error text_type_main-default']"

    #Кнопка "Войти в аккаунт"
    LOGIN_ACCOUNT_BUTTON = By.XPATH, "//button[text()='Войти в аккаунт']"

    #Кнопка "Конструктор"
    CONSTRUCTOR_BUTTON = By.XPATH, "//*[text()='Конструктор']"

    #Кнопка "Логотип"
    LOGO_BUTTON = By.XPATH, "//div/a[@href='/']"

    #Кнопка "Выход"
    EXIT_BUTTON = By.XPATH, "//*[text()='Выход']"

    #Раздел "Булки"
    SECTION_BUN = By.XPATH, "//span[text()='Булки']"

    #Раздел "Соусы"
    SECTION_SAUCE = By.XPATH, "//span[text()='Соусы']"

    #Раздел "Начинки"
    SECTION_FILLING = By.XPATH, "//span[text()='Начинки']"

    #Раздел "Булки" - выбран
    SECTION_BUN_CUR = By.XPATH, "//main/section[1]/div[1]/div[1]"

    #Раздел "Соусы" - выбран
    SECTION_SAUCE_CUR = By.XPATH, "//main/section[1]/div[1]/div[2]"

    #Раздел "Начинки" - выбран
    SECTION_FILLING_CUR = By.XPATH, "//main/section[1]/div[1]/div[3]"
