# Week 3
## Facebook_bot

### Code
#### script
```bash
from selenium import webdriver
from getpass import getpass
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def login():
    email_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.ID, "m_login_email")))
    email_field.send_keys(email)

    pass_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.ID, "m_login_password")))
    pass_field.send_keys(password)

    login_btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'button[data-sigil="touchable login_button_block m_login_button"]')))
    login_btn.click()
    while(True):
        try:
            not_now = driver.find_element_by_css_selector('a[data-sigil="touchable"]')
            not_now.click()
            break
        except NoSuchElementException:
            break

def like():
    like_btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located(    
        (By.ID, "u_0_s")))
    like_btn.click()

def comment():
    comment_box = WebDriverWait(driver,10).until(EC.presence_of_element_located(
        (By.ID,"composerInput")))
    post_btn = WebDriverWait(driver,10).until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'button[aria-label="Post"]')))
    comment_text = "I would like to work as a freelancer, Build some automated web for fun, Instructors are quite informative, They are well known in their respective fields, This Bootcamp taught me basic python, web automation, scraping far, I would not only be willing to, But I would love to carry forward this legacy"
    a = comment_text.split(",")
    for i in range(0,len(a)):
        comment_box.send_keys(a[i])
        time.sleep(1)
        post_btn.click()
        time.sleep(3)
        
    for j in range(5):
        comment_box.send_keys('''#Google_Developers #Developers_Student_Club_Pakistan'''," ",j)
        time.sleep(1)
        post_btn.click()
        time.sleep(3)

def share():
    share_btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR,'a[data-sigil="share-popup"]')))
    share_btn.click()
    share_btn2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.ID,'share-with-message-button')))
    share_btn2.click()
    share_btn3 = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.ID,'share_msg_input')))
    share_btn3.send_keys('''Here, this post shared using a Bot created using selenium. #DSCDSU #DeveloperStudentClubs #DSCPakistan #Python #Bot''')
    share_btn4 = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.ID,'share_submit')))
    share_btn4.click()

def main():
    global email, password
    email = input('Enter email:')
    password = getpass('Enter password:')
    post_url = input("Enter Post URL: ")
    option = Options()
    option.add_argument("--disable-infobars")
    option.add_argument("start-maximized")
    option.add_argument("--disable-extensions")
    option.add_experimental_option("prefs", { "profile.default_content_setting_values.notifications": 1 })
    option.add_argument('--ignore-ssl-errors=yes')
    option.add_argument('--ignore-certificate-errors')
    global driver
    driver = webdriver.Chrome(options = option)
    driver.get("https://m.facebook.com/")

    login()
    time.sleep(3)
    driver.get(post_url)
    like()
    share()
    driver.get(post_url)
    comment()
    
if __name__ == '__main__':
    main()
```
Video Output has been attached