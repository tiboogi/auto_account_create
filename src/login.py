from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

data = []
ErrorList = []

with open('account.txt', 'r') as file:
    for line in file:
        username, email, password, a = line.replace("'", '').strip().split(',')
        data.append({'username': username, 'email': email, 'password': password})

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

counter = 0
skip = False
for account in data:
    if not skip:
        driver = webdriver.Chrome(chrome_options)
        driver.get('https://twitter.com')
        time.sleep(3)
    skip = False
    counter += 1
    print('email:'+str(account['email'])+'登入開始')
    email = driver.find_element(By.NAME, "text")
    email.send_keys(account['email'])
    buttons = driver.find_elements(By.CSS_SELECTOR, 'div[role="button"]')
    for j in buttons:
        if j.text == '下一步' or j.text == 'Next':
            j.click()
            print('點擊下一步')
            break
    time.sleep(2)

    try:
        check = driver.find_element(By.CSS_SELECTOR, 'input[autocomplete="on"]')
        check.send_keys(account['username'])
        buttons = driver.find_elements(By.CSS_SELECTOR, 'div[role="button"]')
        for j in buttons:
            if j.text == '下一步' or j.text == 'Next':
                j.click()
                print('驗證使用者帳號，點擊下一步')
                break
        time.sleep(2)
    except:
        print('無需輸入使用者名稱')
    time.sleep(1)

    try:
        pwd = driver.find_element(By.CSS_SELECTOR, 'input[autocomplete="current-password"]')
        pwd.send_keys(account['password'])
        print('輸入密碼')
    except:
        print(str(account['email']) + '發生問題')
        ErrorList.append(account['email'])
        skip = True
        continue

    buttons = driver.find_elements(By.CSS_SELECTOR, 'div[role="button"]')
    for j in buttons:
        if j.text == '登入' or j.text == 'Log in':
            j.click()
            print('點擊登入')
            break
    time.sleep(3)
    try:
        button = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]')  # 驗證start
        button.click()
        print('驗證start')
    except:
        print('無需start')
print(f'共開啟{counter}個帳號,有{len(ErrorList)}個問題帳號：')
print(ErrorList)

