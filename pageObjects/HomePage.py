

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pageObjects.CheckoutPage import CheckOutPage

class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop =(By.CSS_SELECTOR, "a[href*='shop']")

    userName = (By.CSS_SELECTOR, "input[name='name'].form-control")
    email = (By.CSS_SELECTOR, "[name='email'")
    password = (By.ID, "exampleInputPassword1")
    checkbox = (By.ID, "exampleCheck1")
    dropdown = (By.ID, "exampleFormControlSelect1")
    submitButton = (By.CSS_SELECTOR, ".btn-success")
    message = (By.CSS_SELECTOR, ".alert-success")

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkOutPage = CheckOutPage(self.driver)
        return checkOutPage

    def getName(self):
        return self.driver.find_element(*HomePage.userName)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getPassword(self):
        return self.driver.find_element(*HomePage.password)

    def getCheckbox(self):
        return self.driver.find_element(*HomePage.checkbox)

    def selectDropdownOption(self, index):
        dropdown = Select(self.driver.find_element(*HomePage.dropdown))
        dropdown.select_by_index(index)

    def getSubmitButton(self):
        return self.driver.find_element(*HomePage.submitButton)

    def getMessage(self):
        return self.driver.find_element(*HomePage.message)
