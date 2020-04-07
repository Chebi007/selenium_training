import re
from model.product import Product


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
