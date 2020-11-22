Feature: Retirement Calculator
  Calculating the age someone will
  retire based on the year and
  month they were born.

  Scenario: birth year 1900
	Given a birth year less than 1900
	When the user enters this dates
	Then the program will raise a value error

  Scenario: birth year <= 3000
	Given a birth year greater than or equal to 3000
	When the user enters this dates
	Then the program will raise a value error

  Scenario: birth year > 1937
	Given a birth year less than 1937
	When the user enters this dates
	Then the program will assert 1936 equals respective retirement age

  Scenario: 1937 > birth year < 1943
	Given a birth year in range of 1937 and 1943
	When the user enters this dates
	Then the program will asert birth year equals respective retirement age

  Scenario: 1943 > birth year < 1954
	Given a birth year in range of 1943 and 1954
	When the user enters this dates
	Then the program will asert birth year equals respective retirement age

  Scenario: 1954 > birth year < 1960
	Given a birth year in range of 1954 and 1960
	When the user enters this dates
	Then the program will asert birth year equals respective retirement age

  Scenario: birth year > 1959
	Given a birth year above 1959
	When the user enters this dates
	Then the program will asert birth year equals respective retirement age

  Scenario: birth year > 1900
	Given a birth year above 1900
	When the user enters this dates
	Then the program will raise a value error


  Scenario: birth month > 12
	Given a birth month is greater than 12
    When the user enters this dates
    Then the program will raise a value error

  Scenario: birth month < 1
   	Given a birth month is less than 1
    When the user enters this dates
    Then the program will raise a value error


    # example of birth year of 2000 and birth month of 07
  Scenario Outline: My birthday
    Given Birth year is 2000 and birth month July
    When the user enters these dates
    Then the program determines they will determine retirement age at 67 in July of 2067
    Examples:
      | birth_year | birth_month | age_years | ret_year | ret_month |
      | 2000       | 07          | 67        | 2067     | 07        |
