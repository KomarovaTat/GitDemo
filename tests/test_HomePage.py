import pytest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from data.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self):
        homepage = HomePage(self.driver)
        homepage.getName().send_keys("Tatiana")
        homepage.getEmail().send_keys("tatiana@gmail.com")
        homepage.getPassword().send_keys("12345")
        homepage.getCheckbox().click()

        homepage.selectDropdownOption(1)
        homepage.getSubmitButton().click()
        message = homepage.getMessage().text
        print(message)  # Success! The Form has been submitted successfully!.
        assert "Success" in message

        time.sleep(10)

    def test_formSubmissionWithParams(self, getData):
        homepage = HomePage(self.driver)
        homepage.getName().send_keys(getData[0])
        homepage.getEmail().send_keys(getData[1])
        homepage.getPassword().send_keys(getData[2])
        if getData[3] == "true":
            homepage.getCheckbox().click()

        homepage.selectDropdownOption(getData[4])
        homepage.getSubmitButton().click()
        message = homepage.getMessage().text
        print(message)  # Success! The Form has been submitted successfully!.
        assert "Success" in message
        time.sleep(5)
        self.driver.refresh()

    @pytest.fixture(params=[("Tatiana", "tatiana@gmail.com", "12345", "true", 1),
                            ("John", "john.doe@example.com", "password123", "false", 0),
                            ("Alice", "alice.smith@example.com", "password456", "true", 1)])
    def getData(self, request):
        return request.param

    def test_formSubmissionWithParams2(self, getData1):
        homepage = HomePage(self.driver)
        homepage.getName().send_keys(getData1["firstName"])
        homepage.getEmail().send_keys(getData1["email"])
        homepage.getPassword().send_keys(getData1["password"])
        if getData1['checkbox'] == "true":
            homepage.getCheckbox().click()

        homepage.selectDropdownOption(getData1["gender"])
        homepage.getSubmitButton().click()
        message = homepage.getMessage().text
        print(message)  # Success! The Form has been submitted successfully!.
        assert "Success" in message
        time.sleep(5)
        self.driver.refresh()

    @pytest.fixture(params=[
        {"firstName": "Tatiana123", "email": "tatiana@gmail.com", "password": "12345", "checkbox": "true", "gender": 1},
        {"firstName": "John", "email": "john.doe@example.com", "password": "password123", "checkbox": "false",
         "gender": 0},
        {"firstName": "Alice", "email": "alice.smith@example.com", "password": "password456", "checkbox": "true",
         "gender": 1}])
    def getData1(self, request):
        return request.param

    def test_formSubmissionWithParams3(self, getData3):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        log.info("first name is " + getData3["firstName"])
        homepage.getName().send_keys(getData3["firstName"])

        log.info("email is " + getData3["email"])
        homepage.getEmail().send_keys(getData3["email"])
        homepage.getPassword().send_keys(getData3["password"])
        if getData3['checkbox'] == "true":
            homepage.getCheckbox().click()

        homepage.selectDropdownOption(getData3["gender"])
        homepage.getSubmitButton().click()
        message = homepage.getMessage().text
        print(message)  # Success! The Form has been submitted successfully!.
        assert "Success" in message
        time.sleep(5)
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.data)
    def getData3(self, request):
        return request.param

    def test_formSubmissionWithParams4(self, getData4):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        log.info("first name is " + getData4["firstName"])
        homepage.getName().send_keys(getData4["firstName"])

        log.info("email is " + getData4["email"])
        homepage.getEmail().send_keys(getData4["email"])
        homepage.getPassword().send_keys(getData4["password"])
        if getData4['checkbox'] == "true":
            homepage.getCheckbox().click()

        homepage.selectDropdownOption(getData4["gender"])
        homepage.getSubmitButton().click()
        message = homepage.getMessage().text
        print(message)  # Success! The Form has been submitted successfully!.
        print(getData4)
        assert "Success" in message
        time.sleep(5)
        self.driver.refresh()
        print("22 12 2024")
        print("22 12 2024")
        print("22 12 2024")

        print("new changes in the develop branch")
        print("new changes in the develop branch")
        print("new changes in the develop branch")

    @pytest.fixture(params=HomePageData.getTestData("TestCase1"))
    def getData4(self, request):
        return request.param
