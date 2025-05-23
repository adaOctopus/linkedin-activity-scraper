from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

options = Options()
options.add_argument("start-maximized")
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

wait = WebDriverWait(driver, 10)
url = "https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin/"
driver.get(url)
driver.maximize_window()

wait.until(EC.element_to_be_clickable((By.ID, "username"))).send_keys("nvnvnvnvn")
wait.until(EC.element_to_be_clickable((By.ID, "password"))).send_keys("nvnvnvnv")
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-litms-control-urn='login-submit']"))).click()
wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class,'global-nav__primary-link')][contains(.,'Me')]"))).click()
#wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href*='logout']"))).click()
time.sleep(1)
#driver.quit()
y=1000

df = pd.read_csv(r"C:\Users\tasos\Downloads\linkedin\testFileTwo.csv", usecols = ['First Name','URL', 'Position'])
#, usecols = ['First Name','URL', 'Position']
print(df)
userName = df['First Name']
userURL = df['URL']
userPosition = df['Position']
print(type(userName))
k = 0
message = "Hi " + userName + "! I saw in your profile that you are into AI content, is that right? If so, do you want to roast my latest app? 🤣"
# if you want to iterate through both columns at the same time and same index
# EXAMPLE
#stu_df = pd.DataFrame(students, columns=['Name', 'Age', 'Section'],
#                      index=['1', '2', '3', '4'])
 
# gives a tuple of column name and series
# for each column in the dataframe
#for (columnName, columnData) in stu_df.iteritems():
#    print('Column Name : ', columnName)
#    print('Column Contents : ', columnData.values)
for x in df['URL']:
    #driver.get(x+"/recent-activity/all/")
    driver.get(x)
    k += 1
    time.sleep(2)
    # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[7]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/div[3]/div/div[1]/button"))).click()
    driver.find_element(By.XPATH, '/html/body/div[7]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/div[3]/div/div[1]/button').click()
    # driver.FindElementByXPath("//a[contains(@class, 'message-anywhere-button')]").click()
    #  driver.FindElementByXPath("//div[contains(@class, 'msg-form__contenteditable')]")
    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "msg-form__contenteditable"))).send_keys(message)
    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "msg-form__send-button artdeco-button artdeco-button--1"))).click()
    time.sleep(1)
    # for i in range(0,15):
    #     time.sleep(1)
    #     driver.execute_script("window.scrollTo(0, "+str(y)+")")
    #     y += 1000  
    #     time.sleep(1)
    #     print(i)
        ## this needs to be one index lower than the top level of the range
        # if i == 14:
        #     page_source = driver.page_source
        #     print('here')
        #     fileToWrite = open(fr'C:\Users\tasos\Downloads\linkedin\linkedinPosts{str(k)}.html',"w+",encoding="utf-8")
        #     fileToWrite.write(page_source)
        #     fileToWrite.close()

while(True):
    pass
