

#login_logout_mutipleUser_muliple_window
#Login and logout testing for 3 user with 1000 time



import selenium.webdriver as webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.keys import Keys
from time import sleep
import os,csv,time
from selenium.webdriver.support.ui import WebDriverWait
chrome_driver_path = os.getcwd() + "/chromedriver"
from selenium import webdriver
import os,csv,time
from selenium.webdriver.support.ui import WebDriverWait

values = {'user1': 'chenna08','pass1': 123456,
          'user2':'chenna2','pass2':123456,
          'user3':'chenna3','pass3':123456
          }



drivers={
    "driver1":webdriver.Chrome(chrome_driver_path),
    "driver2":webdriver.Chrome(chrome_driver_path),
    "driver3":webdriver.Chrome(chrome_driver_path),
}

print(values['user1'])
for driver in drivers.values():
    driver.get("http://newtours.demoaut.com/")
    first_window = driver.window_handles[0]
    all_windows = driver.window_handles
    for window in all_windows:
            if window != first_window:
                new_window = window
                driver.switch_to_window(first_window)
            else:
                second_window =window
                driver.switch_to_window(second_window)


                for i in range(100):
                        time.sleep(5)
                        driver.find_element_by_name("userName").click()
                        driver.find_element_by_name("userName").send_keys(values['user1'])
                        driver.find_element_by_name("password").click()
                        driver.find_element_by_name("password").send_keys(values['pass1'])
                        driver.find_element_by_name("login").click()
                        driver.find_element_by_link_text("SIGN-OFF").click()

                for j in range(100):
                    time.sleep(5)
                    driver.find_element_by_name("userName").click()
                    driver.find_element_by_name("userName").send_keys(values['user2'])
                    driver.find_element_by_name("password").click()
                    driver.find_element_by_name("password").send_keys(values['pass2'])
                    driver.find_element_by_name("login").click()
                    driver.find_element_by_link_text("SIGN-OFF").click()


                for x in range(100):
                    time.sleep(5)
                    driver.find_element_by_name("userName").click()
                    driver.find_element_by_name("userName").send_keys(values['user3'])
                    driver.find_element_by_name("password").click()
                    driver.find_element_by_name("password").send_keys(values['pass3'])
                    driver.find_element_by_name("login").click()
                    driver.find_element_by_link_text("SIGN-OFF").click()




