from selenium.common.exceptions import WebDriverException


class there_is_window_other_than(object):

    def __init__(self, old_windows):
        self.old_windows = old_windows

    def __call__(self, wd):
        handles = wd.window_handles
        new = [x for x in handles if x not in self.old_windows]
        if len(new) > 0:
            return new[0]
        else:
            return False

class number_of_elements(object):

    def __init__(self, locator, number):
        self.locator = locator
        self.number = number

    def __call__(self, wd):
        elements = _find_elements(wd, self.locator)
        if len(elements) == self.number:
            return elements
        else:
            return False

def _find_elements(wd, by):
    try:
        return wd.find_elements(*by)
    except WebDriverException as e:
        raise e