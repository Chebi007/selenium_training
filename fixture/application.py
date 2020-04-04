from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from fixture.session import SessionHelper
from fixture.admin import AdminHelper


class Application:

    def __init__(self):
        binary = FirefoxBinary("C:\\Program Files\\Firefox Nightly\\firefox.exe")
        self.wd = webdriver.Firefox(firefox_binary=binary, firefox_profile=webdriver.FirefoxProfile())
        self.wd.implicitly_wait(3)
        self.session = SessionHelper(self)
        self.admin = AdminHelper(self)

    def open_admin_page(self):
        wd = self.wd
        if not wd.current_url.endswith("/admin/"):
            wd.get('http://localhost/litecart/admin/')

    def destroy(self):
        self.wd.quit()
