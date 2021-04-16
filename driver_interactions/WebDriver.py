from selenium import webdriver
import utilities.Logger as Log


class WebDriver:

    log = Log.func_logger()

    def init_driver(self):
        self.log.info("Opening in Chrome")
        return webdriver.Chrome("/Users/edgarnav/Documents/chromedriver")
