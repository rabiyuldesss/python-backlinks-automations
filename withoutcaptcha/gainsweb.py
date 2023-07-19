import tkinter as tk
from tkinter import ttk
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import csv 
from selenium.webdriver.common.keys import Keys
from datetime import datetime


win = tk.Tk()

win.title("Maximized Window")

# Maximize the window
win.attributes("-alpha", True)
win.title("Python GUI App")

ttk.Label(win, text="Selenium Automation").pack()

# Define the dropdown options
options = [
    "|   |___Hospitality",
    "|   |___Web Design and Development",
    "|   |___Development",
    "|   |___Web Hosting",
    "|   |   |___Programming and Development",
    "|   |   |___Internet and Web"

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

    #-------------------------------------------------------------------------------
    # Web Automation

        for line in csv_reader:


            driver = webdriver.Chrome()
            driver.get('https://gainweb.org/submit.php')
            driver.maximize_window()
            time.sleep(5)

            freelink = driver.find_element("xpath", '/html/body/div[5]/div[4]/div[2]/form/table/tbody/tr[1]/td/div/div[1]/table/tbody/tr[3]/td[1]/input')
            freelink.click()
            time.sleep(5)

            username_field = driver.find_element("xpath", '//*[@id="OWNER_NAME"]')
            username_field.send_keys(line[0])
            time.sleep(3)

            Email_field = driver.find_element("xpath", '//*[@id="OWNER_EMAIL"]')
            Email_field.send_keys(line[1])
            time.sleep(3)

            URL_field = driver.find_element("xpath", '//*[@id="URL"]')
            URL_field.send_keys(line[2])
            time.sleep(3)

            Title_field = driver.find_element("xpath", '//*[@id="TITLE"]')
            Title_field.send_keys(line[3])
            time.sleep(3)

            Description_field = driver.find_element("xpath", '//*[@id="DESCRIPTION"]')
            Description_field.send_keys(line[4])
            time.sleep(3)


            element = driver.find_elements(By.NAME, 'CATEGORY_ID')
            print('ok')
            drp = Select(element[0])
            selected_option = combobox.get()  # Get the selected option from the combobox
            drp.select_by_visible_text(selected_option)
            time.sleep(4)

            agree = driver.find_elements(By.NAME, 'AGREERULES')
            agree[0].click()
            time.sleep(10)

            submit = driver.find_elements(By.XPATH, '/html/body/div[5]/div[4]/div[2]/form/table/tbody/tr[13]/td/input')
            submit[0].click()
            driver.quit()
            win.after(stop_duration, stop_app)



button = ttk.Button(win, text="Open Website", command=open_website)
button.pack()
win.mainloop()