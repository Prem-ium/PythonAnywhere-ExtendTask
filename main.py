import os, time
from selenium                               import webdriver
from selenium.webdriver.common.by           import By
from selenium.webdriver.chrome.options      import Options
from webdriver_manager.chrome               import ChromeDriverManager
from selenium.webdriver.chrome.service      import Service
from dotenv                                 import load_dotenv

load_dotenv()

def get_driver():
    """Initialize and return a Selenium WebDriver instance."""
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
    if 'LOGIN' not in os.environ:
        raise ValueError("Environment variable 'LOGIN' is missing.")
    LOGIN = os.environ['LOGIN'].split(',')
    for log in LOGIN:
        creds = log.split(':')
        print(f'Credentials Found for PythonAnywhere Account: {creds[0]}')
        driver = get_driver()
        driver.get('https://www.pythonanywhere.com/login/')
        driver.find_element(By.XPATH, value='//*[@id="id_auth-username"]').send_keys(creds[0])
        driver.find_element(By.XPATH, value='//*[@id="id_auth-password"]').send_keys(creds[1])
        driver.find_element(By.XPATH, value='//*[@id="id_next"]').click()

        time.sleep(5)
        driver.get(f'https://www.pythonanywhere.com/user/{creds[0]}/tasks_tab/')
        time.sleep(5)
        
        for i in range(1, 15):
            try:
                driver.find_element(By.XPATH, value=f'//*[@id="id_scheduled_tasks_table"]/div/div/table/tbody/tr[{i}]/td[6]/button[4]').click()
            except Exception as e:
                driver.quit()
                print(f'{i-1} tasks were found & extended.')
                return
        driver.quit()
if __name__ == '__main__':
    main()