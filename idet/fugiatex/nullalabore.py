from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

LEAVE = (By.XPATH, '//*[@id="guild-context-leave-guild"]/div')

# Usage example with WebDriverWait
def leave_guild(driver):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(LEAVE)).click()
