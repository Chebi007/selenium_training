from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from fixture.custom_wait import there_is_window_other_than
import time


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
        self.app.wait_until_element_present((By.CSS_SELECTOR, "li#app-"))
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

    def edit_country_by_index(self, index):
        wd = self.app.wd
        row = wd.find_elements_by_css_selector("tr.row")[index]
        row.find_elements_by_css_selector("td")[6].click()

    def open_window(self, link):
        wd = self.app.wd
        main_window = wd.current_window_handle
        old_windows = wd.window_handles
        link.click()
        wait = WebDriverWait(wd, 10)
        new_window = wait.until(there_is_window_other_than(old_windows))
        wd.switch_to.window(new_window)
        wd.close()
        wd.switch_to.window(main_window)

    def open_all_windows_on_edit_country_page(self):
        wd = self.app.wd
        self.open_menu_item("Countries")
        self.edit_country_by_index(1)
        rows = wd.find_elements_by_css_selector("#content tr [target=_blank]")
        for i in range(0, len(rows)):
            link = rows[i]
            self.open_window(link)

    def get_browser_logs(self):
        wd = self.app.wd
        wd.get("http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=1")
        rows = wd.find_elements_by_css_selector("tr.row")[3:]
        for row in range(0, len(rows)):
            rows = wd.find_elements_by_css_selector("tr.row")[3:]
            rows[row].find_element_by_css_selector("td a").click()
            self.app.get_browser_logs()
            wd.find_element_by_name("cancel").click()
