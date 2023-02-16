Feature: showing off behave

  Scenario Outline: Page responce codes
    Given URL '<url>' as endpoint
    When we open expected page
    Then Verify that code is equal to '<code>'
    Examples:
      | url                                      | code |
      | https://docs.qameta.io/allure/#_python   | 200  |
      | https://jenkins.hillel.it/job/adasdasda/ | 404  |
      | https://www.wikipedia.org/               | 200  |
      | https://en.wikipedia.org/a               | 404  |
