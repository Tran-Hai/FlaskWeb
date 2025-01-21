from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.edge.options import Options
import os
import  pandas as pd

def crawl_data(): # crawl data from website and store these data into python 2 - Dimensional list
    options = Options()
    options.add_argument('--headless')
    options.headless = True

    # define dataset to store data
    dataset = []

    # setup chrome and login to website
    driver = webdriver.Edge(options=options)
    url = "http://10.122.72.1/static/m647"
    driver.get(url)

    # Setup information of username and password
    username_field = driver.find_element(By.XPATH, "//*[@id='epUserID']")
    username_field.send_keys("s00024")

    password_field = driver.find_element(By.XPATH, "//*[@id='epPassWord']")
    password_field.send_keys("1234qwer!")

    login_field = driver.find_element(By.XPATH, "/html/body/div/div[3]/form/div/button")
    login_field.click()

    # Access to required data
    # done_checkbox = driver.find_element(By.XPATH, "//*[@id='Status_3']")
    wait = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='Status_3']"))
    )
    done_checkbox = driver.find_element(By.XPATH, "//*[@id='Status_3']")
    done_checkbox.click()

    close_checkbox = driver.find_element(By.XPATH, "//*[@id='Status_4']")
    close_checkbox.click()

    bm_checkbox = driver.find_element(By.XPATH, "//*[@id='Type_8']")
    bm_checkbox.click()

    wait = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='pt-showreport']"))
    )
    report_field = driver.find_element(By.ID, "pt-showreport")
    report_field.click()

    # View data
    wait = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/table/tbody/tr/td[2]/div/div[2]/div[3]/div/div/table"))
    )
    data_view = driver.find_element(By.XPATH, "/html/body/table/tbody/tr/td[2]/div/div[2]/div[3]/div/div/table/tbody")

    # access data on table convert it into python lists
    rows = data_view.find_elements(By.TAG_NAME, "tr")

    for row in rows:
        columns = row.find_elements(By.TAG_NAME, "td")
        if len(columns) == 5:
            continue
        temp = []
        for i in range(0, 15):
            # print(columns[i].text)
            temp.append(columns[i].text)
        dataset.append(temp)

    driver.quit()
    return dataset

