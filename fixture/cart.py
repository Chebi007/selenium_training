from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from fixture.custom_wait import number_of_elements


class CartHelper:

    def __init__(self, app):
        self.app = app

    def add_item(self):
        wd = self.app.wd
        products = self.app.main.list_of_products()
        products[0].click()
        self.app.wait_until_element_present((By.NAME, "add_cart_product"))
        if self.app.is_element_present("select[name^=options]"):
            select = Select(wd.find_element_by_css_selector("select[name^=options]"))
            select.select_by_index('1')
            wd.find_element_by_css_selector("[name=add_cart_product]").click()
        else:
            wd.find_element_by_css_selector("[name=add_cart_product]").click()

    def check_quantity(self, quantity):
        self.app.wait_until_text_to_be_present_in_element((By.CSS_SELECTOR, "span.quantity"), quantity)

    def checkout(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("#cart a.link").click()

    def remove_item(self):
        wd = self.app.wd
        wd.find_elements_by_css_selector("[value=Remove]")[0].click()

    def add_and_remove_items(self, number):
        wd = self.app.wd
        wait = WebDriverWait(wd, 10)
        for i in range(1, number):
            self.add_item()
            self.check_quantity('%s' % i)
        self.checkout()
        for i in range(1, number):
            self.remove_item()
            wait.until(number_of_elements((By.CSS_SELECTOR, "#checkout-summary-wrapper tr"), 8 - i))