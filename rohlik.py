import configparser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# nacti konfig
config = configparser.ConfigParser()
config.read("user.conf")

driver = webdriver.Chrome(executable_path="chromedriver", service_log_path=config["rohlik"]["log"])
driver.get("https://www.rohlik.cz/")

# nechceme responsive verzi
driver.set_window_size(1200, 600)

# zavreme newsletter
driver.find_element_by_css_selector("body").send_keys(Keys.ESCAPE)

# najdeme tlacitko pro prihlaseni a pockame
css_selector = "a[href='/uzivatel/prihlaseni']"
driver.find_element(By.CSS_SELECTOR, css_selector).click()

# najdeme input pro prihlaseni
css_selector = "#frm-loginForm-email"
user_input = driver.find_element_by_css_selector(css_selector)
user_input.send_keys(config["rohlik"]["user"])

# najdeme input pro heslo
css_selector = "#frm-loginForm-password"
user_input = driver.find_element_by_css_selector(css_selector)
user_input.send_keys(config["rohlik"]["password"])
user_input.send_keys(Keys.RETURN)

# najdeme tlacitko rohlikovac
css_selector = "a[href='/stranka/rohlikovac']"
driver.find_element(By.CSS_SELECTOR, css_selector).click()

# najdeme tlacitko pro spusteni rohlikovace
css_selector = "a[href='/stranka/rohlikovac?do=creditForge-roll']"
driver.find_element(By.CSS_SELECTOR, css_selector).click()

# zavreme modal
css_selector = "rel='rohlikovac'"
driver.find_element(By.CSS_SELECTOR, css_selector).click()

driver.close()