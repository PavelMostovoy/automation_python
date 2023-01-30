Feature: showing off behave


  @smoke
  Scenario: run a simple test
    Given we have behave installed
    When we implement a test
    Then behave will test it for us!



  Scenario Outline: Name Comparison
    Given User '<login>' as admin
    When Add additional user '<additional name>'
    Then Compare Users names <case>
    Examples:
      | login | additional name | case |
      | Bob   | Bob             | 1    |
      | Bill  | Mike            | a    |
      | Mike  | Mike            | 1    |
      | Bob   | Mike            | 1    |
      | Bob   | Bob             | g   |
      | Bill  | Mike            | 1    |
      | Mike  | Mike            | 1    |
      | Bob   | Mike            | 1    |
      | Bob   | Bob             | t    |
      | Bill  | Mike            | 1    |
      | Mike  | Mike            | 1    |
      | Bob   | Mike            | t    |
      | Bob   | Bob             | 1    |
      | Bill  | Mike            | 1    |
      | Mike  | Mike            | t    |
      | Bob   | Mike            | 1    |

    @example_1
    Examples:
      | login | additional name | case |
      | Bob   | Bob             | 1    |
      | Bill  | Mike            | a    |
      | Mike  | Mike            | 1    |
      | Bob   | Mike            | 1    |
      | Bob   | Bob             | g   |
      | Bill  | Mike            | 1    |