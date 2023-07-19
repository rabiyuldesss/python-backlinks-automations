import requests
import tkinter as tk
from tkinter import ttk
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import csv 
web = webdriver.Chrome()
from selenium.webdriver.common.keys import Keys
from datetime import datetime


win = tk.Tk()

win.title("Maximized Window")

# Maximize the window
win.attributes("-alpha", True)
win.title("Python GUI App")

ttk.Label(win, text="Selenium Automation").pack()
#-------------------------------------------------------------------------------
# Setup

# Define the dropdown options
options = [
    "|   |   |___Internet and Web",
    "|   |   |___Web Development"

]

# Create the combobox widget
combobox = ttk.Combobox(win, values=options)
combobox.pack()

driver = webdriver.Chrome()

def stop_app():
    win.destroy()
def delay(waiting_time=5):
    driver.implicitly_wait(waiting_time)
stop_duration = 5000

def open_website():
    Username = 0
    Email = 1
    URL = 2

    with open('data.csv', 'r') as csv_file:

        csv_reader = csv.reader(csv_file)


        for line in csv_reader:
            driver = webdriver.Chrome()
            driver.get('https://www.prolinkdirectory.com/submit.php')
            driver.maximize_window()
            time.sleep(5)

            regular_free = driver.find_elements(By.XPATH, '/html/body/form/table/tbody/tr/td/table/tbody/tr[1]/td/div[1]/table/tbody/tr[5]/td[1]/input')
            regular_free[0].click()

            tit = driver.find_elements(By.XPATH, '/html/body/form/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr[2]/td[2]/input')
            tit[0].send_keys(line[3])
            print('ok')


            link = driver.find_elements(By.XPATH, '//*[@id="URL"]')
            link[0].send_keys(line[2])
            time.sleep(5)

            #category not filled
            # element=web.find_elements(By.NAME, ('CATEGORY_ID'))
        
            # drp=Select(element[0])
        

            # drp.select_by_visible_text('|   |   |___Internet and Web')

            element = driver.find_elements(By.NAME, 'CATEGORY_ID')
            print('ok')
            drp = Select(element[0])
            selected_option = combobox.get()  # Get the selected option from the combobox
            drp.select_by_visible_text(selected_option)
            time.sleep(10)

            des = driver.find_elements(By.XPATH, '/html/body/form/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr[6]/td[2]/textarea')
            des[0].send_keys(line[4])
            time.sleep(4)

            yourname = driver.find_elements(By.XPATH, '/html/body/form/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr[14]/td[2]/input')
            yourname[0].send_keys(line[0])
            time.sleep(3)

            mail = driver.find_elements(By.XPATH, '/html/body/form/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr[15]/td[2]/input')
            mail[0].send_keys(line[1])
            time.sleep(3)

            # meta_keywords = web.find_elements(By.NAME, 'META_KEYWORDS')
            # meta_keywords[0].send_keys(line[5])
            # time.sleep(2)

            # meta_des = web.find_elements(By.NAME, 'META_DESCRIPTION')
            # meta_des[0].send_keys(line[0])
            # time.sleep(3)
            # agree = web.find_elements(By.XPATH, '//*[@id="AGREERULES"]')
            # agree[0].click()
            # time.sleep(7)
            # print('i agree')
            scontinue = driver.find_elements(By.XPATH, '/html/body/form/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr[19]/td/input')
            scontinue[0].click()
            time.sleep(5)
            # web.quit()

            driver.quit()
            win.after(stop_duration, stop_app)

button = ttk.Button(win, text="Open Website", command=open_website)
button.pack()
win.mainloop()