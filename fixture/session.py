from selenium.webdriver.common.by import By


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login_on_admin_page(self, username, password):
        wd = self.app.wd
        self.app.open_admin_page()
        wd.find_element_by_name("username").click()
        wd.find_element_by_name("username").clear()
        wd.find_element_by_name("username").send_keys(username)
        wd.find_element_by_name("password").click()
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys(password)
        wd.find_element_by_name("login").click()

    def logout_on_admin_page(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("a[title='Logout']").click()

    def login_on_main_page(self, customer):
        wd = self.app.wd
        self.app.wait_until_element_present((By.NAME, "email"))
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(customer.email)
        wd.find_element_by_name("password").click()
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys(customer.password)
        wd.find_element_by_name("login").click()

    def logout_on_main_page(self):
        wd = self.app.wd
        element = wd.find_element_by_css_selector("#box-account li>a[href*=logout]")
        wd.execute_script("arguments[0].click();", element)