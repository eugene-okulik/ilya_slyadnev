from playwright.sync_api import Page, expect


def test_okulik_page(page: Page):
    page.goto("https://okulik.by/")

    expect(page).to_have_url("https://okulik.by/")

    text_element = page.get_by_text("Меня зовут Евгений Окулик")
    expect(text_element).to_be_visible()
