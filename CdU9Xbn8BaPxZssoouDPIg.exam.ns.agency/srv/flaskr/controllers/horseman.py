import urllib.parse
import logging
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-setuid-sandbox')

log = logging.getLogger(__name__)

# export OBJC_DISABLE_INITIALIZE_FORK_SAFETY=YES

class Spooky(object):
    driver = None

    def __init__(self, cookie=None):
        if self.driver is None:

            # TODO: fix the phantomJS page rendering
            self.driver = webdriver.Chrome(chrome_options=chrome_options)
            self.driver.set_page_load_timeout(10)
            self.driver.set_window_size(1024, 768)

        if cookie:
            self.driver.get(cookie.get("domain"))
            cookie['domain'] = None # Clear the domain and use the current page
            self.driver.add_cookie(cookie)

    def __enter__(self):
        return self.driver

    def __exit__(self, type, value, traceback):
        self.driver.close()
        self.driver.quit()

    def get(self, url):
        self.driver.get(url)

    @staticmethod
    def make_cookie(domain, name, value, secure=False):
        ret = {'domain': domain, 'name': name, 'value': value, 'secure': secure}
        return ret


def check_alert(driver, flag):
    try:
        WebDriverWait(driver, 3).until(EC.alert_is_present(),'timed out waiting for alert')
        alert = driver.switch_to_alert()
        alert.accept()
        if flag in alert.getText():
            return True
        return False
    except Exception as e:
        return False


def xss_get(url, cookie_domain=None, cookie_name=None, cookie_value=None, user_agent=None):

    time.sleep(3)

    cookie = None
    if cookie_domain:
        base_url = urllib.parse.urlparse(cookie_domain)
        domain = "{}://{}".format(base_url.scheme, base_url.netloc)
        cookie = Spooky.make_cookie(domain, cookie_name, cookie_value)
        log.critical('Cookie: %s' % repr(cookie))


    url = domain + url

    log.critical("xss_get(%s, %s, %s, %s, %s)" % (url, cookie_domain, cookie_name, cookie_value, user_agent))

    with Spooky(cookie) as s:

        log.critical("HTTP GET {}".format(url))
        try:

            s.get(url)

            if check_alert(s, cookie_value):
                print('FLAG FOUND IN ALERT')
            elif cookie_value in s.page_source:
                print('FLAG FOUND!')
            else:
                print('FLAG NOT FOUND!')

        except Exception as e:
            log.exception(repr(e))

        log.critical("Test complete.")


