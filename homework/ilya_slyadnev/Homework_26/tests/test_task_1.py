from playwright.sync_api import expect


def test_form_authentication(page):
    page.goto("https://the-internet.herokuapp.com/")
    page.get_by_role("link", name="Form Authentication").click()

    page.get_by_role("textbox", name="Username").fill("tomsmith")
    page.get_by_role("textbox", name="Password").fill("SuperSecretPassword!")
    page.get_by_role("button", name="Login").click()

    expect(page.get_by_role("heading", name="Welcome to the Secure Area")).to_be_visible()
