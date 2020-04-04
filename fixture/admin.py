

class AdminHelper:

    def __init__(self, app):
        self.app = app

    def check_h1(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("h1")

    def check_left_menu(self):
        wd = self.app.wd
        rows = wd.find_elements_by_css_selector("li#app-")
        for row in range(0, len(rows)):
            rows = wd.find_elements_by_css_selector("li#app-")
            rows[row].click()
            self.check_h1()
            docs = wd.find_elements_by_css_selector("[id^=doc]")
            if len(docs) > 0:
                for i in range(0, len(docs)):
                    docs = wd.find_elements_by_css_selector("[id^=doc]")
                    docs[i].click()
                    self.check_h1()