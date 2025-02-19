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
urltwo = "https://www.linkedin.com"
driver.get(postUrl)
y = 1000
for i in range(0,10):
    driver.execute_script("window.scrollTo(0, "+str(y)+")")
    y += 1000  
    time.sleep(1)

page_source = driver.page_source
print('your are here now')
fileToWrite = open(r"<yourpath>\linkedin.html", "w+", encoding="utf-8")
print('writing to file')
fileToWrite.write(page_source)
fileToWrite.close()

while(True):
    pass

for i in range(0,10):
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
while(True):
    pass
