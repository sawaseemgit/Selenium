from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.nyse.com/index')
elem = browser.find_element_by_css_selector('#content-66ca4323-8ef7-4978-820f-f65ea780cfe6 > nav > div.navbar__right.hidden-xs > form > div > div > input[type=search]')
elem.send_keys('stocks')
elem.submit()
browser.refresh()
browser.quit()