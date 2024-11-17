from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# Локаторы
input_text = ('xpath', '//input[@id="id_text_string"]')
button_submit = ('xpath', '//button[@type="submit"]')
result_text = ('xpath', '//p[@id="result-text"]')


def test_input_form():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    driver.get("https://www.qa-practice.com/elements/input/simple")
    test_text = "Valid-Text_123"
    input_field = driver.find_element(*input_text)
    input_field.clear()
    input_field.send_keys(test_text)
    input_field.send_keys(Keys.ENTER)

    print(f"Введенный текст: {test_text}")
    print(f"Полученный текст: {test_text}")

    assert test_text == test_text, "Введенный и полученный текст не совпадают!"

    driver.quit()
