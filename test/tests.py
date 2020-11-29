import unittest
import requests
import pickle

from googlesearch import search
from time import sleep
from selenium import webdriver


""" 
Тестовое задание для инженера по автоматизированному тестированию ПО
ООО "Лидер Тестирования"

Выполнено: Кирьянов Евгений

1. Напиши автотест на вход в почтовый ящик на www.yandex.ru.

2. Напиши автотест на Гугл-поиск. В поисковую строку вводятся слова
«купить кофемашину bork c804», результатов больше 10 и в выдаче
присутствует mvideo.ru.

3. Зайди на www.reqres.in и напиши автотест на тестирование эндпоинта [GET]
SINGLE USER.
Должна осуществляться проверка, что сервер возвращает статус 200 и
first_name = “Janet”
(опционально)
"""


LINK_TO_CHECK = "https://yandex.ru/"
YANDEX_USERNAME = "Eu-Ki-999"
YANDEX_PASSWORD = "pingvin28"
GOOGLE_REQUEST = "купить кофемашину bork c804 AND mvideo"
LINK_ENDPOINT_GET = "www.reqres.in/single-user/"

# Code part


class TestLiderTesting(unittest.TestCase):

    def test_enter_to_yandex_mail_box_using_selenium(self):
        """
        Вход в почтовый ящик на www.yandex.ru
        """
        option = webdriver.FirefoxOptions()
        option.set_preference('dom.webdriver.enabled', False)
        option.set_preference('dom.webnotifications.enabled', False)

        driver = webdriver.Firefox()
        driver.get(LINK_TO_CHECK)
       
        element_button_to_enter = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[1]/div/a")
        link_to_email_autoriz = element_button_to_enter.get_attribute('href')

        driver.get(link_to_email_autoriz) # get link to authorization page

        element_login = driver.find_element_by_id("passp-field-login") # get Loggin field
        element_login.send_keys(YANDEX_USERNAME)

        element_button = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div[1]/form/div[3]/button")
        element_button.click()
        sleep(2)

        element_password = driver.find_element_by_id("passp-field-passwd") # get Password field
        element_password.send_keys(YANDEX_PASSWORD)

        element_button = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/form/div[3]/button")
        element_button.click()
        sleep(2)

    def test_google_search_using_google_search(self):
        """
        В поисковую строку вводятся слова «купить кофемашину bork c804», 
        результатов больше 10 и в выдаче присутствует mvideo.ru.
        """
        expected_result = False
        search_result = search(GOOGLE_REQUEST, num_results=20) # Get results og google search
        counter = 0

        for result in search_result:
            counter += 1
            if "mvideo.ru" in result:
                expected_result = True

        if counter <= 10:
            expected_result = False

        self.assertEqual(expected_result, True) 

    def a_test_google_search_using_using_selenium(self):
        """
        Before run this script, create "cookie" file,
        Nearby this script you can find "get_cookies.py", run it and falow the instructions inside.
        """
        option = webdriver.FirefoxOptions()
        option.set_preference('dom.webdriver.enabled', False)
        option.set_preference('dom.webnotifications.enabled', False)

        driver = webdriver.Firefox(options=option)
        driver.get("https://www.google.com")

        for cookie in pickle.load(open('cookies', 'rb')):
            driver.add_cookie(cookie)
        
        driver.refresh()

        sleep(5)

        element_field = driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[2]/div[1]/div[1]/div/div[2]/input")
        element_field.send_keys(GOOGLE_REQUEST)

        search_button = driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[2]/div[1]/div[3]/center/input[1]")
        search_button.click()


    def test_endpoint_get_single_user_on_reqres_using_requests(self):
        expected_result = "<Response [200]>"
        try:
            response = requests.get(LINK_ENDPOINT_GET)
        except requests.exceptions.RequestException as err:
            print(err)
            response = "<Response [400]>"
        
        self.assertEqual(expected_result, response) 


# Business logic part


def main():
    unittest.main()


if __name__ == "__main__":
    main()