from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

URL = "https://magento.softwaretestingboard.com/gear/bags.html"

# locators
_first_product = ("css selector", ".product-item:first-child")
_add_to_compare = ("css selector", ".product-item:first-child .tocompare")
_product_name = ("css selector", ".product-item:first-child .product-item-link")
_compare_section = ("css selector", ".block-compare")
_compare_product_name = ("css selector", ".block-compare .product-item-name")


def test_add_to_compare(driver):
    driver.get(URL)

    product_name = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(_product_name)
    ).text

    first_product = driver.find_element(*_first_product)
    ActionChains(driver).move_to_element(first_product).perform()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(_add_to_compare)
    ).click()

    compare_product = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(_compare_product_name)
    ).text

    assert compare_product == product_name
