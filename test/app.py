from flask import Flask, request
import requests
import time
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os

app = Flask(__name__)

# SELENIUM_HOST = os.getenv("SELENIUM_HOST", "http://localhost:4444")


@app.route("/get-results", methods=["GET"])
def fetch_html():
    print("hit -> /get-results")
    try:
        # Create Chromeoptions instance
        options = webdriver.ChromeOptions()
        # Adding argument to disable the AutomationControlled flag
        options.add_argument("--disable-blink-features=AutomationControlled")
        # Exclude the collection of enable-automation switches
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        # Turn-off userAutomationExtension
        options.add_experimental_option("useAutomationExtension", False)
        # headless options
        options.add_argument("--no-sandbox")
        options.add_argument("--headless")
        options.add_argument("--disable-dev-shm-usage")
        # set user agent profile
        options.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
            (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
        )

        # service = Service("/usr/local/bin/chromedriver")
        s = Service(ChromeDriverManager().install())

        # Setting the driver path and requesting a page
        # driver = webdriver.Chrome(service=s, options=options)
        driver = webdriver.Remote(
            command_executor="http://tyousafn8n.click:4444/wd/hub",
            options=options,
        )
        # Changing the property of the navigator value for webdriver to undefined
        driver.execute_script(
            "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
        )

        query_params = request.args.get(
            "url",
            "https://www.google.com/search?q=site%3Alinkedin.com%2Fin%2F+%28%22Chief+Product+Officer%22%29+%28%22United+States%22%29+%28%22Automotive%22%29&sca_esv=c5f02fd2b2be415a&sxsrf=ACQVn0-34X-ugeniEQUP9_2eAdrC7zg8FA%3A1709610395290&ei=m5XmZaC0EYTdptQP0biH0AM&ved=0ahUKEwjg7cKCm9yEAxWErokEHVHcAToQ4dUDCBA&uact=5&oq=site%3Alinkedin.com%2Fin%2F+%28%22Chief+Product+Officer%22%29+%28%22United+States%22%29+%28%22Automotive%22%29&gs_lp=Egxnd3Mtd2l6LXNlcnAiUHNpdGU6bGlua2VkaW4uY29tL2luLyAoIkNoaWVmIFByb2R1Y3QgT2ZmaWNlciIpICgiVW5pdGVkIFN0YXRlcyIpICgiQXV0b21vdGl2ZSIpSABQAFgAcAB4AJABAJgBAKABAKoBALgBA8gBAPgBAZgCAKACAJgDAJIHAKAHAA&sclient=gws-wiz-serp",
        )

        base_url = query_params  # base url for profile
        driver.get(base_url)  # go to linkedin
        time.sleep(5)

        ps = driver.page_source

        driver.quit()

        return {"data": ps, "status": 200, "x": "abc"}
    except requests.RequestException as e:
        return {"error": str(e)}, 500


@app.route("/", methods=["GET"])
def hello():
    print("hit -> /")
    try:
        return "hello"
    except requests.RequestException as e:
        return {"error": str(e)}, 500


if __name__ == "__main__":
    # app.run(debug=True)  # Run on http://127.0.0.1:5000
    app.run(host="0.0.0.0", port=5000, debug=True)
