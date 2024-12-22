import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.CheckoutPage import CheckOutPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


# @pytest.mark.usefixtures("setup")
class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        checkOutPage = homePage.shopItems()
        log.info("getting all the products titles")
        products = checkOutPage.getProductTitle()

        for product in products:
            productName = product.find_element(By.XPATH, "div/h4/a").text
            if productName == "Blackberry":
                product.find_element(By.XPATH, "div/button").click()  # click on Add button #card footer

        checkOutPage.checkOut1Products().click()  # clicking on Checkout(1) button, Checkout page opens then

        # driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click() #clicking on Checkout button
        confirmPage = checkOutPage.checkOutItems()

        # TC choose a necessary country name, click on checkbox andf click on Purchase button
        log.info("Entering country name as Pol")
        self.driver.find_element(By.ID, "country").send_keys("Pol")

        # wait = WebDriverWait(self.driver, 10)
        # wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "Poland")))

        self.verifyLinkPresence("Poland")

        self.driver.find_element(By.LINK_TEXT, "Poland").click()

        self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()

        self.driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

        successText = self.driver.find_element(By.CLASS_NAME, "alert-success ").text
        log.info("Text received from application is " + successText)
        assert "Success! Thank you!njkkn" in successText

        print(successText)  # Success! Thank you! Your order will be delivered in next few weeks :-).

        time.sleep(4)
