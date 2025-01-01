from utils.user_data import Users
from playwright.sync_api import expect


class TestRegistrationPage:
    def test_valid_registration(self, account_page):
        account_page.open()
        account_page.click_consent_button()

        account_page.create_account(
            firstname=Users.firstname,
            lastname=Users.lastname,
            email=Users.email,
            password=Users.password,
        )

        expect(account_page.success).to_be_visible()

    def test_short_password(self, account_page):
        account_page.open()
        account_page.click_consent_button()

        account_page.create_account(
            firstname=Users.firstname,
            lastname=Users.lastname,
            email=Users.email,
            password="lol",
        )

        expect(account_page.password_error).to_have_text(
            "Minimum length of this field must be equal or greater "
            "than 8 symbols. Leading and trailing spaces will be "
            "ignored."
        )

    def test_empty_email(self, account_page):
        account_page.open()
        account_page.click_consent_button()

        account_page.create_account(
            firstname=Users.firstname,
            lastname=Users.lastname,
            email=" ",
            password=Users.password,
        )

        expect(account_page.email_error).to_have_text(
            "This is a required field."
        )
