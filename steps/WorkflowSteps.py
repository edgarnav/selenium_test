from behave import given, when, then
from pages.SearchPage import SearchPage
from pages.ResultsPage import ResultsPage


class WorkflowSteps:

    @given("Prepare classes and go to web page")
    def prepare_classes(context):
        context.search_page = SearchPage(context.driver)
        context.results_page = ResultsPage(context.driver)

    @when("Enter a text in search box with text {text}")
    def send_text_search(context, text):
        context.search_page.send_text_search(text)

    @then("Press button search")
    def press_btn_search(context):
        context.search_page.click_btn_search()

    @when("Navigate to the url that is show in second card of results")
    def go_to_url(context):
        context.results_page.find_url_batman()

    @then("Navigate back using browser features")
    def back_to_results_page(context):
        context.results_page.back_page()

    @then("Press back button")
    def click_back_btn(context):
        context.results_page.back_page()

    @then("Make sure that input for search is empty")
    def sure_input_empty(context):
        context.search_page.clear_search_input()
