from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest


class TestAbs(unittest.TestCase):

    def test_registration1(self):  # ✅ метод начинается с test_ и имеет self
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()

        try:
            browser.get(link)

            # Заполняем обязательные поля
            input1 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your first name']")
            input1.send_keys("Regina")

            input2 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your last name']")
            input2.send_keys("Shem")

            input3 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your email']")
            input3.send_keys("0707@mail.ru")

            # Отправляем форму
            button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
            button.click()

            # Ждем загрузки
            time.sleep(1)

            # Проверяем результат
            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            welcome_text = welcome_text_elt.text

            # ✅ Правильное использование self.assertEqual()
            expected_text = "Congratulations! You have successfully registered!"
            self.assertEqual(
                expected_text,
                welcome_text,
                f"Expected '{expected_text}', but got '{welcome_text}'"
            )

        finally:
            time.sleep(10)
            browser.quit()

    def test_registration2(self):  # ✅ метод начинается с test_ и имеет self
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()

        try:
            browser.get(link)

            # Заполняем обязательные поля
            input1 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your first name']")
            input1.send_keys("Regina")

            input2 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your last name']")
            input2.send_keys("Shem")

            input3 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your email']")
            input3.send_keys("0707@mail.ru")

            # Отправляем форму
            button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
            button.click()

            # Ждем загрузки
            time.sleep(1)

            # Проверяем результат
            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            welcome_text = welcome_text_elt.text

            # ✅ Правильное использование self.assertEqual()
            expected_text = "Congratulations! You have successfully registered!"
            self.assertEqual(
                expected_text,
                welcome_text,
                f"Expected '{expected_text}', but got '{welcome_text}'"
            )

        finally:
            time.sleep(10)
            browser.quit()


if __name__ == "__main__":
    unittest.main()