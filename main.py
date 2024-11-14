import os, time
from selenium                               import webdriver
from selenium.webdriver.common.by           import By
from selenium.webdriver.chrome.options      import Options
from webdriver_manager.chrome               import ChromeDriverManager
from selenium.webdriver.chrome.service      import Service
from dotenv                                 import load_dotenv

load_dotenv()

def getDriver():
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--headless')
    try:
        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=chrome_options)
    except Exception as e:
        driver = webdriver.Chrome(options=chrome_options)
    return driver

def main():
    LOGIN = os.environ['LOGIN'].split(':')
    driver = getDriver()

    driver.get('https://www.pythonanywhere.com/login/')

    driver.find_element(By.XPATH, value='//*[@id="id_auth-username"]').send_keys(LOGIN[0])
    driver.find_element(By.XPATH, value='//*[@id="id_auth-password"]').send_keys(LOGIN[1])

    driver.find_element(By.XPATH, value='//*[@id="id_next"]').click()

    driver.get(f'https://www.pythonanywhere.com/user/{LOGIN[0]}/tasks_tab/')
    time.sleep(15)
    
    # Expand ten tasks, change the range to expand more or less
    for i in range(1, 11):
        try:
            driver.find_element(By.XPATH, value=f'//*[@id="id_scheduled_tasks_table"]/div/div/table/tbody/tr[{i}]/td[6]/button[4]').click()
        except Exception as e:
            print(f'{i-1} tasks were found & extended.\n')
            break
    driver.quit()

if __name__ == '__main__':
    main()