from playwright.sync_api import Page, expect


def test_new_tab_button(page: Page):
    page.goto("https://www.qa-practice.com/elements/new_tab/button")
    button = page.locator(".a-button")

    with page.expect_popup() as popup_info:
        button.click()
    new_page = popup_info.value

    expect(new_page.locator("#result")).to_have_text("I am a new page in a new tab")
    expect(button).to_be_enabled()
