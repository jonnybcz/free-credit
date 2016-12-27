import configparser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# nacti konfig
config = configparser.ConfigParser()
config.read("user.conf")

driver = webdriver.Chrome(executable_path="chromedriver", service_log_path=config["slevomat"]["log"])
driver.get("https://www.slevomat.cz/kolotoc-stesti")

# nechceme responsive verzi
driver.set_window_size(1200, 600)

# zavreme newsletter
driver.find_element_by_css_selector("body").send_keys(Keys.ESCAPE)

driver.implicitly_wait(3)

# najdeme tlacitko pro prihlaseni
css_selector = ".wheel-container .desktop-only a"
driver.find_element_by_css_selector(css_selector).click()

# najdeme input pro prihlaseni
css_selector = "input[type='email']"
user_input = driver.find_element_by_css_selector(css_selector)
user_input.send_keys(config["slevomat"]["user"])

# najdeme input pro heslo
css_selector = "input[type='password']"
user_input = driver.find_element_by_css_selector(css_selector)
user_input.send_keys(config["slevomat"]["password"])
user_input.send_keys(Keys.RETURN)

# prejdeme na stranku s kolotocem
driver.get("https://www.slevomat.cz/kolotoc-stesti")

try:
    while True:
        # najdeme tlacitko pro spusteni kolotoce
        css_selector = ".wheel-button.js-wheel-button"
        driver.find_element(By.CSS_SELECTOR, css_selector).click()
        # pockame na dotoceni, mozna budeme tocit znovu
        driver.implicitly_wait(20)
except:
    print("pak zavrit driver")
    driver.implicitly_wait(5)
    driver.close()
