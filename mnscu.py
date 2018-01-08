
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests as r
import pandas as pd
from bs4 import BeautifulSoup
import re
from time import sleep
import pdb

driver = webdriver.Chrome()
driver.get('https://webproc.mnscu.edu/registration/search/advanced.html?campusid=mnonline')

main_page_source = driver.page_source

college_values = driver.find_elements_by_name("searchrcid")
college_actual_values = college_values[0].find_elements_by_tag_name('option')

college_value = college_actual_values[1]
college_value.click()

semester_values = driver.find_elements_by_name("yrtr")
semester_actual_values = semester_values[0].find_elements_by_tag_name('option')

subject_values = driver.find_elements_by_name('subject')
subject_actual_values = subject_values[0].find_elements_by_tag_name('option')

open_values = driver.find_elements_by_css_selector("input[type='radio'][name='openValue']")
delivery_values = driver.find_elements_by_css_selector("input[type='radio'][name='delivery']")


for college_value_index in range(1, len(college_actual_values)):
    driver.get('https://webproc.mnscu.edu/registration/search/advanced.html?campusid=mnonline')

    college_values = driver.find_elements_by_name("searchrcid")
    college_actual_values = college_values[0].find_elements_by_tag_name('option')

    college_value = college_actual_values[college_value_index]
    college_value.click()
    for semester_value_index in range(len(semester_actual_values)):
        for subject_value_index in range(1, 2): #len(subject_actual_values)
            for open_value_index in range(len(open_values)):
                for delivery_value_index in range(1,len(delivery_values)):

                    driver.get('https://webproc.mnscu.edu/registration/search/advanced.html?campusid=mnonline')
                    college_values = driver.find_elements_by_name("searchrcid")
                    college_actual_values = college_values[0].find_elements_by_tag_name('option')

                    college_value = college_actual_values[college_value_index]
                    college_value.click()

                    semester_values = driver.find_elements_by_name("yrtr")
                    semester_actual_values = semester_values[0].find_elements_by_tag_name('option')

                    subject_values = driver.find_elements_by_name('subject')
                    subject_actual_values = subject_values[0].find_elements_by_tag_name('option')

                    open_values = driver.find_elements_by_css_selector("input[type='radio'][name='openValue']")
                    delivery_values = driver.find_elements_by_css_selector("input[type='radio'][name='delivery']")
                    try:
                        semester_value = semester_actual_values[semester_value_index]
                    except:
                        print("ummmmm")
                        continue
                    subject_value = subject_actual_values[subject_value_index]

                    open_value = open_values[open_value_index]
                    delivery_value = delivery_values[delivery_value_index]

                    semester_value.click()
                    subject_value.click()
                    open_value.click()
                    delivery_value.click()

                    driver.find_element_by_css_selector("input[type='submit'][title='Search']").click()

                    # iterate through all pages
                    try:
                        driver.find_element_by_css_selector("a[class='yui-pg-next']").click()
                    except:
                        continue

                    html_source = str(driver.page_source)

                    with open('./mnscu/%s.html' % ('out'),'w') as f:
                        f.write(str(html_source))
