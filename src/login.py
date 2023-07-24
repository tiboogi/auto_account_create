from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

data = []
ErroList = []
with open('account.txt', 'r') as file:
    for line in file:
        username, email, password, a = line.replace("'", '').strip().split(',')
        data.append({'username': username, 'email': email, 'password': password})
counter = 0
for account in data:
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    # options.binary_location = "path to Google Chrome"
    # chrome_driver_binary = "/path/to/chromedriver"  # Replace with the correct path to chromedriver
    driver = webdriver.Chrome(chrome_options)
    driver.get('https://twitter.com')
    time.sleep(3)
    # sign_up = driver.find_element(By.CSS_SELECTOR, 'a[href="/i/flow/signup"]')
    # sign_up.click()
    print('email:'+str(account['email'])+'登入開始')
    name = driver.find_element(By.NAME, "text")
    name.send_keys(account['email'])
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
        ErroList.append(account['email'])
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
    # driver.close()
print(ErroList)
# # email = driver.find_element_by_name("name")
# # email.send_keys('aaaa@gmail.com')

