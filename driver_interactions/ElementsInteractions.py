from traceback import print_stack

from allure_commons.types import AttachmentType
from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

import utilities.Logger as Log
import allure


class ElementsInteractions:

    log = Log.func_logger()

    def __init__(self, driver):
        self.driver = driver

    def locator(self, locator_type):
        if locator_type == "id":
            return By.ID
        elif locator_type == "name":
            return By.NAME
        elif locator_type == "class":
            return By.CLASS_NAME
        elif locator_type == "xpath":
            return By.XPATH
        elif locator_type == "css":
            return By.CSS_SELECTOR
        elif locator_type == "tag":
            return By.TAG_NAME
        elif locator_type == "link":
            return By.LINK_TEXT
        elif locator_type == "plink":
            return By.PARTIAL_LINK_TEXT
        else:
            self.log.error("Locator Type : " + locator_type + " entered is not found")
        return False

    def launch_web_page(self, url):
        try:
            self.driver.get(url)
            self.log.info("Web Page Launched with URL : " + url)
        except Exception:
            self.log.info("Web Page not Launched with URL : " + url)

    def go_to_url(self, url):
        self.driver.get(url)

    def verify_page(self, page_name):
        if page_name != self.driver.title:
            self.take_screenshot(self.driver.title)
            assert False

    def back_page(self):
        self.driver.back()

    def explicit_wait(self, locator_value, locator_type, time):
        try:
            locator_by_type = self.locator(locator_type)
            WebDriverWait(self.driver, time).until(ec.presence_of_all_elements_located((locator_by_type, locator_value)))
            self.log.info("Element found with locator " + locator_value + " using locatorType " + locator_by_type)
        except Exception:
            self.log.error(
                "Element not found with locator " + locator_value + " using locatorType " + locator_type)
            print_stack()
            self.take_screenshot(locator_type)
            assert False


    def get_element(self, locator_value, locator_type):
        element = None
        try:
            locator_by_type = self.locator(locator_type)
            element = self.driver.find_element(locator_by_type, locator_value)
            self.log.info("Element found with locator " + locator_value + " using locatorType " + locator_by_type)
        except Exception:
            self.log.error(
                "Element not found with locator " + locator_value + " using locatorType " + locator_type)
            print_stack()
        return element

    def get_all_elements(self, locator_value, locator_type):
        elements = None
        try:
            locator_by_type = self.locator(locator_type)
            elements = self.driver.find_elements(locator_by_type, locator_value)
            self.log.info("Elements found with locator " + locator_value + " using locatorType " + locator_by_type)
        except Exception:
            self.log.error(
                "Elements not found with locator " + locator_value + " using locatorType " + locator_type)
            print_stack()
        return elements

    def wait_element(self, locator_value, locator_type):
        try:
            locator_by_type = self.locator(locator_type)
            wait = WebDriverWait(self.driver, 25, poll_frequency=1,
                                 ignored_exceptions=[ElementNotVisibleException, NoSuchElementException])
            element = wait.until(ec.presence_of_element_located((locator_by_type, locator_value)))
            self.log.info("WebElement found with locator value " + locator_value + " using locatorType " + locator_type)
        except Exception:
            self.log.error(
                "WebElement not found with locator value " + locator_value + " using locatorType " + locator_type)
            print_stack()
            self.take_screenshot(locator_type)
            assert False
        return element

    def click_element(self, locator_value, locator_type):
        try:
            element = self.wait_element(locator_value, locator_type)
            element.click()
            self.log.info(
                "Clicked on WebElement with locator value " + locator_value + " using locatorType " + locator_type)
        except Exception:
            self.log.error(
                "Unable to Click on WebElement with locator value " + locator_value + " using locatorType " + locator_type)
            print_stack()
            assert False

    def send_text(self, text, locator_value, locator_type):
        try:
            element = self.wait_element(locator_value, locator_type)
            element.send_keys(text)
            self.log.info(
                "Sent the text " + text + " in WebElement with locator value " + locator_value + " using locatorType " + locator_type)
        except Exception:
            self.log.error(
                "Unable to Sent the text " + text + " in WebElement with locator value " + locator_value + "using locatorType " + locator_type)
            print_stack()
            self.take_screenshot(locator_type)
            assert False

    def get_text(self, locator_value, locator_type):
        element_text = None
        try:
            element = self.wait_element(locator_value, locator_type)
            element_text = element.text
            self.log.info(
                "Got the text " + element_text + " from WebElement with locator value " + locator_value + " using locatorType " + locator_type)
        except Exception:
            self.log.error(
                "Unable to get the text " + element_text + " from WebElement with locator value " + locator_value + "using locatorType " + locator_type)
            print_stack()

        return element_text

    def is_element_displayed(self, locator_value, locator_type):
        element_displayed = None
        try:
            element = self.wait_element(locator_value, locator_type)
            element_displayed = element.is_displayed()
            self.log.info(
                "WebElement is Displayed on web page with locator value " + locator_value + " using locatorType " + locator_type)
        except Exception:
            self.log.error(
                "WebElement is not Displayed on web page with locator value " + locator_value + " using locatorType " + locator_type)
            print_stack()

        return element_displayed

    def scroll(self, locator_value, locator_type):
        actions = ActionChains(self.driver)
        try:
            element = self.wait_element(locator_value, locator_type)
            actions.move_to_element(element).perform()
            self.log.info(
                "Scrolled to WebElement with locator value " + locator_value + " using locatorType " + locator_type)
        except Exception:
            self.log.error(
                "Unable to scroll to WebElement with locator value " + locator_value + "using locatorType " + locator_type)
            print_stack()

    def take_screenshot(self, text):
        allure.attach(self.driver.get_screenshot_as_png(), name=text, attachment_type=AttachmentType.PNG)
