from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from random import randint
import pandas as pd
import os

# Create Chromeoptions instance
options = webdriver.ChromeOptions()
# Adding argument to disable the AutomationControlled flag
options.add_argument("--disable-blink-features=AutomationControlled")
# Exclude the collection of enable-automation switches
options.add_experimental_option("excludeSwitches", ["enable-automation"])
# Turn-off userAutomationExtension
options.add_experimental_option("useAutomationExtension", False)
# allow clipboard access
options.add_experimental_option(
    "prefs",
    {
        "profile.default_content_setting_values.notifications": 2,
        "profile.default_content_setting_values.clipboard": 1,
    },
)
# set user agent profile
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
    (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
)
# Setting the driver path and requesting a page
driver = webdriver.Chrome(options=options)
# Changing the property of the navigator value for webdriver to undefined
driver.execute_script(
    "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
)


# csv_file = f"{USERNAME}.csv"
# if os.path.isfile(csv_file):
#    df = pd.read_csv(csv_file)
# else:
#    df = pd.DataFrame(columns=["link", "post"])

base_url = "https://www.google.com/search?q=site%3Alinkedin.com%2Fin%2F+%28%22Chief+Product+Officer%22%29+%28%22United+States%22%29+%28%22Automotive%22%29&sca_esv=c5f02fd2b2be415a&sxsrf=ACQVn0-34X-ugeniEQUP9_2eAdrC7zg8FA%3A1709610395290&ei=m5XmZaC0EYTdptQP0biH0AM&ved=0ahUKEwjg7cKCm9yEAxWErokEHVHcAToQ4dUDCBA&uact=5&oq=site%3Alinkedin.com%2Fin%2F+%28%22Chief+Product+Officer%22%29+%28%22United+States%22%29+%28%22Automotive%22%29&gs_lp=Egxnd3Mtd2l6LXNlcnAiUHNpdGU6bGlua2VkaW4uY29tL2luLyAoIkNoaWVmIFByb2R1Y3QgT2ZmaWNlciIpICgiVW5pdGVkIFN0YXRlcyIpICgiQXV0b21vdGl2ZSIpSABQAFgAcAB4AJABAJgBAKABAKoBALgBA8gBAPgBAZgCAKACAJgDAJIHAKAHAA&sclient=gws-wiz-serp"  # base url for profile
wait = WebDriverWait(driver, timeout=10, poll_frequency=0.2)  # initialise wait
driver.get(base_url)  # go to linkedin
time.sleep(5)

# store source code of driver
print(driver.page_source)

with open("source.txt", "w") as file:
    file.write(driver.page_source)

# read from file



# linkedin credentials
# email = ""
# password = ""

# login
# wait.until(lambda d: driver.find_element(By.ID, "session_key").is_displayed())
# driver.find_element(By.ID, "session_key").send_keys(email)
# driver.find_element(By.ID, "session_password").send_keys(password)
# driver.find_element(By.CLASS_NAME, "sign-in-form__submit-btn--full-width").click()

# time.sleep(15)  # security check
## go to profile
# driver.get(base_url.format(USERNAME=USERNAME))
# time.sleep(5)  # just in case

# wait.until(
#    lambda d: driver.find_element(
#        By.CLASS_NAME, "profile-creator-shared-feed-update__container"
#    ).is_displayed()
# )

# posts: [WebElement] = []
# time_end = time.time() + 15
# while time.time() < time_end:
#    # scroll to bottom of page
#    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# posts = driver.find_elements(
#    By.CLASS_NAME, "profile-creator-shared-feed-update__container"
# )
## limit posts list to 10
# posts = posts[:10]

## reset scroll position
# driver.execute_script("window.scrollTo(0, 0);")
## maximise screen
# driver.maximize_window()

# count = 0

# iterate through posts and click svg with class artdeco-button__icon
# for post in posts:
#    count += 1
#    try:
#        print("trying post:", count)
#        time.sleep(randint(1, 2))
#        svgs = post.find_elements(By.TAG_NAME, "svg")
#        buttons = post.find_elements(By.TAG_NAME, "button")

#        try:
#            for button in buttons:
#                if button.get_attribute("aria-label") == "Open control menu":
#                    driver.execute_script("arguments[0].click();", button)
#                    # button.click()
#                    break
#        except Exception as e:
#            for svg in svgs:
#                if svg.get_attribute("data-test-icon") == "overflow-web-ios-medium":
#                    driver.execute_script("arguments[0].click();", svg)
#                    break

#        # find all elements with class name artdeco-dropdown__item
#        wait.until(
#            lambda d: driver.find_element(
#                By.CLASS_NAME, "artdeco-dropdown__item"
#            ).is_displayed()
#        )
#        elements = driver.find_elements(By.CLASS_NAME, "artdeco-dropdown__item")
#        # iterate through elements and find copy to clipboard
#        for element in elements:
#            if element.text == "Copy link to post":
#                driver.execute_script("arguments[0].click();", element)
#                break

#        clipboard = driver.execute_script("return navigator.clipboard.readText()")
#        post_text = post.find_element(By.CLASS_NAME, "break-words").text

#        if clipboard not in df["link"].values and post_text not in df["post"].values:
#            df.loc[len(df.index)] = [clipboard, post_text]
#    except Exception as e:
#        print("error:", str(e))
#        continue

## save dataframe to csv
# df.to_csv(f"{USERNAME}.csv", index=False)
