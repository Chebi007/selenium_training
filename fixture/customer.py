from selenium.webdriver.support.ui import Select


class CustomerHelper:

    def __init__(self, app):
        self.app = app

    def fill_field_value(self, field_name, text):
        wd = self.app.wd
        wd.find_element_by_name(field_name).click()
        wd.find_element_by_name(field_name).send_keys(text)

    def fill_account_form(self, customer):
        wd = self.app.wd
        self.app.wait_until_element_present("[name=tax_id]")
        self.fill_field_value('tax_id', customer.tax_id)
        self.fill_field_value('company', customer.company)
        self.fill_field_value('firstname', customer.firstname)
        self.fill_field_value('lastname', customer.lastname)
        self.fill_field_value('address1', customer.address1)
        self.fill_field_value('address2', customer.address2)
        self.fill_field_value('postcode', customer.postcode)
        self.fill_field_value('city', customer.city)
        select = wd.find_element_by_css_selector("select[name=country_code]")
        wd.execute_script("arguments[0].selectedIndex = 224; arguments[0].dispatchEvent(new Event('change'))", select)
        Select(wd.find_element_by_css_selector("select[name=zone_code]")).select_by_visible_text(customer.zone_code)
        self.fill_field_value('email', customer.email)
        self.fill_field_value('phone', customer.phone)
        self.fill_field_value('password', customer.password)
        self.fill_field_value('confirmed_password', customer.confirmed_password)

    def create_account(self, customer):
        wd = self.app.wd
        self.app.open_main_page()
        wd.find_element_by_css_selector("[href$=create_account]").click()
        self.fill_account_form(customer)
        wd.find_element_by_css_selector("[name=create_account").click()


