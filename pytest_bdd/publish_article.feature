Feature: Blog
  A site where you can .

  Scenario Outline: Go to the page
    Given Our driver
    And Customized URL '<url>'

    When I navigate to the page

    Then Werify the page content

    Examples:
      | url                   | gg|
      | https://wikipedia.org | g|
      | https://aqa.science   |g |
      | https://google.com    | g|
      | https://adv.wiki      | g|

