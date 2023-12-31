import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome(
        r"C:\Users\green\PycharmProjects\Module_25\chromedriver.exe")
    pytest.driver.implicitly_wait(10)
    pytest.driver.get('http://petfriends.skillfactory.ru/login')

    yield

    pytest.driver.quit()


def test_show_all_pets():
    """Проверяем, что на станице all_pets во всех карточках
    питомцев присутствуют: фото, имя, информация о питомце"""


    pytest.driver.find_element(By.ID, 'email').send_keys('ksyu_3@mail.ru')
    pytest.driver.find_element(By.ID, 'pass').send_keys('123456')
    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    images = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-img-top')
    names = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-title')
    descriptions = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-text')

    for i in range(len(names)):
        assert images[i].get_attribute('src') != ''
        assert names[i].text != ''
        assert descriptions[i].text != ''
        assert ', ' in descriptions[i]
        parts = descriptions[i].text.split(", ")
        assert len(parts[0]) > 0
        assert len(parts[1]) > 0