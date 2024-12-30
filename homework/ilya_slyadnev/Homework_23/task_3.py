from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_single_select():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    driver.get("https://www.qa-practice.com/elements/select/single_select")

    select_element = driver.find_element("id", "id_choose_language")
    select = Select(select_element)
    select.select_by_visible_text("Python")

    submit_button = driver.find_element("id", "submit-id-submit")
    submit_button.click()

    result = wait.until(EC.presence_of_element_located(("id", "result-text")))
    assert result.text == "Python", f"Ожидался текст 'Python', получено: {result.text}"

    print("Тест успешно пройден!")
    driver.quit()


def test_dynamic_loading():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
    start_button = driver.find_element("css selector", "#start button")
    start_button.click()
    hello_text = wait.until(
        EC.presence_of_element_located(("css selector", "#finish h4"))
    )

    assert hello_text.text == "Hello World!", f"Ожидался текст 'Hello World!', получено: {hello_text.text}"

    print("Тест успешно пройден!")
    driver.quit()
