import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", help="Choose browser: chrome or firefox",
                     default="chrome")
    parser.addoption("--language", action="store", help="Choose language: ru, en...",
                     default="ru")

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    language = request.config.getoption("language")
    browser = None
    if browser_name == "chrome":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        print(f"\nStarting test with CHROME:{language}-version")
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", language)
        print(f"\nStarting test with FIREFOX:{language}-version")
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        print("Error: unavailable browser")
    yield browser
    print("\nquit browser..")
    browser.quit()


