from selenium import webdriver

wd = webdriver.Firefox()
wd.get('https://software-testing.ru/')
wd.implicitly_wait(3)
wd.quit()