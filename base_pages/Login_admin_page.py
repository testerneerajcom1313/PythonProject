# this page will contain the locators of login page and action methods (entering th
# username or password or clicking on login button)
from selenium.webdriver.common.by import By


class Login_admin_page:
    textbox_username_field = "Email"
    textbox_password_field = "Password"
    btn_login_xpath = "//button[normalize-space()='Log in']"

    #constructor of login page and driver is global variable to access the class variables

    def __init__(self, driver):
        self.driver = driver

        #we write action method

    def enter_username_field(self, username):
        self.driver.find_element(By.ID, self.textbox_username_field).clear()
        self.driver.find_element(By.ID, self.textbox_username_field).send_keys(username)

    def enter_password_field(self, password):
        self.driver.find_element(By.ID, self.textbox_password_field).clear()
        self.driver.find_element(By.ID, self.textbox_password_field).send_keys(password)

    def login_button(self):
        self.driver.find_element(By.XPATH, self.btn_login_xpath).click()
        