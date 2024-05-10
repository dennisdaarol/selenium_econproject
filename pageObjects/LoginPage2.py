from selenium.webdriver.common.by import By

class LoginPage2:
    textbox_email_xpath = "//input[@type='email']"
    textbox_password_xpath = "//input[@type='password']"
    button_login_xpath = "//button[@type='submit']"
    button_logout_xpath = "//a[@href='/logout']"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element(By.XPATH, self.textbox_email_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_email_xpath).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).send_keys(password)

    def clickLoginButton(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def clickLogoutButton(self):
        self.driver.find_element(By.XPATH, self.button_logout_xpath).click()

