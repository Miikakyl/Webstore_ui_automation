import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BuyItems(webdriver.Chrome):
    def __init__(self, driver_path=r"C:/", teardown=False):
        options = webdriver.ChromeOptions()
        self.teardown = teardown
        options.add_experimental_option("detach", True)

        self.driver_path = driver_path
        os.environ['PATH'] += self.driver_path
        super(BuyItems, self).__init__(options=options)
        self.implicitly_wait(20)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get("https://www.demoblaze.com/index.html")

    def sign_up(self, username, password):
        self.find_element(By.ID, "signin2").click()

        self.find_element(By.ID, "sign-username").send_keys(username)

        self.find_element(By.ID, "sign-password").send_keys(password)

        self.find_element(
            By.CSS_SELECTOR, "Button[onclick='register()']").click()

        WebDriverWait(self, 10).until(EC.alert_is_present())
        self.switch_to.alert.accept()

    def login(self, username, password):
        self.find_element(By.ID, "login2").click()

        self.find_element(By.ID, "loginusername").send_keys(username)

        self.find_element(By.ID, "loginpassword").send_keys(password)

        self.find_element(By.CSS_SELECTOR, "Button[onclick='logIn()']").click()

    def select_item(self, item_name):
        self.refresh()
        self.find_element(By.LINK_TEXT, f"{item_name}").click()

        WebDriverWait(self, 10).until(
            EC.presence_of_element_located(
                (By.LINK_TEXT, "Add to cart")
            )
        ).click()

        WebDriverWait(self, 10).until(EC.alert_is_present())
        self.switch_to.alert.accept()

    def purchase_item(self, customer_information):

        self.find_element(By.ID, "cartur").click()
        self.find_element(
            By.CSS_SELECTOR, "Button[type='button'][class='btn btn-success'][data-toggle='modal'][data-target='#orderModal']").click()
        input_fields = self.find_elements(
            By.CSS_SELECTOR, "input[id='name'],input[id='country'],input[id='city'],input[id='card'],input[id='month'],input[id='year']")

        for index, input_field in enumerate(input_fields):
            input_field.send_keys(customer_information[index])

        self.find_element(
            By.CSS_SELECTOR, "Button[onclick='purchaseOrder()'").click()
