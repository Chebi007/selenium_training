from selenium.webdriver.common.by import By


class AdminHelper:

    def __init__(self, app):
        self.app = app

    def get_header_h1(self):
        wd = self.app.wd
        return wd.find_element_by_css_selector("h1").text

    def check_left_menu(self):
        wd = self.app.wd
        rows = wd.find_elements_by_css_selector("li#app-")
        for row in range(0, len(rows)):
            rows = wd.find_elements_by_css_selector("li#app-")
            rows[row].click()
            self.get_header_h1()
            docs = wd.find_elements_by_css_selector("[id^=doc]")
            if len(docs) > 0:
                for i in range(0, len(docs)):
                    docs = wd.find_elements_by_css_selector("[id^=doc]")
                    docs[i].click()
                    self.get_header_h1()

    def open_menu_item(self, item):
        wd = self.app.wd
        rows = wd.find_elements_by_css_selector("li#app-")
        for row in range(0, len(rows)):
            rows = wd.find_elements_by_css_selector("li#app-")
            if rows[row].find_element_by_css_selector("span.name").get_attribute("textContent") == item:
                rows[row].find_element_by_css_selector("span.name").click()

    def get_list_of_countries(self):
        wd = self.app.wd
        self.open_menu_item("Countries")
        list = []
        for row in wd.find_elements_by_css_selector("tr.row"):
            cells = row.find_elements_by_css_selector("td")
            country = cells[4].text
            list.append(country)
        return list

    def get_zones_from_countries(self):
        wd = self.app.wd
        self.open_menu_item("Countries")
        rows = wd.find_elements_by_css_selector("tr.row")
        dict = {}
        for row in range(0, len(rows)):
            rows = wd.find_elements_by_css_selector("tr.row")
            cells = rows[row].find_elements_by_css_selector("td")
            key = cells[4].text
            if int(cells[5].text) > 0:
                zones = []
                cells[6].find_element_by_css_selector("[title=Edit]").click()
                rows2 = wd.find_elements_by_css_selector("#table-zones tr")
                for row2 in range(1, (len(rows2) - 1)):
                    rows2 = wd.find_elements_by_css_selector("#table-zones tr")
                    cells2 = rows2[row2].find_elements_by_css_selector("td")
                    zones.append(cells2[2].text)
                wd.find_element_by_css_selector("[name=cancel]").click()
                dict[key] = zones
        return dict

    def get_zones_from_geozones(self):
        wd = self.app.wd
        self.open_menu_item("Geo Zones")
        rows = wd.find_elements_by_css_selector("tr.row")
        dict = {}
        for row in range(0, len(rows)):
            rows = wd.find_elements_by_css_selector("tr.row")
            cells = rows[row].find_elements_by_css_selector("td")
            key = cells[2].text
            zones = []
            cells[4].find_element_by_css_selector("[title=Edit]").click()
            rows2 = wd.find_elements_by_css_selector("#table-zones tr")
            for row2 in range(1, (len(rows2) - 1)):
                rows2 = wd.find_elements_by_css_selector("#table-zones tr")
                cells2 = rows2[row2].find_elements_by_css_selector("td option[selected=selected]")
                zones.append(cells2[1].text)
            wd.find_element_by_css_selector("[name=cancel]").click()
            dict[key] = zones
        return dict
