from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 10)

url = "https://demoqa.com/automation-practice-form"

# Текстовые поля
input_first_name = ('xpath', '//input[@id="firstName"]')
input_last_name = ('xpath', '//input[@id="lastName"]')
input_email = ('xpath', '//input[@id="userEmail"]')
input_mobile = ('xpath', '//input[@id="userNumber"]')
input_current_address = ('xpath', '//textarea[@id="currentAddress"]')

# Радио-кнопки пола
radio_gender_male = ('xpath', '//label[@for="gender-radio-1"]')
radio_gender_female = ('xpath', '//label[@for="gender-radio-2"]')
radio_gender_other = ('xpath', '//label[@for="gender-radio-3"]')

# Дата рождения
input_date_of_birth = ('xpath', '//input[@id="dateOfBirthInput"]')
select_month = ('xpath', '//select[@class="react-datepicker__month-select"]')
select_year = ('xpath', '//select[@class="react-datepicker__year-select"]')

# Предметы
input_subjects = ('xpath', '//input[@id="subjectsInput"]')
div_subjects_container = ('xpath', '//div[@id="subjectsContainer"]')

# Чекбоксы хобби
checkbox_sports = ('xpath', '//label[@for="hobbies-checkbox-1"]')
checkbox_reading = ('xpath', '//label[@for="hobbies-checkbox-2"]')
checkbox_music = ('xpath', '//label[@for="hobbies-checkbox-3"]')

# Загрузка изображения
input_picture = ('xpath', '//input[@id="uploadPicture"]')

# Выпадающие списки штата и города
input_state = ('xpath', '//input[@id="react-select-3-input"]')
input_city = ('xpath', '//input[@id="react-select-4-input"]')

# Кнопка отправки
button_submit = ('xpath', '//button[@id="submit"]')

modal_content = ('class name', 'modal-content')
modal_rows = ('tag name', 'tr')
modal_cells = ('tag name', 'td')


def test_submit_form_with_valid_data():
    driver.get(url)

    driver.find_element(*input_first_name).send_keys("John")
    driver.find_element(*input_last_name).send_keys("Doe")
    driver.find_element(*input_email).send_keys("john.doe@example.com")
    driver.find_element(*radio_gender_male).click()
    driver.find_element(*input_mobile).send_keys("1234567890")
    driver.find_element(*input_date_of_birth).click()
    driver.find_element(*input_date_of_birth).send_keys(Keys.ENTER)
    driver.find_element(*input_subjects).send_keys("Math")
    driver.find_element(*input_subjects).send_keys(Keys.ENTER)
    driver.find_element(*checkbox_sports).click()
    driver.find_element(*input_current_address).send_keys("123 Test Street")
    driver.find_element(*input_state).send_keys("NCR")
    driver.find_element(*input_state).send_keys(Keys.ENTER)
    driver.find_element(*input_city).send_keys("Delhi")
    driver.find_element(*input_city).send_keys(Keys.ENTER)
    driver.find_element(*button_submit).click()
    modal = wait.until(EC.presence_of_element_located(modal_content))
    table_rows = modal.find_elements(*modal_rows)

    print("\nРезультаты отправки формы:")
    print("-" * 50)
    for row in table_rows:
        cells = row.find_elements(*modal_cells)
        if len(cells) >= 2:
            print(f"{cells[0].text}: {cells[1].text}")
    print("-" * 50)
