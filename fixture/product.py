import re
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

    def load_file(self, field_name, file):
        wd = self.app.wd
        wd.find_element_by_name(field_name).send_keys(file)

    def open_tab(self, tab_name):
        wd = self.app.wd
        if tab_name == 'Information':
            wd.find_elements_by_css_selector("ul.index > li")[1].click()
        if tab_name == 'Prices':
            wd.find_elements_by_css_selector("ul.index > li")[3].click()

    def add_new(self, product):
        wd = self.app.wd
        time.sleep(1)
        self.app.admin.open_menu_item("Catalog")
        self.app.wait_until_element_present("a.button[href$=edit_product]")
        wd.find_element_by_css_selector("a.button[href$=edit_product]").click()
        self.app.wait_until_element_present("input[type=radio]")
        status = wd.find_elements_by_css_selector("#tab-general tr")[0]
        status.find_element_by_css_selector("[type=radio]").click()
        self.app.fill_field_value("name[en]", product.name)
        self.app.fill_field_value("code", product.code)
        categories = wd.find_elements_by_css_selector("#tab-general tr")[6]
        categories.find_element_by_css_selector("input[type=checkbox]").click()
        genders = wd.find_elements_by_css_selector("#tab-general tr")[11]
        genders.find_element_by_css_selector("input[type=checkbox]").click()
        self.app.fill_field_value("quantity", product.quantity)
        self.app.select_by_text("default_category_id", "Subcategory")
        self.app.select_by_text("quantity_unit_id", "pcs")
        self.app.select_by_text("delivery_status_id", "3-5 days")
        self.app.select_by_text("sold_out_status_id", "Temporary sold out")
        self.load_file("new_images[]", os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'snickers.jpg'))
        self.app.fill_field_value("date_valid_from", product.date_valid_from)
        self.app.fill_field_value("date_valid_to", product.date_valid_to)
        self.open_tab('Information')
        self.app.select_by_text("manufacturer_id", product.manufacturer)
        self.app.fill_field_value("keywords", product.keywords)
        self.app.fill_field_value("short_description[en]", product.short_description)
        wd.find_element_by_css_selector("div.trumbowyg-editor").send_keys(product.description)
        self.app.fill_field_value("head_title[en]", product.head_title)
        self.app.fill_field_value("meta_description[en]", product.meta_description)
        self.open_tab('Prices')
        self.app.fill_field_value("purchase_price", product.price)
        self.app.select_by_text("purchase_price_currency_code", "Euros")
        self.app.fill_field_value("prices[EUR]", product.price)
        wd.find_element_by_css_selector("[name=save]").click()

    def get_list(self):
        wd = self.app.wd
        self.app.admin.open_menu_item("Catalog")
        products = []
        rows = wd.find_elements_by_css_selector("tr.row")[2:]
        for row in rows:
            cells = row.find_elements_by_css_selector("td")
            name = cells[2].text
            products.append(name)
        return products

