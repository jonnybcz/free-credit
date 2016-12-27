import random
import configparser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

pieces_of_pizza = ["#p1", "#p2", "#p3", "#p4", "#p5", "#p6"]

# nacti konfig
config = configparser.ConfigParser()
config.read("user.conf")

driver = webdriver.Chrome(executable_path="chromedriver", service_log_path=config["damejidlo"]["log"])
driver.get("https://www.damejidlo.cz/uzivatel/prihlaseni")

# nechceme responsive verzi
driver.set_window_size(1200, 600)

# zavreme newsletter
driver.find_element_by_css_selector("body").send_keys(Keys.ESCAPE)

# najdeme input pro prihlaseni
css_selector = "section #frm-loginForm-email"
user_input = driver.find_element_by_css_selector(css_selector)
user_input.send_keys(config["damejidlo"]["user"])

# najdeme input pro heslo
css_selector = "section #frm-loginForm-password"
user_input = driver.find_element_by_css_selector(css_selector)
user_input.send_keys(config["damejidlo"]["password"])
user_input.send_keys(Keys.RETURN)

# najdeme tlacitko rohlikovac
css_selector = "a[href='/facebook/vypecene-kredity']"
driver.find_element(By.CSS_SELECTOR, css_selector).click()

# najdeme tlacitko pro spusteni rohlikovace
css_selector = random.choice(pieces_of_pizza)
driver.find_element(By.CSS_SELECTOR, css_selector).click()

driver.implicitly_wait(5)
driver.close()
