from driver_interactions.ElementsInteractions import ElementsInteractions
import utilities.Logger as Logger

class ResultsPage(ElementsInteractions):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    log = Logger.func_logger()

    url_batman = "https://www.tvmaze.com/shows/975/batman"
    class_url = "white-text"
    class_back_btn = "btn-primary"

    def find_url_batman(self):
        elements = self.get_all_elements(self.class_url, "class")
        links = [element.get_attribute('href') for element in elements]
        index = links.index(self.url_batman)
        elements[index].click()

    def return_page(self):
        self.back_page()

    def click_back_btn(self):
        self.click_element(self.class_back_btn, "class")
