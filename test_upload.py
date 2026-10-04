import time
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# Configuration

SITE_URL = "https://www.starmakerstudios.com/en"


# User input

def get_user_inputs():
    """Collect song information and lyrics from the user."""

    email = input("Enter email: ").strip()
    password = input("Enter password: ").strip()

    audio_file = input("Enter audio file path: ").strip().strip('"')
    image_file = input("Enter image file path: ").strip().strip('"')

    title = input("Enter title: ").strip()
    artist = input("Enter artist name: ").strip()

    language = input(
        "Enter language (uppercase/lowercase both supported): "
    ).strip()

    if language:
        language = language[0].upper() + language[1:].lower()

    print()
    print("=" * 60)
    print("PASTE LYRICS")
    print("Paste as many lines as you want.")
    print("Minimum 4 lines required.")
    print("Blank lines are also allowed.")
    print("When finished, type End on a separate line.")
    print("=" * 60)

    lyrics = []

    while True:
        line = input()

        if line.strip().lower() == "end":
            break

        lyrics.append(line)

    if len(lyrics) < 4:
        print()
        print("❌ Lyrics must contain at least 4 lines.")
        print(f"❌ Only {len(lyrics)} line(s) entered.")
        raise ValueError("Minimum 4 lyrics lines are required.")

    print("✅ get_user_inputs COMPLETE")

    return (
        email,
        password,
        audio_file,
        image_file,
        title,
        artist,
        language,
        lyrics
    )


# Helper functions

def click_active_next(driver, wait):
    """Click the currently active Next button."""

    next_btn = wait.until(
        lambda d: next(
            (
                button
                for button in d.find_elements(
                    By.CSS_SELECTOR,
                    "div.next_btn.next_active"
                )
                if button.is_displayed() and button.is_enabled()
            ),
            False
        )
    )

    driver.execute_script("arguments[0].click();", next_btn)

    print("✅ click_active_next COMPLETE")


# Login

def login(driver, wait, email, password):
    """Open the site and log in to the upload section."""

    driver.get(SITE_URL)

    driver.find_element(
        By.XPATH,
        "//*[normalize-space()='Upload Tracks']"
    ).click()

    email_input = wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "input[placeholder='Email address']")
        )
    )
    email_input.send_keys(email)

    password_input = wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "input[placeholder='Password']")
        )
    )
    password_input.send_keys(password)

    driver.find_element(
        By.XPATH,
        "//button[normalize-space()='Log in']"
    ).click()

    # Click Upload Tracks after login.
    try:
        time.sleep(2)

        before = set(driver.window_handles)

        upload_btn = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//*[normalize-space()='Upload Tracks']")
            )
        )

        upload_btn.click()

        new_windows = set(driver.window_handles) - before
        if new_windows:
            driver.switch_to.window(list(new_windows)[0])

    except Exception as error:
        print(f"❌ Upload Tracks click FAILED: {error}")
        raise

    print("✅ login COMPLETE")


# Audio upload

def upload_audio(driver, wait, audio_file):
    """Upload the selected audio file."""

    song_input = driver.find_elements(
        By.CSS_SELECTOR,
        "input[type='file']"
    )[0]

    song_input.send_keys(audio_file)

    wait.until(
        lambda d: any(
            element.is_displayed()
            for element in d.find_elements(
                By.CSS_SELECTOR,
                "i.ivu-icon-ios-checkmark"
            )
        )
    )

    click_active_next(driver, wait)

    print("✅ upload_audio COMPLETE")


# Song details

def add_song_details(driver, wait, image_file, title, artist):
    """Upload artwork and enter the song details."""

    image_input = wait.until(
        EC.presence_of_element_located(
            (
                By.CSS_SELECTOR,
                "input[type='file'][accept='image/*']"
            )
        )
    )
    image_input.send_keys(image_file)

    title_input = wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "input[placeholder='Title']")
        )
    )
    title_input.send_keys(title)

    artist_input = wait.until(
        EC.presence_of_element_located(
            (
                By.CSS_SELECTOR,
                'input[placeholder="Artist(s) Use comma\\",\\"to split singers."]'
            )
        )
    )
    artist_input.send_keys(artist)

    checkbox = wait.until(
        EC.presence_of_element_located(
            (
                By.CSS_SELECTOR,
                "input[type='checkbox'].ivu-checkbox-input"
            )
        )
    )

    if not checkbox.is_selected():
        driver.execute_script("arguments[0].click();", checkbox)

    click_active_next(driver, wait)

    print("✅ add_song_details COMPLETE")


# Lyrics options

def set_lyrics_options(driver, wait, language, lyrics):
    """Select lyric settings, language, and enter the lyrics."""

    lyrics_box = wait.until(
        EC.presence_of_element_located(
            (
                By.CSS_SELECTOR,
                "textarea[placeholder='Enter your lyrics here']"
            )
        )
    )

    second_radio = wait.until(
        EC.presence_of_element_located(
            (
                By.CSS_SELECTOR,
                "div.ivu-radio-group > "
                "label.ivu-radio-wrapper.ivu-radio-group-item:nth-child(2)"
            )
        )
    )

    driver.execute_script("arguments[0].click();", second_radio)

    language_dropdown = wait.until(
        EC.element_to_be_clickable(
            (
                By.CSS_SELECTOR,
                "div.ivu-select-selection input.ivu-select-input"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block: 'center'});",
        language_dropdown
    )
    driver.execute_script(
        "arguments[0].click();",
        language_dropdown
    )

    language_option = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, f"//*[normalize-space()='{language}']")
        )
    )
    driver.execute_script("arguments[0].click();", language_option)

    lyrics_box.click()
    lyrics_box.clear()

    for index, line in enumerate(lyrics):
        lyrics_box.send_keys(line)

        if index < len(lyrics) - 1:
            lyrics_box.send_keys(Keys.SHIFT, Keys.ENTER)

    click_active_next(driver, wait)

    print("✅ set_lyrics_options COMPLETE")


# Lyrics synchronization

def sync_lyrics_with_space(driver, wait, lyrics):
    """Send space presses for lyric synchronization and continue."""

    body = driver.find_element(By.TAG_NAME, "body")

    for _ in range(len(lyrics)):
        body.send_keys(Keys.SPACE)

    body.send_keys(Keys.SPACE)

    confirm_button = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//div[contains(@class,'next_btn') and "
                "contains(@class,'next_active') and "
                "normalize-space()='Confirm']"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block: 'center'});",
        confirm_button
    )
    confirm_button.click()

    next_button = driver.find_element(
        By.XPATH,
        "//div[contains(@class,'next_btn') and "
        "contains(@class,'next_active') and "
        "normalize-space()='Next']"
    )

    driver.execute_script("arguments[0].click();", next_button)

    print("✅ sync_lyrics_with_space COMPLETE")


# Test flow

def test_upload(driver: WebDriver, wait: WebDriverWait):
    """Run the complete track upload workflow."""

    (
        email,
        password,
        audio_file,
        image_file,
        title,
        artist,
        language,
        lyrics
    ) = get_user_inputs()

    login(driver, wait, email, password)

    upload_audio(driver, wait, audio_file)

    add_song_details(
        driver, wait, image_file, title, artist
    )

    set_lyrics_options(
        driver, wait, language, lyrics
    )

    sync_lyrics_with_space(
        driver, wait, lyrics
    )

    print()
    print("=" * 60)
    print("✅ test_upload COMPLETE")
    print("=" * 60)