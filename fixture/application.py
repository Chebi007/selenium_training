from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from fixture.session import SessionHelper
from fixture.admin import AdminHelper
from fixture.main import MainHelper
from fixture.product import ProductHelper
from fixture.customer import CustomerHelper
from fixture.cart import CartHelper


class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.admin = AdminHelper(self)
        self.main = MainHelper(self)
        self.product = ProductHelper(self)
        self.account = CustomerHelper(self)
        self.cart = CartHelper(self)

    def open_admin_page(self):
        wd = self.wd
        if not wd.current_url.endswith("/admin/"):
            wd.get('http://localhost/litecart/admin/')

    def open_main_page(self):
        wd = self.wd
        if not wd.current_url.endswith("/litecart/en/"):
            wd.get('http://localhost/litecart/en/')

    def is_element_present(self, css_locator):
        wd = self.wd
        try:
            wd.find_element_by_css_selector(css_locator)
            return True
        except NoSuchElementException:
            return False

    def destroy(self):
        self.wd.quit()

    def wait_until_element_present(self, locator):
        wd = self.wd
        wait = WebDriverWait(wd, 10)
        return wait.until(EC.presence_of_element_located(locator))

    def wait_until_text_to_be_present_in_element(self, locator, text):
        wd = self.wd
        wait = WebDriverWait(wd, 10)
        return wait.until(EC.text_to_be_present_in_element(locator, text))

    def wait_until_staleness_of_element(self, element):
        wd = self.wd
        wait = WebDriverWait(wd, 10)
        return wait.until(EC.staleness_of(element))

    def fill_field_value(self, field_name, text):
        wd = self.wd
        wd.find_element_by_name(field_name).click()
        wd.find_element_by_name(field_name).send_keys(text)

    def select_by_text(self, field_name, text):
        wd = self.wd
        select = Select(wd.find_element_by_name(field_name))
        select.select_by_visible_text(text)