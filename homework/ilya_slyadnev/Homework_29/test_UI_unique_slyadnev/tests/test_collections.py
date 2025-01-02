from playwright.sync_api import expect


class TestCollectionsPage:
    def test_products_display(self, collections_page):
        collections_page.open()
        collections_page.click_consent_button()
        products_count = collections_page.get_products_count()

        assert products_count > 0, "На странице нет товаров"

    def test_sort_dropdown_presence(self, collections_page):
        collections_page.open()
        collections_page.click_consent_button()

        expect(collections_page.sorter).to_be_visible()

    def test_page_title(self, collections_page):
        collections_page.open()
        collections_page.click_consent_button()

        expect(collections_page.title).to_have_text("Eco Friendly")
