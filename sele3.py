from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://automatetheboringstuff.com/')
# elem = browser.find_element_by_xpath('/html/body/div[2]/div[1]/blockquote[2]')
elem = browser.find_element_by_css_selector('html')
filewrite = open('newfile.txt', 'at')
filewrite.write(elem.text)
filewrite.close()

browser.quit()
