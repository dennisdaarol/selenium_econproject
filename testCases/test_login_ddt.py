import time

from selenium import webdriver
import pageObjects
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils   # import utils for DDT

class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path=".//TestData/LoginData.xlsx"
    #username = ReadConfig.getUserEmail() -- Remove since we are using data driven, unsername and password is from file.
    #password = ReadConfig.getPassword()
    logger = LogGen.loggen()    # create a logger object
    # old:
    #baseURL = "https://admin-demo.nopcommerce.com/"
    #username = "admin@yourstore.com"
    #password = "admin"

    def test_login(self, setup):
        self.logger.info("************* Test_002_DDT_Login **************")
        self.logger.info("************* Verify Login Test using DDT **************")
        self.driver = setup
        self.driver.get(self.baseURL)

        self.loginpage = pageObjects.LoginPage(self.driver) # create an object for LoginPage Class

        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        print(f'Rows: {self.rows}')

        run_status = []
        for r in range(2, self.rows+1):
            self.user = XLUtils.readData(self.path,'Sheet1',r,1)
            self.password = XLUtils.readData(self.path,'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)

            self.loginpage.setUserName(self.user)
            self.loginpage.setPassword(self.password)
            self.loginpage.clickLogin()
            time.sleep(4)
            pageTitle = self.driver.title
            #self.driver.close()
            if pageTitle == "Your store. Login":
                if self.exp == 'Fail':
                    self.logger.info(f'Username: {self.user}, Password: {self.password} = PASS')
                    run_status.append('Pass')
                else:
                    self.driver.save_screenshot("Screenshots/test_login_func_DDT.png")
                    self.logger.error(f'Username: {self.user}, Password: {self.password} = FAIL')
                    run_status.append('Fail')
            elif pageTitle == "Dashboard / nopCommerce administration":
                if self.exp == 'Pass':
                    self.logger.info(f'Username: {self.user}, Password: {self.password} = PASS')
                    run_status.append('Pass')
                else:
                    self.driver.save_screenshot("Screenshots/test_login_func_DDT.png")
                    self.logger.error(f'Username: {self.user}, Password: {self.password} = FAIL')
                    run_status.append('Fail')
                    self.loginpage.clickLogout()
        if 'Fail' not in run_status:
            self.logger.info(f'All data tested Passed.')
            assert True
        else:
            self.logger.error(f'One or more input scenario Failed.')
            assert False
        self.driver.close()


