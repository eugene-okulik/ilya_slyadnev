from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://www.demoblaze.com/index.html"

# locators
_first_product = ("xpath", "//h4[@class='card-title']")
_price = ("xpath", "//h3[@class='price-container']")
_add_to_cart_button = ("xpath", "//a[contains(@class, 'btn-success')]")
_cart_link = ("xpath", "//a[@id='cartur']")
_cart_product_name = ("xpath", "//td[text()='Samsung galaxy s6']")
_cart_product_price = ("xpath", "//td[text()='360']")


def test_add_product_to_cart_from_new_tab(driver):
    driver.get(URL)

    first_product = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(_first_product)
    )
    product_name = first_product.text

    ActionChains(driver) \
        .key_down(Keys.COMMAND) \
        .click(first_product) \
        .key_up(Keys.COMMAND) \
        .perform()

    driver.switch_to.window(driver.window_handles[1])
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(_price))
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(_add_to_cart_button)).click()

    WebDriverWait(driver, 10).until(EC.alert_is_present()).accept()

    driver.close()
    driver.switch_to.window(driver.window_handles[0])

    driver.find_element(*_cart_link).click()
    cart_product = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(_cart_product_name)
    ).text

    assert cart_product == product_name, "Имя продукта не соответствует"
