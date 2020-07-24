from selenium import webdriver

cbrower = webdriver.Chrome('./chromedriver')
cbrower.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

# print('Selenium Easy Demo' in cbrower.title)

buttonshwmess = cbrower.find_element_by_class_name('btn-default')
# print(buttonshwmess.get_attribute('innerHTML'))

assert 'Show Message' in cbrower.page_source

textb = cbrower.find_element_by_id('user-message')
textb.clear()
textb.send_keys('Iam cool')
buttonshwmess.click()
outmessage = cbrower.find_element_by_id('display')
assert 'cool' in outmessage.text

button2 = cbrower.find_element_by_css_selector('#get-input > .btn')
print(button2)
cbrower.close()