Feature: showing off behave

  Scenario Outline: Page responce codes
    Given URL '<url>' as endpoint
    When we open expected page
    Then Verify that code is equal to '<code>'
    Examples:
      | url    | code |
      | first  | 200  |
      | second | 403  |
      | third  | 200  |
      | fourth | 404  |
      | fifth  | 500  |
      | six    | 403  |
      | seven  | 200  |
