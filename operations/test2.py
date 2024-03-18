import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException


# part 1
# --> connect to the website and setting up chrome browser to ignore the unsigned SSL/Cert as this is an IP
service = Service()
options = webdriver.ChromeOptions()
chrome_options = Options()

driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()

url = "https://avio2-webapp.netlify.app/#/login/"  # web page's URL
driver.get(url)

time.sleep(5)  # timer 5 seconds

# part 2
# --> log in with these credentials
username = "avio2"
password = "Matrox0001"

driver.find_element(By.NAME, "username").send_keys(username)
driver.find_element(By.NAME, "password").send_keys(password)

try:
    # Wait for the "Sign in" button to be clickable
    sign_in_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'button-primary'))
    )

    # Click the "Sign in" button
    sign_in_button.click()

except Exception as e:
    print(f"Error during login: {e}")

time.sleep(5)  # timer 10 seconds

# # Click on 'Network' option from the Side bar
# navigation_bar = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.CLASS_NAME, "navigation-bar"))
# )

# # Click on 'Devices' option from the Side bar
# list_item_text = "Device"
# list_item = navigation_bar.find_element(By.XPATH, f"//a[text()='{list_item_text}']")

# # Click on the list item
# list_item.click()

# time.sleep(5)  # Time to complete the action and wait for the next

# # Select the 'Others' tile
# others_tile = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.XPATH, "//p[text()='Other']/ancestor::tile-card"))
# )

# # Click on the 'Others' tile
# others_tile.click()
# print("Clicked on 'Others' tile")

# time.sleep(5)

# Click on the '...' dots
# Locate the parent container of the "..." button
image_src = "assets/images/dots-horizontal.svg"
button_xpath = f"//button[@class='action-button']//img[@src='{image_src}']"

# Wait for the button to be clickable
dots_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, button_xpath))
)

# Perform your action on the button
dots_button.click()

print("Clicked on '...' button successfully!")


time.sleep(5)

connect_option_xpath = "//li[@class='list-item']//p[@class='label' and text()=' Device mode... ']"

connect_option = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, connect_option_xpath))
)

connect_option.click()

time.sleep(5)
print('clicked on Device change mode')

receiver_button_xpath = "//button[@class='mode-select']/p[text()=' Receiver ']"

# Wait for the button to be clickable
receiver_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, receiver_button_xpath))
)

# Click on the Transmitter button
receiver_button.click()

time.sleep(5)
print('clicked on Receiver option')

transmitter_div_xpath = "//li[@class='list-item']//p[@class='label' and text()=' Transmitter ']"

# Wait for the div to be present in the DOM
transmitter_div = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, transmitter_div_xpath))
)

transmitter_div.click()
print("Transmitter is selected")

time.sleep(5)

max_retries = 3
retry_count = 0

#while retry_count < max_retries:
try:
    ok_button = "//button[@class='button-large button-primary']/p[text()='Ok' and not(@disabled)]]"
    ok_button_xpath = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, ok_button))
    )

    print("Ok button found, attempting to click.")
    time.sleep(10)
    driver.execute_script("arguments[0].click();", ok_button_xpath)
    print("Ok button clicked.")
except TimeoutException:
    print("TimeoutException: Ok button not found or not clickable.")

# try:
#     ok_button_xpath = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.XPATH, "//button[@class='button-primary']"))
# )
#     ok_button_xpath.click()
    # except NoSuchElementException:
    #     print("Button not found on the page")

# ok_button_xpath = "//button[@class= 'button-primary'] /p[text() = 'Ok']"
# # Find and click the "Ok" button
# ok_button = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.XPATH, ok_button_xpath))
# )

# action = ActionChains(driver)
# action.move_to_element(ok_button).click(ok_button).perform()

# ok_button.click()

# if ok_button.is_displayed():
#     ok_button.click()
#     print("Clicked on Ok button")

# else:
#     print('not found')
    

#time.sleep(15)

# Finally, quit the driver
driver.quit()
