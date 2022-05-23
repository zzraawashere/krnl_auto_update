from ssl import Options
import selenium
from selenium import webdriver
import glob
import os

from selenium.webdriver.firefox.options import Options

options = Options()
options.set_preference("browser.download.folderList", 2)
options.set_preference("browser.download.manager.showWhenStarting", False)
options.set_preference("browser.download.dir", r"C:\Users\penis\Documents")
options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/x-gzip")

driver = webdriver.Firefox(options=options)





def seleniumTasks(krnlDownload, xpath):

    driver.get(krnlDownload)

    driver.find_element_by_xpath(xpath).click()





def osTasks(list_of_files = 0, latest_file = 0):
    list_of_files = glob.glob('C:/Users/penis/Documents/*') # * means all if need specific format then *.csv
    latest_file = max(list_of_files, key=os.path.getctime)
    print(latest_file)
    os.startfile(latest_file)


seleniumTasks("https://krnl.ca/download.html", "/html/body/header/div/div[2]/div/div[2]/div/div/a/button")

osTasks()