from playwright.sync_api import expect


class TestSalePage:
    def test_page_title(self, sale_page):
        sale_page.open()
        sale_page.click_consent_button()

        expect(sale_page.title).to_have_text("Sale")

    def test_view_side_bar(self, sale_page):
        sale_page.open()
        sale_page.click_consent_button()

        expect(sale_page.side_bar_menu).to_be_visible()

    def test_view_promo(self, sale_page):
        sale_page.open()
        sale_page.click_consent_button()

        expect(sale_page.promo_image).to_be_visible()
