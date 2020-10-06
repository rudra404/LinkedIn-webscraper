# imports
from selenium import webdriver
from time import sleep
import parameters
import csv
from selenium.webdriver.common.keys import Keys
from parsel import Selector

# defining new variable passing two parameters
writer = csv.writer(open(parameters.file_name, 'w'))

# writerow() method to the write to the file object
writer.writerow(['Name', 'Job Title', 'Company', 'College', 'Location', 'URL'])

# specifies the path to the chromedriver.exe
driver = webdriver.Chrome('/usr/bin/chromedriver')

# driver.get method() will navigate to a page given by the URL address
driver.get('https://www.linkedin.com')
#driver.manage().window().maximize()
sleep(3)

main_window = driver.current_window_handle
driver.execute_script("window.open();")
driver.switch_to.window(driver.window_handles[1])
driver.get('https://www.google.com')
sleep(3)

driver.switch_to.window(main_window)

# locate email form by_class_name
username = driver.find_element_by_id('session_key')

# send_keys() to simulate key strokes
username.send_keys(parameters.linkedin_username)

# sleep for 0.5 seconds
sleep(1)

# locate password form by_class_name
password = driver.find_element_by_id('session_password')

# send_keys() to simulate key strokes
password.send_keys(parameters.linkedin_password)
sleep(1)

# locate submit button by_xpath
sign_in_button = driver.find_element_by_class_name('sign-in-form__submit-button')        

# .click() to mimic button click
sign_in_button.click()
sleep(3)

# open new blank tab
#driver.execute_script("window.open();")
#sleep(1)
#WebDriverWait(driver, 20).until(EC.number_of_windows_to_be(2))
# switch to the new window which is second in window_handles array
#driver.switch_to.window(driver.window_handles[1])

# open successfully and close
#driver.get('https://www.google.com')
#sleep(3)
driver.switch_to.window(driver.window_handles[1])
sleep(0.5)
search_bar = driver.find_element_by_name('q')
search_bar.send_keys(parameters.search_query)
sleep(0.5)

search_bar.send_keys(Keys.RETURN)
sleep(5)

#linkedin_urls = driver.find_elements_by_class_name('iUh30')
#linkedin_urls = [url.text for url in linkedin_urls]
#sleep(0.5)

links = []
linkedin_urls = driver.find_elements_by_class_name('g')

# For loop to iterate over each URL in the list
for linkedin_url in linkedin_urls:

	element = linkedin_url.find_element_by_css_selector('a')
	linkedin_url = element.get_attribute('href')
	links.append(linkedin_url)

   # get the profile URL 
	#driver.get(linkedin_url)

   # add a 5 second pause loading each URL
	sleep(5)

   # assigning the source code for the webpage to variable sel
	sel = Selector(text=driver.page_source) 
print (links)

driver.quit()

#driver.switch_to.window(main_window)
#sleep(3)