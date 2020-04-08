from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from fixture.session import SessionHelper
from fixture.admin import AdminHelper
from fixture.main import MainHelper
from fixture.product import ProductHelper
from fixture.customer import CustomerHelper


class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.admin = AdminHelper(self)
        self.main = MainHelper(self)
        self.product = ProductHelper(self)
        self.account = CustomerHelper(self)

    def open_admin_page(self):
        wd = self.wd
        if not wd.current_url.endswith("/admin/"):
            wd.get('http://localhost/litecart/admin/')

    def open_main_page(self):
        wd = self.wd
        if not wd.current_url.endswith("/litecart/en/"):
            wd.get('http://localhost/litecart/en/')

    #def is_element_present(self, *args):
        #wd = self.wd
        #try:
            #wd.find_element(*args)
            #return True
        #except NoSuchElementException:
            #return False

    def destroy(self):
        self.wd.quit()

    def is_element_present(self, locator):
        wd = self.wd
        wait = WebDriverWait(wd, 10)
        return wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "%s" % locator)))