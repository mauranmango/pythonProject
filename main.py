import chromedriver_autoinstaller
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

opt = webdriver.ChromeOptions()
opt.add_experimental_option('detach', True)


# CREATE THE WEBDRIVER
chromedriver_autoinstaller.install()
driver = webdriver.Chrome(options=opt)
driver.maximize_window()
driver.get('https://www.acb.com/club/index/temporada_id/2022')
# assert "Python Test" in driver.title

# LOAD ALL THE TEAMS
teams = driver.find_elements(By.CLASS_NAME, 'club')
print('test')