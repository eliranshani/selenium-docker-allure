# coding=utf-8
import helpers.helpers as utils
import pytest
from selenium.webdriver.common.by import By


def submit_form(driver):
    driver.find_element(By.XPATH, "//input[@type='submit']").click()


def find_flight_in_dropdown(dropdown_element, expected_flight):
    for option in dropdown_element.find_elements_by_tag_name('option'):
        if option.text == expected_flight:
            option.click()


def choose_departure_flight(driver, departure_flight):
    from_port_dropdown = utils.find_element(driver, By.NAME, "fromPort")
    find_flight_in_dropdown(dropdown_element=from_port_dropdown, expected_flight=departure_flight)


def choose_arrival_flight(driver, arrival_flight):
    to_port_dropdown = utils.find_element(driver, By.NAME, "toPort")
    find_flight_in_dropdown(dropdown_element=to_port_dropdown, expected_flight=arrival_flight)


@pytest.fixture(scope="function")
def open_blazedemo(driver, url):
    driver.get(url)
    driver.find_element(By.TAG_NAME, "form")
    assert driver.title == "BlazeDemo"


@pytest.mark.parametrize('from_port, to_port', [
    ("Paris", "Buenos Aires"),
    ("Philadelphia", "Rome"),
    ("Boston", "London"),
    ("Portland", "Berlin"),
    ("San Diego", "New York"),
    ("Mexico City", "Dublin"),
    # fail on purpose to verify screenshot was added to allure report
    ("Tel Aviv", "Dubai")
])
def test_find_flights(driver, open_blazedemo, from_port, to_port):

    # Find flight
    choose_departure_flight(driver, departure_flight=from_port)
    choose_arrival_flight(driver, arrival_flight=to_port)
    submit_form(driver)

    assert from_port in utils.get_text(driver, By.TAG_NAME, "h3"), "{} was not found".format(from_port)
    assert to_port in utils.get_text(driver, By.TAG_NAME, "h3"), "{} was not found".format(to_port)
    assert "reserve.php" in driver.current_url

    # Choose flight
    submit_form(driver)

    assert from_port in utils.get_text(driver, By.TAG_NAME, "h2"), "{} was not found".format(from_port)
    assert to_port in utils.get_text(driver, By.TAG_NAME, "h2"), "{} was not found".format(to_port)
    assert "purchase.php" in driver.current_url

    # Purchase flight
    submit_form(driver)

    assert "Thank you for your purchase today!" in utils.get_text(driver, By.TAG_NAME, "h1")
    assert "confirmation.php" in driver.current_url


def test_teardown(driver):
    driver.quit()
