from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.common.exceptions import NoSuchElementException
from fixture.session import SessionHelper
from fixture.admin import AdminHelper
from fixture.main import MainHelper
from fixture.product import ProductHelper


class Application:

    def __init__(self):
        #binary = FirefoxBinary("C:\\Program Files\\Firefox Nightly\\firefox.exe")
        #self.wd = webdriver.Firefox(firefox_binary=binary, firefox_profile=webdriver.FirefoxProfile())
        self.wd = webdriver.Ie()
        self.wd.implicitly_wait(3)
        self.session = SessionHelper(self)
        self.admin = AdminHelper(self)
        self.main = MainHelper(self)
        self.product = ProductHelper(self)

    def open_admin_page(self):
        wd = self.wd
        if not wd.current_url.endswith("/admin/"):
            wd.get('http://localhost/litecart/admin/')

    def open_main_page(self):
        wd = self.wd
        if not wd.current_url.endswith("/litecart/en/"):
            wd.get('http://localhost/litecart/en/')

    def is_element_present(self, *args):
        wd = self.wd
        try:
            wd.find_element(*args)
            return True
        except NoSuchElementException:
            return False

    def destroy(self):
        self.wd.quit()
