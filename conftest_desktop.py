# CHROME PROFILE CONFIGURATION
# Windows / Linux / macOS
#
# 1. CURRENT SETUP:
#    # Create a new Chrome profile for the test session.
#
# 2. TO USE A SAVED CHROME PROFILE LATER:
#    Replace the temporary_profile and profile_path block with:
#
#    profile_path = os.path.expanduser(
#        "~/.starmaker-chrome-profile"
#    )
#
# 3. FOR A SAVED PROFILE:
#    Remove shutil.rmtree() after browser.quit().
#    Choose the fixture scope according to your requirements.

import os
import shutil
import tempfile

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture (scope="session")
def driver():
    # Configure Chrome browser options.
    options = Options()

    # Create a fresh temporary Chrome profile for each test.
    temporary_profile = tempfile.mkdtemp(
        prefix="starmaker-chrome-"
    )
    profile_path = temporary_profile

    options.add_argument(
        f"--user-data-dir={profile_path}"
    )

    # Launch Chrome with the configured options.
    browser = webdriver.Chrome(options=options)

    # Maximize the browser window.
    browser.maximize_window()

    try:
        # Provide the browser instance to the test.
        yield browser

    finally:
        # Close Chrome after the test finishes.
        browser.quit()

        # Delete the temporary Chrome profile.
        shutil.rmtree(
            temporary_profile,
            ignore_errors=True
        )


@pytest.fixture
def wait(driver):
    # Wait up to 60 seconds for a condition.
    return WebDriverWait(driver, 60)