import time
from selenium.webdriver.common.keys import Keys
from .base_page import BasePage
from selenium.webdriver.common.by import By

class MainPage(BasePage):
    modalWindow = ".modal-header"
    SignInButton = ".btn.btn-outline-white.header_signin"
    inputLogin = "#signinEmail"
    inputPassword = "#signinPassword"
    # checkboxRememberMe = "#remember"
    # buttonForgotPassword = "//button[@_ngcontent-miv-c51]"
    # loginButton = ".modal-footer.d-flex.justify-content-between > .btn.btn-primary"
    click_BUTTON = "//div[@class='header_right d-flex align-items-center']//button[@class='header-link -guest']"
    add_but = "//div[@class='panel-page_heading d-flex justify-content-between']//button[@class='btn btn-primary']"
    add_car1_1 = "//select[@id='addCarBrand']/option[2]"
    add_car1_2 = "//select[@id='addCarModel']/option[1]"
    mlg_inp = "//div[@class='input-group']/input[@id='addCarMileage']"
    butt_add_last = "//div[@class='modal-footer d-flex justify-content-end']//button[@class='btn btn-primary']"


    def click_sign_in(self):
        self.wait_and_click_on_element(By.CSS_SELECTOR, self.SignInButton)

    def is_open_modal_window(self):
        return self.is_element_clickable(By.CSS_SELECTOR, self.modalWindow)

    # def enter_login(self, login):
    #     self.browser.find_element(By.CSS_SELECTOR, self.inputLogin).send_keys(login)
    #
    # def enter_password(self, password):
    #     self.browser.find_element(By.CSS_SELECTOR, self.inputPassword).send_keys(password)

    # def click_login_button(self):
    #     self.browser.find_element(By.CSS_SELECTOR, self.loginButton)

    def BUTTON(self):
        self.browser.find_element(By.XPATH, self.click_BUTTON).click()

    def add(self):
        self.browser.find_element(By.XPATH, self.add_but).click()

    def add_car1(self):
        self.browser.find_element(By.XPATH, self.add_car1_1).click()
        self.browser.find_element(By.XPATH, self.add_car1_2).click()

    def mlg_1(self):
        self.browser.find_element(By.XPATH, self.mlg_inp).send_keys('100')

    def lastbut(self):
        self.browser.find_element(By.XPATH, self.butt_add_last).click()
        time.sleep(3)
