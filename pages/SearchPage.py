from driver_interactions.ElementsInteractions import ElementsInteractions


class SearchPage(ElementsInteractions):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    name_search_input = "search"
    class_search_btn = "waves-light"

    def send_text_search(self, text):
        self.send_text(text, self.name_search_input, "name")

    def click_btn_search(self):
        self.click_element(self.class_search_btn, "class")

    def clear_search_input(self):
        element = self.get_element(self.name_search_input, "name")
        element.clear()
