from playwright.sync_api import sync_playwright, expect


def test_fill_practice_form():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        page = browser.new_page(viewport={'width': 1920, 'height': 1080})
        page.goto("https://demoqa.com/automation-practice-form")

        page.locator("#firstName").fill("Ivan")
        page.locator("#lastName").fill("Ivanov")
        page.locator("#userEmail").fill("ivan_ivanov@example.com")
        page.locator("#gender-radio-1").check(force=True)
        page.locator("#userNumber").fill("1234567890")

        subjects = page.locator("#subjectsInput")
        subjects.fill("Math")
        page.locator(".subjects-auto-complete__option").first.click()

        page.locator("#hobbies-checkbox-1")
        page.locator("#currentAddress").fill("123 Lenina St, Moscow, Russia")

        page.locator("#state").click()
        page.locator("#react-select-3-option-0").click()

        page.locator("#city").click()
        page.locator("#react-select-4-option-0").click()

        page.locator("#submit").click()
        page.wait_for_timeout(1000)
        modal_title = page.locator("#example-modal-sizes-title-lg")

        expect(modal_title).to_be_visible()
        expect(modal_title).to_have_text("Thanks for submitting the form")

        browser.close()
