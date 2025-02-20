from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
options.add_argument("start-maximized")
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.linkedin.com/in/<YOURPROFILENAMEASAPPEARSINURL>/recent-activity/all/")
commentsUrl = "https://www.linkedin.com/in/<YOURPROFILENAMEASAPPEARSINURL>/recent-activity/comments/"
#driver.get()
wait = WebDriverWait(driver, 10)
url = "https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin/"
driver.get(url)
driver.maximize_window()

wait.until(EC.element_to_be_clickable((By.ID, "username"))).send_keys("YOUREMAILADDRESS")
wait.until(EC.element_to_be_clickable((By.ID, "password"))).send_keys("YOURPASSWORD")
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-litms-control-urn='login-submit']"))).click()
wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class,'global-nav__primary-link')][contains(.,'Me')]"))).click()
#wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href*='logout']"))).click()
time.sleep(1)
#driver.quit()
y=1000

df = pd.read_csv(r"yourpathtofile\testFile.csv", usecols = ['First Name','URL', 'Position'])
#, usecols = ['First Name','URL', 'Position']
print(df)
userName = df['First Name']
userURL = df['URL']
userPosition = df['Position']
print(type(userName))
k = 0
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
    driver.get(x+"/recent-activity/all/")
    k += 1
    for i in range(0,15):
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, "+str(y)+")")
        y += 1000  
        time.sleep(1)
        print(i)
        ## this needs to be one index lower than the top level of the range
        if i == 14:
            page_source = driver.page_source
            print('here')
            fileToWrite = open(fr'C:\Users\tasos\Downloads\linkedin\linkedinPosts{str(k)}.html',"w+",encoding="utf-8")
            fileToWrite.write(page_source)
            fileToWrite.close()

while(True):
    pass

for i in range(0,10):
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
while(True):
    pass
