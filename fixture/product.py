import re
from selenium.webdriver.support.ui import Select
import os.path
from model.product import Product
import time


class ProductHelper:

    def __init__(self, app):
        self.app = app

    def get_product_by_index_on_main_page(self, index, block):
        wd = self.app.wd
        self.app.open_main_page()
        row = wd.find_elements_by_css_selector("#box-%s li" % block)[index]
        name = row.find_element_by_css_selector(".name").text
        regular_price = row.find_element_by_css_selector(".regular-price").text
        campaign_price = row.find_element_by_css_selector(".campaign-price").text
        return Product(name=name, regular_price=regular_price, campaign_price=campaign_price)

    def get_product_by_index_on_edit_page(self, index, block):
        wd = self.app.wd
        self.app.open_main_page()
        wd.find_elements_by_css_selector("#box-%s li" % block)[index].click()
        name = wd.find_element_by_css_selector("h1.title").text
        regular_price = wd.find_element_by_css_selector(".regular-price").text
        campaign_price = wd.find_element_by_css_selector(".campaign-price").text
        return Product(name=name, regular_price=regular_price, campaign_price=campaign_price)

    def get_css_properties_for_regular_price_on_main_page(self):
        wd = self.app.wd
        self.app.open_main_page()
        dict = {}
        row = wd.find_elements_by_css_selector("#box-campaigns li")[0]
        dict["color"] = self.get_numbers(row.find_element_by_css_selector(".regular-price").value_of_css_property("color"))
        dict["text_decoration_line"] = row.find_element_by_css_selector(".regular-price").value_of_css_property("text-decoration-line")
        dict["font_size"] = self.get_numbers(row.find_element_by_css_selector(".regular-price").value_of_css_property("font-size"))[0]
        return dict

    def get_css_properties_for_campaign_price_on_main_page(self):
        wd = self.app.wd
        self.app.open_main_page()
        dict = {}
        row = wd.find_elements_by_css_selector("#box-campaigns li")[0]
        dict["color"] = self.get_numbers(row.find_element_by_css_selector(".campaign-price").value_of_css_property("color"))
        dict["font_weight"] = row.find_element_by_css_selector(".campaign-price").value_of_css_property("font-weight")
        dict["font_size"] = self.get_numbers(row.find_element_by_css_selector(".campaign-price").value_of_css_property("font-size"))[0]
        return dict

    def get_css_properties_for_regular_price_on_edit_page(self):
        wd = self.app.wd
        self.app.open_main_page()
        wd.find_elements_by_css_selector("#box-campaigns li")[0].click()
        dict = {}
        dict["color"] = self.get_numbers(wd.find_element_by_css_selector(".regular-price").value_of_css_property("color"))
        dict["text_decoration_line"] = wd.find_element_by_css_selector(".regular-price").value_of_css_property("text-decoration-line")
        dict["font_size"] = self.get_numbers(wd.find_element_by_css_selector(".regular-price").value_of_css_property("font-size"))[0]
        return dict

    def get_css_properties_for_campaign_price_on_edit_page(self):
        wd = self.app.wd
        self.app.open_main_page()
        wd.find_elements_by_css_selector("#box-campaigns li")[0].click()
        dict = {}
        dict["color"] = self.get_numbers(wd.find_element_by_css_selector(".campaign-price").value_of_css_property("color"))
        dict["font_weight"] = wd.find_element_by_css_selector(".campaign-price").value_of_css_property("font-weight")
        dict["font_size"] = self.get_numbers(wd.find_element_by_css_selector(".campaign-price").value_of_css_property("font-size"))[0]
        return dict

    def get_numbers(self, str):
        return re.findall('[\d\.\d]+', str)

    def fill_field_value(self, field_name, text):
        wd = self.app.wd
        wd.find_element_by_name(field_name).click()
        wd.find_element_by_name(field_name).send_keys(text)

    def select_by_text(self, field_name, text):
        wd = self.app.wd
        select = Select(wd.find_element_by_name(field_name))
        select.select_by_visible_text(text)

    def load_file(self, field_name, file):
        wd = self.app.wd
        wd.find_element_by_name(field_name).send_keys(file)

    def add_new_product(self):
        wd = self.app.wd
        self.app.wait_until_element_present("li#app- a[href$=catalog]")
        self.app.admin.open_menu_item("Catalog")
        wd.find_element_by_css_selector("a.button[href$=edit_product]").click()

        status =wd.find_elements_by_css_selector("#tab-general tr")[0]
        status.find_element_by_css_selector("[type=radio]").click()

        self.fill_field_value("name[en]", "Liliiaa")
        self.fill_field_value("code", "123456")
        categories = wd.find_elements_by_css_selector("#tab-general tr")[6]
        categories.find_element_by_css_selector("input[type=checkbox]").click()
        genders = wd.find_elements_by_css_selector("#tab-general tr")[11]
        genders.find_element_by_css_selector("input[type=checkbox]").click()
        self.fill_field_value("quantity", "25")
        self.select_by_text("default_category_id", "Subcategory")
        self.select_by_text("quantity_unit_id", "pcs")
        self.select_by_text("delivery_status_id", "3-5 days")
        self.select_by_text("sold_out_status_id", "Temporary sold out")
        self.load_file("new_images[]", os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'snickers.jpg'))
        self.fill_field_value("date_valid_from", "2020-04-04")
        self.fill_field_value("date_valid_to", "2020-04-30")
        wd.find_element_by_css_selector("[name=save]").click()

