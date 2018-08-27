from selenium import webdriver


driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.douban.com')
driver.implicitly_wait(5)

driver.find_element_by_name('form_email').clear()
driver.find_element_by_name('form_email').send_keys('15210647516')
driver.find_element_by_name('form_password').clear()
driver.find_element_by_name('form_password').send_keys('clb891212')
driver.find_element_by_class_name('bn-submit').click()
driver.get(driver.current_url)
driver.find_element_by_xpath('//*[@id="statuses"]/div[2]/div[3]/div/div/div[2]/div[1]/div[2]/div/a').click()


print('End')