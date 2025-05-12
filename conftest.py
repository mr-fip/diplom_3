import pytest
import requests
from selenium import webdriver
from data import Data
from url import Url

@pytest.fixture(params=['firefox', 'chrome'])
def driver(request):
    
    browser = request.param
    driver = None
    
    try:
        if browser == "chrome":
            print("\nStart Chrome browser")
            driver = webdriver.Chrome()
        elif browser == "firefox":
            print("\nStart Firefox browser")
            driver = webdriver.Firefox()
        
        driver.implicitly_wait(10)
        yield driver
        
    finally:
        if driver is not None:
            print("\nQuitting browser..")
            driver.quit()

@pytest.fixture()
def register_new_user_and_return_credentials():
    payload = Data.USER_CREDENTIALS
    response = requests.post(Url.create_user, json=payload)
    
    if response.status_code != 200:
        pytest.fail(f"Registration failed: {response.text}")
    access_token = response.json()["accessToken"]
    refresh_token = response.json()["refreshToken"]
    
    yield (payload['email'], payload['password'], access_token, refresh_token)
    
    headers = {"Authorization": access_token}
    requests.delete(Url.user_data_management_url, headers=headers)

@pytest.fixture()
def login_user_via_localStorage(register_new_user_and_return_credentials, driver):
    email, password, access_token, refresh_token = register_new_user_and_return_credentials
    driver.get(Url.BASE_URL)
    driver.execute_script(f"localStorage.setItem('accessToken', '{access_token}')")
    driver.execute_script(f"localStorage.setItem('refreshToken', '{refresh_token}')")
    driver.refresh()
    return email, password