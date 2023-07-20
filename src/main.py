from selenium import webdriver

# options = webdriver.ChromeOptions()
# options.binary_location = "/Users/tiboogi/Downloads/Google Chrome.app/Contents/MacOS/Google Chrome"
# chrome_driver_binary = "/path/to/chromedriver"  # Replace with the correct path to chromedriver
driver = webdriver.Chrome()
driver.get('https://www.gamer.com.tw/index2.php')
