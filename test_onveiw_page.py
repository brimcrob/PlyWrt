import re
import pytest
import logging
from playwright.sync_api import Page, expect
from playwright.sync_api import sync_playwright

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

@pytest.fixture(scope="session")

#defines browser
def browser():
    with sync_playwright() as p:
        #log browser launch
        logger.info('Browser launched')
        browser = p.chromium.launch(headless= True,)
        yield browser
        browser.close()
        logger.info('Browser Closed')

#testing that the username field is on page
def test_login_username(browser):
    #logstart
    logger.info('Browser opend')
    #creats new instance of browser
    #log new log in page
    logger.info('Starting Test -Check Username Text Box')
    page = browser.new_page()
    #go to page login screen
    page.goto('https://test.simba.eks.omnichan.co.uk/auth/login')
    logger.info('Navigated to OneView Log-in screen')
    #check fpr username text box
    username_textbox = page.get_by_role('textbox', name='Username')
    username_textbox.highlight()
    page.screenshot(path="screenshots/Username_Field_Displayed.png")
    #Assert that the textbox is present
    assert username_textbox.is_visible(), 'Username text input is not visable on screen'
    logger.info('Login Username Field Is displayed on OneView Login screen')
    page.close()
    logger.info('Test Ends')

#testing that the password field is on page
def test_login_password(browser):
    logger.info('Starting Test - Check Password Text Box')
    #creats new instance of browser
    page = browser.new_page()
    #go to page login screen
    page.goto('https://test.simba.eks.omnichan.co.uk/auth/login')
    logger.info('Navigated to OneView Log-in screen')
    #check fpr username text box
    password_textbox = page.get_by_role('textbox', name='Password')
    password_textbox.highlight()
    page.screenshot(path="screenshots/Password_Field_Displayed.png")
    #Assert that the textbox is present
    assert password_textbox.is_visible(), 'Password input is not visable on screen'
    logger.info('Login Password Field Is displayed on OneView Login screen')

    page.close()
    logger.info('Test Ends')

#testing that forogot pass is one page
def test_login_forgotpass(browser):
    logger.info('Starting Test - Check Frpgpt password Link')
    #creats new instance of browser
    page = browser.new_page()
    #go to page login screen
    page.goto('https://test.simba.eks.omnichan.co.uk/auth/login')
    logger.info('Navigated to OneView Log-in screen')
    #check fpr username text box
    username_forgotpass = page.get_by_role('link', name='Forgot password?')
    #Assert that the link is present
    assert username_forgotpass.is_visible(), 'Password input is not visable on screen'
    logger.info('Login Frogot Pass Is displayed on OneView Login screen')

    page.close()
    logger.info('Test Ends')

#testing login button is on page
def test_login_loginbutton(browser):
    #creats new instance of browser
    page = browser.new_page()
    #go to page login screen
    page.goto('https://test.simba.eks.omnichan.co.uk/auth/login')
    logger.info('Navigated to OneView Log-in screen')
    #check fpr username text box
    user_loginbutton = page.get_by_role('button', name='LOGIN')
    #Assert that the link is present
    assert user_loginbutton.is_visible(), 'login button is not visable on screen'
    logger.info('Login Buttong Is displayed on OneView Login screen')

    page.close()
    logger.info('Test Ends')

#testing that image in on page
def test_login_loginscreenImage(browser):
    #creats new instance of browser
    page = browser.new_page()
    #go to page login screen
    page.goto('https://test.simba.eks.omnichan.co.uk/auth/login')
    logger.info('Navigated to OneView Log-in screen')
    #check fpr username text box
    user_loginImage = page.locator(".right__container")
    #Assert that the link is present
    assert user_loginImage.is_visible(), 'lmage on the login screen is not being displayed'
    page.close()
    logger.info('End Test')
    
#testing the login buttin is intialy disabled
def test_login_loginButtonDisabled(browser):
    #creats new instance of browser
    page = browser.new_page()
    #go to page login screen
    page.goto('https://test.simba.eks.omnichan.co.uk/auth/login')
    logger.info('Navigated to OneView Log-in screen')
    #check fpr username text box
    user_ButtonDisable =  page.get_by_role('button', name='LOGIN')
    #Assert that the link is present
    assert user_ButtonDisable.is_disabled(), 'login button is not disabled'
    logger.info('Login Button is disabled')
    logger.info('End Test')


""" Tests for  the SendLink Screens- """


def test_login_ForgotBrowserTitle(browser):
    #logstart
    logger.info('Browser opend')
    #creats new instance of browser
    #log new log in page
    logger.info('Starting Test -Check Page Header')
    page = browser.new_page()
    #go to page login screen
    page.goto('https://test.simba.eks.omnichan.co.uk/auth/login')
    logger.info('Navigated to OneView Send Link screen')
    #check fpr username text box
    ForgotPass_Title = page.title()
    #Assert that the textbox is present
    assert ForgotPass_Title == 'Stellar OneView', f'Expected title to be "Stellar OneView",but got {ForgotPass_Title}'
    logger.info('Send Link Page Header is correct')

    page.close()
    logger.info('Test Ends')



""" Test logging in to the OneView site  """
def login(page, username, password):
    """
    Function to perform login on the website.
    :param page: Playwright page object
    :param username: Username for login
    :param password: Password for login
    """
    # Navigate to the login page
    page.goto("https://test.simba.eks.omnichan.co.uk/auth/login")

    # Fill in the username and password fields
    page.get_by_placeholder("Username...").fill(username)
    page.get_by_placeholder("Password...").fill(password)

    # Click the login button
    page.get_by_role("button", name="Login").click()

    # Wait for navigation or a specific element to ensure login was successful
    page.wait_for_url('https://test.simba.eks.omnichan.co.uk/admin')  # Replace with the correct URL after login

    """ # Optionally, verify that login was successful
    assert page.is_visible('text=Welcome'), "Login failed" """

# test that admin page has loaded 

def test_login_sucessfull(browser):
     #logstart
    logger.info('Browser opend')
    #creats new instance of browser
    #log new log in page
    logger.info('Starting Test -Check Username Text Box')
    page = browser.new_page()
    #go to page login screen
    page.goto('https://test.simba.eks.omnichan.co.uk/auth/login')
    logger.info('Navigated to OneView Log-in screen')
    #enter username and password
    login(page,'superadmin','Pa55word')
    #dashboard loaded
    Admin_page = page.title()
    assert Admin_page == 'Stellar OneView - Admin Configurations', f'Expected title "Stellar OneView - Admin Configurations" but got {Admin_page}'
    page.close()
    logger.info('End Test')

#test going to the admin 

def test_admin_search_user(browser):
     #logstart
    logger.info('Browser opend')
    #creats new instance of browser
    #log new log in page
    logger.info('Starting Test -Check Username Text Box')
    page = browser.new_page()
    #go to page login screen
    page.goto('https://test.simba.eks.omnichan.co.uk/auth/login')
    logger.info('Navigated to OneView Log-in screen')
    #enter username and password
    login(page,'superadmin','Pa55word')
    page.get_by_role("button", name="Login").click()
    people_nav = page.get_by_role("button", name="People")
    user_nav = page.get_by_text("Users")
    people_nav.click()
    logger.info("People option is selected")
    user_nav.click()
    logger.info("User Option is selected")


""" 
    page.get_by_role("button", name="People").click()
    page.get_by_text("Users").click()
    page.get_by_role("textbox", name="Search...").click()
    page.get_by_role("textbox", name="Search...").fill("bm")
    page.get_by_role("cell", name="BM Brian McRoberts").click() 
    """


