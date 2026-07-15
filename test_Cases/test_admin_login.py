import time
from tkinter.constants import SEL

import driver
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from base_pages.Login_admin_page import Login_admin_page
from utilities.read_properties import Read_config
from utilities.custom_logger import log_makker


class Test_01_Admin_Login:

    URL = Read_config.get_URL()
    username = Read_config.get_username()
    password = Read_config.get_password()
    logger = log_makker.log_gen()


        #test case 1
    def test_title_verification(self,setup):
        self.logger.info("***********Test_01_Admin_Login********************")
        self.logger.info("************verification of title of login page*********************")
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.URL)
        act_title = self.driver.title
        print(act_title)
        exp_title = "nopCommerce demo store. Login"
        if exp_title == act_title:
            self.logger.info("***********Title matched**********************")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\test_01_Admin_Login.png")
            self.logger.info("***********Title not matched**********************")
            self.driver.close()
            assert False


    def test_valid_login(self, setup):
        self.logger.info("************Test_valid_login**********************")
        self.driver = setup
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.driver.get(self.URL)
        print("Current URL:", self.driver.current_url)
        self.admin_lp = Login_admin_page(self.driver)
        self.admin_lp.enter_username_field(self.username)
        self.admin_lp.enter_password_field(self.password)
        self.admin_lp.login_button()
        print("Current URL:", self.driver.current_url)

        time.sleep(10)










        





