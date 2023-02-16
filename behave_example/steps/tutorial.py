import requests
from assertpy import assert_that
from behave import *

use_step_matcher("re")
url_data = {
        "first": "https://docs.qameta.io/allure/#_python",
        "second": "https://jenkins.hillel.it/job/adasdasda/",
        "third": "https://www.wikipedia.org/",
        "forth": "https://en.wikipedia.org/a ",
        "fifth": "https://www.wikipedia.net/ ",
        "six": "https://en.wikipedia.org/a"
}


@given('we have behave installed')
def step_impl(context):
    pass


@when('we implement a test')
def step_impl(context):
    assert True is not False


@then('behave will test it for us!')
def step_impl(context):
    assert context.failed is False


@given("User '(?P<name>.+)' as admin")
def implementaion(context, name):
    context.login = name
    print(f"user {name}")


@when("Add additional user '(?P<name>.*)'")
def second_user(context, name):
    context.second_name = name
    print(f"added name {name}")
    return name


@then("Compare Users names")
def some_name_(context):
    assert_that(context.login).is_not_none()


@given("URL '(?P<url>.+)' as endpoint")
def step_impl(context, url):
    """
    :type context: behave.runner.Context
    :type url: str
    """
    # url = url_data[url]
    url = url_data.get(url, "https://google.com")
    context.given_url = url


@when("we open expected page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    response = requests.get(context.given_url)
    context.received_response = response


@then("Verify that code is equal to '(?P<code>.*)'")
def step_impl(context, code):
    """
    :type context: behave.runner.Context
    :type code: str
    """
    code = int(code)
    response = context.received_response.status_code

    assert response == code, f"Expected {code} received: {response} "
