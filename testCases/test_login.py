from selenium import webdriver
import pageObjects
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()    # create a logger object
    # old:
    #baseURL = "https://admin-demo.nopcommerce.com/"
    #username = "admin@yourstore.com"
    #password = "admin"

    def test_homepage(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        homePageTitle = self.driver.title
        self.driver.close()
        if homePageTitle == "Your store. Login":
            assert True
        else:
            assert False

    def test_login_func(self, setup):
        self.logger.info("************* Test_001_Login **************")
        self.logger.info("************* Verify Login Test **************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.loginpage = pageObjects.LoginPage(self.driver) # create an object for LoginPage Class
        self.loginpage.setUserName(self.username)
        self.loginpage.setPassword(self.password)
        self.loginpage.clickLogin()
        adminpageTitle = self.driver.title
        #self.driver.close()
        if adminpageTitle == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("************* Login Test Pass **************")
        else:
            self.driver.save_screenshot("Screenshots/test_login_func.png")
            self.logger.error("************* Login Test Failed **************")
            self.driver.close()
            assert False





