Feature: Workflow test

  Scenario: Workflow test selenium
    Given Prepare classes and go to web page
    When Enter a text in search box with text batman
    Then Press button search
    When Navigate to the url that is show in second card of results
    Then Navigate back using browser features
    Then Press back button
    And Make sure that input for search is empty