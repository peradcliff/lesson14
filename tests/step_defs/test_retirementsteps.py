from pytest_bdd import scenario, given, when, then


@given("Someone has a birth year and month")
def step_impl():
    raise NotImplementedError(u'STEP: Given Someone has a birth year and month')


@when("the user enters their birth year and month")
def step_impl():
    raise NotImplementedError(u'STEP: When  the user enters their birth year and month')


@then("the program determines the year and month they will retire")
def step_impl():
    raise NotImplementedError(u'STEP: Then  the program determines the year and month they will retire')


@given("Birth year is 1995 and birth month February")
def step_impl():
    raise NotImplementedError(u'STEP: Given Birth year is 1995 and birth month February')


@when("the user enters these dates")
def step_impl():
    raise NotImplementedError(u'STEP: When the user enters these dates')


@then("the program determines they will determine retirement age at 67 in February 2062")
def step_impl():
    raise NotImplementedError(
        u'STEP: Then the program determines they will determine retirement age at 67 in February 2062')


@given("User enters their birth month and year")
def step_impl():
    raise NotImplementedError(u'STEP: Given User enters their birth month and year')


@when("the user hits enter after each it will process it")
def step_impl():
    raise NotImplementedError(u'STEP: When the user hits enter after each it will process it')


@then("the program will determine the date of retirement to the month and year")
def step_impl():
    raise NotImplementedError(u'STEP: Then the program will determine the date of retirement to the month and year')


@given("a birth year less than 1900")
def step_impl():
    raise NotImplementedError(u'STEP: Given a birth year less than 1900')


@when("the user enters this dates")
def step_impl():
    raise NotImplementedError(u'STEP: When the user enters this dates')


@then("the program will raise a value error")
def step_impl():
    raise NotImplementedError(u'STEP: Then the program will raise a value error')


@given("a birth year greater than or equal to 3000")
def step_impl():
    raise NotImplementedError(u'STEP: Given a birth year greater than or equal to 3000')


@then("the program will assert 1936 equals respetive retirement age")
def step_impl():
    raise NotImplementedError(u'STEP: Then the program will assert 1936 equals respetive retirement age')


@given("a birth year in range of 1937 and 1943")
def step_impl():
    raise NotImplementedError(u'STEP: Given a birth year in range of 1937 and 1943')


@then("the program will asert birth year equals respetive retirement age")
def step_impl():
    raise NotImplementedError(u'STEP: Then the program will asert birth year equals respetive retirement age')


@given("a birth year above 1959")
def step_impl():
    raise NotImplementedError(u'STEP: Given a birth year above 1959')


@given("a birth month is greater than 12")
def step_impl():
    raise NotImplementedError(u'STEP: Given a birth month is greater than 12')


@given("a birth month is less than 1")
def step_impl():
    raise NotImplementedError(u'STEP: Given a birth month is less than 1')
