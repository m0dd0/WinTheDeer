import os
import time
from datetime import datetime
import traceback

from selenium.webdriver import Chrome, ActionChains
from selenium.webdriver.chrome.options import Options

# TODO auf raspberry

BIRTHDAY_DD = ""
BIRTHDAY_MM = ""
BIRTHDAY_YYYY = ""
EMAIL = ""
PASSWORD = ""

while True:
    try:
        path_to_driver = os.path.join(
            os.path.dirname(os.path.realpath(__file__)), 'chromedriver_win32',
            'chromedriver')

        # opts = Options()
        # opts.set_headless()
        driver = Chrome(executable_path=str(path_to_driver),
                        # options=opts
                        )  # TODO make possible with headless driver
        # driver.fullscreen_window()
        driver.get('https://shop.jaegermeister.de/shotmachine')

        # accepting cookies is done because the "accept cookie" button woul shadow needed buttons
        # otherwise even if scrolled to elemnt
        driver.find_element_by_id('cookie-permission--accept-button').click()

        driver.find_element_by_id('agegate-dd').send_keys(BIRTHDAY_DD)
        driver.find_element_by_id('agegate-mm').send_keys(BIRTHDAY_MM)
        driver.find_element_by_id('agegate-yyyy').send_keys(BIRTHDAY_YYYY)

        jetzt_sichern_button = driver.find_element_by_xpath(
            '//button[text()="jetzt chance sichern "]')
        # driver.execute_script("arguments[0].scrollIntoView();",
        #                       jetzt_sichern_button)
        time.sleep(1)  # needed after scrolling
        jetzt_sichern_button.click()

        driver.find_element_by_id('email').send_keys(EMAIL)
        driver.find_element_by_id('passwort').send_keys(PASSWORD)

        anmelden_button = driver.find_element_by_xpath(
            '//button[text()="anmelden"]')
        # driver.execute_script("arguments[0].scrollIntoView();",
        #                       anmelden_button)
        time.sleep(1)  #  needed after scrolling
        anmelden_button.click()

        time.sleep(1)

        print('chance gesichert um {0}'.format(
            datetime.now().strftime("%H:%M:%S")))

        wait = 60 * 60 + 30

    except:
        print('error um {0}'.format(datetime.now().strftime("%H:%M:%S")))
        print(traceback.format_exc())

        wait = 30

    try:
        driver.delete_all_cookies()
        driver.close()
    except:
        print(traceback.format_exc())

    time.sleep(wait)