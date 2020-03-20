from selenium import webdriver
from fixture.session import SessionHelper


class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        #self.wd = webdriver.Chrome()
        #self.wd = webdriver.Ie()
        self.wd.implicitly_wait(3)
        self.session = SessionHelper(self)

    def open_admin_page(self):
        wd = self.wd
        if not wd.current_url.endswith("/admin/"):
            wd.get('http://localhost/litecart/admin/')

    def destroy(self):
        self.wd.quit()
