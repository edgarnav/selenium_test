from driver_interactions.ElementsInteractions import ElementsInteractions
from driver_interactions.WebDriver import WebDriver
import utilities.Logger as Logger
import config.ConfigFile as ConfigFile
import time

log = Logger.func_logger()


def before_all(context):
    log.info("Script started")
    context.prepare_driver = WebDriver()
    context.driver = context.prepare_driver.init_driver()
    context.bp = ElementsInteractions(context.driver)
    context.bp.launch_web_page(ConfigFile.url)


def after_all(context):
    time.sleep(2)
    context.driver.quit()
    log.info("Script ended")
