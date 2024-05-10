import pageObjects
from selenium import webdriver

class Test_002_Login:
    baseURL = "https://admin-demo.nopcommerce.com/"
    username = "admin@yourstore.com"
    password = "admin"

    def test_home(self):
        self.options = webdriver.ChromeOptions()  # old: driver=webdriver.Chrome()
        #self.options.add_experimental_option("detach", True)
        self.options.add_experimental_option(name="detach", value=True)
        self.driver = webdriver.Chrome(options=self.options)
        #self.driver = setup
        self.driver.get(self.baseURL)
        Page_Title = self.driver.title
        #self.driver.close()
        if Page_Title == "Yours store. Login":
            assert True
        else:
            self.driver.save_screenshot("Screenshots/login_page2.png")
            assert False

    def Test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.loginpage = pageObjects.LoginPage2(self.driver)
        self.loginpage.setUserName(self.username)
        self.loginpage.setPassword(self.password)
        self.loginpage.clickLoginButton()
        loginPage_title = self.driver.title
        if loginPage_title == "Dashboard / nopCommerce administration":
            assert True
        else:
            assert False
        self.loginpage.clickLogoutButton()
        Page_Title = self.driver.title
        self.driver.close()
        if Page_Title == "Your store. Login":
            assert True
        else:
            assert False





