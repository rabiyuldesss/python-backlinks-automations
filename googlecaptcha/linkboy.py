
import tkinter as tk
from tkinter import ttk
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.keys import Keys



win = tk.Tk()
# win.minsize(800, 600)
# win.title("Maximized Window")

# Maximize the window
win.attributes("-alpha", True)
win.title("Python GUI App")

ttk.Label(win, text="Selenium Automation").pack()

# Define the dropdown options
options = [
    "|   |___Hospitality",
    "|   |___Programming",
    "|   |___Internet",
    "|   |___Developers and Publishers"

]

# Create the combobox widget
combobox = ttk.Combobox(win, values=options)
combobox.pack()


def stop_app():
    win.destroy()
def delay(waiting_time=5):
    driver = webdriver.Chrome()
    driver.implicitly_wait(waiting_time)
stop_duration = 5000


def open_website():
            #-------------------------------------------------------------------------------
            # Setup
            Username = 0
            Email = 1
            URL = 2

            with open('data.csv', 'r') as csv_file:

                csv_reader = csv.reader(csv_file)

            #-------------------------------------------------------------------------------
            # Web Automation

                for line in csv_reader:

                    driver = webdriver.Chrome()
                    driver.get('http://www.link-boy.org/submit.php')
                    driver.maximize_window()
                    time.sleep(5)

                    Title_field = driver.find_element("xpath", '//*[@id="content"]/form/table/tbody/tr[1]/td[2]/input')
                    Title_field.send_keys(line[3])
                    time.sleep(3)

                    URL_field = driver.find_element("xpath", '//*[@id="content"]/form/table/tbody/tr[2]/td[2]/input')
                    URL_field.send_keys(line[2])
                    time.sleep(3)

                    Description_field = driver.find_element("xpath", '//*[@id="content"]/form/table/tbody/tr[3]/td[2]/textarea')
                    Description_field.send_keys(line[4])
                    time.sleep(3)

                    username_field = driver.find_element("xpath", '//*[@id="content"]/form/table/tbody/tr[4]/td[2]/input')
                    username_field.send_keys(line[0])
                    time.sleep(3)

                    Email_field = driver.find_element("xpath", '//*[@id="content"]/form/table/tbody/tr[5]/td[2]/input')
                    Email_field.send_keys(line[1])
                    time.sleep(3)



                    element = driver.find_elements(By.NAME, 'CATEGORY_ID')
                    print('ok')
                    drp = Select(element[0])
                    selected_option = combobox.get()  # Get the selected option from the combobox
                    drp.select_by_visible_text(selected_option)
                    time.sleep(30)
                    
                    # submit = driver.find_elements(By.XPATH, '//*[@id="content"]/form/table/tbody/tr[8]/td/input')
                    # submit[0].click()
                    print("completed")
                    win.after(stop_duration, stop_app)



button = ttk.Button(win, text="Open Website", command=open_website)
button.pack()
win.mainloop()   

    