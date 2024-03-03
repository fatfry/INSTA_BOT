import os
import time
import logging

from dotenv import load_dotenv

from selenium import webdriver

from consts import LOGIN_URL, PROFILE_URL, LOOPS, FOLLOW_BUTTON_CSS_SELECTOR, UNFOLLOW_BUTTON_CSS_SELECTOR
from utils import waiting_for_load_page, login_to_inst, open_profile, click_followers_button, loop_unfollow, \
    click_followers_window_to_close

load_dotenv('.env.dev')
logging.basicConfig(filename='logs.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

username = os.getenv('INSTA_USERNAME')
password = os.getenv('PASSWORD')

driver = webdriver.Chrome()
logging.info('Драйвер запущен')

driver.get(LOGIN_URL)
logging.info('Открыта страница входа в Instagram')
waiting_for_load_page(logging)
logging.info('Начало работы скрипта')
try:
    login_to_inst(driver, username, password, logging)
    open_profile(driver, logging, PROFILE_URL)

    for _ in range(LOOPS):
        click_followers_button(driver, logging)
        loop_unfollow(driver, logging)
        click_followers_window_to_close(driver, logging)  # закрываем окно подписок


finally:
    # Закрытие браузера
    time.sleep(30)
    driver.quit()
    logging.info('Завершение работы скрипта')
