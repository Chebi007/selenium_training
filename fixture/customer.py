from selenium.webdriver.support.ui import Select


class CustomerHelper:

    def __init__(self, app):
        self.app = app

    def fill_customer_from(self, customer):
        wd = self.app.wd
        self.app.is_element_present("[name=tax_id]")
        wd.find_element_by_css_selector("[name=tax_id]").click()
        wd.find_element_by_css_selector("[name=tax_id]").send_keys(customer.tax_id)
        wd.find_element_by_css_selector("[name=company]").click()
        wd.find_element_by_css_selector("[name=company]").send_keys(customer.company)
        wd.find_element_by_css_selector("[name=firstname]").click()
        wd.find_element_by_css_selector("[name=firstname]").send_keys(customer.firstname)
        wd.find_element_by_css_selector("[name=lastname]").click()
        wd.find_element_by_css_selector("[name=lastname]").send_keys(customer.lastname)
        wd.find_element_by_css_selector("[name=address1]").click()
        wd.find_element_by_css_selector("[name=address1]").send_keys(customer.address1)
        wd.find_element_by_css_selector("[name=address2").click()
        wd.find_element_by_css_selector("[name=address2").send_keys(customer.address2)
        wd.find_element_by_css_selector("[name=postcode]").click()
        wd.find_element_by_css_selector("[name=postcode]").send_keys(customer.postcode)
        wd.find_element_by_css_selector("[name=city]").click()
        wd.find_element_by_css_selector("[name=city]").send_keys(customer.city)

        select = wd.find_element_by_css_selector("select[name=country_code]")
        wd.execute_script("arguments[0].selectedIndex = 224; arguments[0].dispatchEvent(new Event('change'))", select)

        select2 = Select(wd.find_element_by_css_selector("select[name=zone_code]"))
        select2.select_by_visible_text(customer.zone_code)

        wd.find_element_by_css_selector("[name=email]").click()
        wd.find_element_by_css_selector("[name=email]").send_keys(customer.email)
        wd.find_element_by_css_selector("[name=phone").click()
        wd.find_element_by_css_selector("[name=phone").send_keys(customer.phone)
        wd.find_element_by_css_selector("[name=password").click()
        wd.find_element_by_css_selector("[name=password").send_keys(customer.password)
        wd.find_element_by_css_selector("[name=confirmed_password").click()
        wd.find_element_by_css_selector("[name=confirmed_password").send_keys(customer.confirmed_password)

    def create_account(self, customer):
        wd = self.app.wd
        self.app.open_main_page()
        wd.find_element_by_css_selector("[href$=create_account]").click()
        self.fill_customer_from(customer)
        wd.find_element_by_css_selector("[name=create_account").click()


