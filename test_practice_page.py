import pytest
from playwright.sync_api import Page, expect

BASE_URL = "https://rahulshettyacademy.com/AutomationPractice/"


@pytest.fixture(autouse=True)
def open_page(page: Page):
    page.goto(BASE_URL)


def test_select_dropdown_option(page: Page):
    dropdown = page.locator("#dropdown-class-example")
    dropdown.select_option("option2")
    expect(dropdown).to_have_value("option2")


def test_checkbox_check_and_uncheck(page: Page):
    checkbox = page.locator("#checkBoxOption1")

    checkbox.check()
    expect(checkbox).to_be_checked()

    checkbox.uncheck()
    expect(checkbox).not_to_be_checked()
