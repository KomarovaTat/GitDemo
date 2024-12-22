from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConformPage


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver

    productTitle = (By.XPATH, "//div[@class='card h-100']")
    #driver.find_elements(By.XPATH, "//div[@class='card h-100']")

    # productFooter = (By.XPATH, "div/button") #don't need it
    # #find_element(By.XPATH, "div/button"

    checkOut1 = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    #driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']")

    checkOut = (By.CSS_SELECTOR, "button.btn-success")
    #driver.find_element(By.CSS_SELECTOR, "button.btn-success")

    def getProductTitle(self):
        return self.driver.find_elements(*CheckOutPage.productTitle)

    # def getProductFooter(self): #don't need it
    #     return self.driver.find_element(*CheckOutPage.productFooter)

    def checkOut1Products(self):
        return self.driver.find_element(*CheckOutPage.checkOut1)

    def checkOutItems(self):
        self.driver.find_element(*CheckOutPage.checkOut).click()
        confirmPage = ConformPage(self.driver)
        return confirmPage