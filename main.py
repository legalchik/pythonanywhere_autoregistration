import os, time
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options


def add(q):
    with open("logins.txt", 'a') as file:
        file.write(f'{q}\n')


def get_browser():
    options = Options()
    options.headless = False # True - hide

    browser = webdriver.Firefox(os.path.abspath(os.curdir), options=options)
    browser.implicitly_wait(5)
    return browser


def reg(browser, username, email, password):

    browser.get('https://www.pythonanywhere.com/registration/register/beginner/')

    username_input = browser.find_element_by_css_selector("input[name='username']")
    email_input = browser.find_element_by_css_selector("input[name='email']")
    password1_input = browser.find_element_by_css_selector("input[name='password1']")
    password2_input = browser.find_element_by_css_selector("input[name='password2']")
    tos_input = browser.find_element_by_css_selector("input[name='tos']")

    username_input.send_keys(username)
    email_input.send_keys(email)
    password1_input.send_keys(password)
    password2_input.send_keys(password)
    sleep(1)
    tos_input.click()

    login_button = browser.find_element_by_xpath("//button[@type='submit']")
    login_button.click()

    browser.implicitly_wait(2)
    end_btn = browser.find_element_by_css_selector("button[data-role='end']")
    end_btn.click()

    return browser


def main():
    browser = get_browser()

    browser.get("https://10minutemail.org/")
    email = browser.find_element_by_css_selector("input[class='mailtext']").get_attribute("value")
    browser = reg(browser, email.split("@")[0], email, email)
    browser.implicitly_wait(1)
    sleep(4)
    browser.get("https://10minutemail.org/")
    browser.find_elements_by_link_text("PythonAnywhere: confirm your email address")[0].click()
    browser.implicitly_wait(1)
    browser.find_elements_by_link_text("click this link")[0].click()
    add(email)
    browser.implicitly_wait(5)

    sleep(20)
    browser.close()
    browser.switch_to.window(browser.window_handles[0])
    browser.close()


if __name__ == "__main__":
    n = 0
    # while True:
    start_time = time.time()
    main()
    n += 1
    print(f"{n} {time.time() - start_time} seconds")
    sleep(2)
