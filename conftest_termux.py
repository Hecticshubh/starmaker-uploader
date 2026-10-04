# 1. This setup creates a fresh Chrome profile
#    for the test session.
# 2. If you want to use a saved Chrome profile later,
#    replace the temporary_profile & profile_path block
#    with:
#    profile_path = os.path.expanduser(
#        "~/.starmaker-chrome-profile"
#    )
# 3. For A Saved Profile:
#    Remove shutil.rmtree() after browser.quit().
#    Choose the fixture scope according to your requirements.



import os
import shutil
import tempfile

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture(scope="session")
def driver():
    os.environ["DISPLAY"] = ":0"

    options = Options()

    options.binary_location = (
        "/data/data/com.termux/files/usr/bin/chromium-browser"
    )

    # Create a new Chrome profile for the test session.
    temporary_profile = tempfile.mkdtemp(
        prefix="starmaker-chrome-"
    )

    profile_path = temporary_profile

    options.add_argument(
        f"--user-data-dir={profile_path}"
    )

    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    service = Service(
        "/data/data/com.termux/files/usr/bin/chromedriver"
    )

    browser = webdriver.Chrome(
        service=service,
        options=options
    )

    browser.maximize_window()

    try:
        yield browser

    finally:
        browser.quit()

        # Delete the temporary Chrome profile
        # after the test is finished.
        shutil.rmtree(
            temporary_profile,
            ignore_errors=True
        )


@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, 60)