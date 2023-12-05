from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC # You can change EC

class LoginPage:
    textbox_username_id = "Email"
    textbox_username = (By.ID, 'Email') # wait until element is displayed
    textbox_password_css = "input[id='Password']"
    button_login_xpath = "//button[@class='button-1 login-button']"
    link_logout_id = "Logout"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element(By.ID, self.textbox_username_id).clear() # another command to use
        self.element = WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located(locator=self.textbox_username))
        self.element.clear()
        #self.driver.find_element(By.ID, self.textbox_username_id).clear() #older version with No wait
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.CSS_SELECTOR, self.textbox_password_css).clear()
        self.driver.find_element(By.CSS_SELECTOR, self.textbox_password_css).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.ID, self.link_logout_id).click()