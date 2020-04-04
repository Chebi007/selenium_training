

class MainHelper:

    def __init__(self, app):
        self.app = app

    def list_of_products(self):
        wd = self.app.wd
        self.app.open_main_page()
        return wd.find_elements_by_css_selector("li[class^=product]")

    def count_stickers_on_products(self):
        list = []
        for row in self.list_of_products():
            list.append(len(row.find_elements_by_css_selector("div[class^=sticker]")))
        return list
