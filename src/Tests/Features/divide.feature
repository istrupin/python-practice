Feature: Divide_Two
    Divide 2 numbers

Scenario Outline: Divide Two positive numbers
    Given Dividend of "<dividend>" and Divisor of "<divisor>"
    When I divide them
    Then Quotient should be accurate "<result>"

    Examples:
    | dividend | divisor | result |
    | 10       | 5       | 2      |
    | 10       | 3       | 3      |

Scenario: Divide Two negative numbers
    Given Dividend of "-10" and Divisor of "-5"
    When I divide them
    Then Quotient should be accurate "2"

Scenario: Divide positive by negative
    Given Dividend of "10" and Divisor of "-5"
    When I divide them
    Then Quotient should be accurate "-2"

Scenario: Divide negative by positive
    Given Dividend of "-10" and Divisor of "5"
    When I divide them
    Then Quotient should be accurate "-2"