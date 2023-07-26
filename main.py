from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import chromedriver_autoinstaller
import time

chrome_driver_path = "\D:\Development\chromedriver.exe"
chromedriver_autoinstaller.install() # automatically downloads the chromedriver compatible to the client's version of chrome
service = Service(chrome_driver_path) # starts the chromedriver
options = webdriver.ChromeOptions()  # this class is used to manipulate various properties of chromedriver
options.add_experimental_option("detach", True) # keeps the browser open
driver = webdriver.Chrome(service=service, options=options)
URL = "https://tinder.com/"

EMAIL = "***"
PW = "***"

driver.get(URL)
time.sleep(2)
driver.fullscreen_window()
time.sleep(1)

# Login
login_button = driver.find_element(By.XPATH, '//*[@id="q-497183963"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
login_button.click()
time.sleep(2)

# Login w Facebook
fb_login_button = driver.find_element(By.XPATH, '//*[@id="q2069402257"]/main/div/div/div[1]/div/div/div[3]/span/div[2]/button/div[2]/div[2]/div/div')
fb_login_button.click()
time.sleep(2)

# Switch to FB window
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]

driver.switch_to.window(fb_login_window)
print(driver.title)

# Log in with Email and Password and hit ENTER
email_bar = driver.find_element(By.ID, 'email')
email_bar.click()
email_bar.send_keys(EMAIL)

pw_bar = driver.find_element(By.ID, 'pass')
pw_bar.click()
pw_bar.send_keys(PW)
pw_bar.send_keys(Keys.ENTER)
time.sleep(5)

# Switch back to Tiner window
driver.switch_to.window(base_window)
print(driver.title)
time.sleep(5)

# Click Allow, Not Interested, and Accept Cookies
allow_button = driver.find_element(By.XPATH, '//*[@id="q2069402257"]/main/div/div/div/div[3]/button[1]')
allow_button.click()
time.sleep(2)

not_interested = driver.find_element(By.XPATH, '//*[@id="q2069402257"]/main/div/div/div/div[3]/button[2]')
not_interested.click()
time.sleep(2)

accept_cookies = driver.find_element(By.XPATH, '//*[@id="q-497183963"]/div/div[2]/div/div/div[1]/div[1]/button')
accept_cookies.click()
time.sleep(2)

# Swipe Left bc I got a bae :)
for i in range(100):

    try:
        swipe_left_button = driver.find_element(By.XPATH, '//*[@id="q-497183963"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[2]/button')
        swipe_left_button.click()
        time.sleep(3)

    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, ".itsAMatch a")
            match_popup.click()

        except NoSuchElementException:
            time.sleep(2)

driver.quit()




# # Continue as Shoto
# continue_button = driver.find_element(By.CLASS_NAME, 'x1o1ewxj')
# continue_button.click()
# time.sleep(2)
#
# # Verify
# verify_button = driver.find_element(By.ID, 'home_children_button')
# verify_button.click()
# time.sleep(2)