import pytest
from selenium import webdriver
import time
import math


@pytest.fixture()
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(50)
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('urls', ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1",
                                  "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1",
                                  "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1",
                                  "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1"])
class TestLogin:
    def test_run_browser(self, browser, urls):
        link = f"{urls}"
        browser.get(link)
        # вычисляем формулу
        answer = str(math.log(int(time.time())))
        # вводим ответ
        input1 = browser.find_element_by_class_name("textarea.string-quiz__textarea.ember-text-area.ember-view")
        input1.send_keys(answer)
        # Жмем кнопку
        button = browser.find_element_by_class_name("submit-submission")
        button.click()
        # Ждем фидбека о том что ответ правильный
        msg1 = browser.find_element_by_class_name \
            ("smart-hints__feedback.hints__component.hints__component_showed.ember-view")
        assert msg1.text == "Correct!", "Should be equal messages"


if __name__ == "__main__":
    pytest.main()
