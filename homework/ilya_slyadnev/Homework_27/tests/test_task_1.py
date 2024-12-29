from playwright.sync_api import Page, expect


def test_confirm_alert_ok_button(page: Page):
    page.goto("https://www.qa-practice.com/elements/alert/confirm")
    page.on("dialog", lambda dialog: dialog.accept())
    page.click(".a-button")

    expect(page.locator("#result-text")).to_have_text("Ok")
