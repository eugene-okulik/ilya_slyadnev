from playwright.sync_api import Page, expect


def test_wait_for_red_button(page: Page):
    page.goto("https://demoqa.com/dynamic-properties")

    color_button = page.locator("#colorChange")
    expect(color_button).to_have_css("color", "rgb(220, 53, 69)")
    color_button.click()
