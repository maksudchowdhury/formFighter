#-------------------------- Selenium preparation ------------------------
#pip install selenium 

#-------------------------- Necessary imports ---------------------------
from selenium import webdriver
from selenium.webdriver.common.by import By

#-------------------------- firefox preparation -------------------------
from selenium.webdriver.firefox.options import Options
options = Options()
options.binary_location = r'./browser/firefox.exe' #location of firefox browser exe file
driver = webdriver.Firefox(executable_path="./driver/geckodriver_firefox_102_minimum.exe",options=options)


#-------------------------- Chrome preparation --------------------------
# ensure that chrome v106.0.5249.x is installed in the default directory 
#driver = webdriver.Chrome(executable_path="./driver/chrome_106_0_5249_61.exe")

#-------------------------- commands from selenium --------------------------
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSdVO68xpcT4nZS6grZUmzaTz6RkZV9dQp1Ph7EVLQqdk45B9Q/viewform?pli=1")
successCount=0

for i in range(50):
    driver.find_element(By.CSS_SELECTOR, "#i5 .AB7Lab").click()
    driver.find_element(By.CSS_SELECTOR, "#i15 .AB7Lab").click()
    driver.find_element(By.CSS_SELECTOR, "#i32 > .uHMk6b").click()
    driver.find_element(By.CSS_SELECTOR, "#i52 > .uHMk6b").click()
    driver.find_element(By.XPATH, "//form[@id=\'mG61Hd\']/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label/div[2]/div/div/div[3]/div").click()
    driver.find_element(By.CSS_SELECTOR, ".qs41qe .AB7Lab").click()
    driver.find_element(By.XPATH, "//form[@id=\'mG61Hd\']/div[2]/div/div[2]/div[8]/div/div/div[2]/div/span/div/label/div[2]/div/div/div[3]/div").click()
    driver.find_element(By.XPATH, "//form[@id='mG61Hd']/div[2]/div/div[2]/div[7]/div/div/div[2]/div/span/div/label/div[2]/div/div/div[3]").click()
    driver.find_element(By.CSS_SELECTOR, ".qs41qe .AB7Lab").click()
    driver.find_element(By.CSS_SELECTOR, "#i118 .AB7Lab").click()
    driver.find_element(By.XPATH, "//form[@id='mG61Hd']/div[2]/div/div[2]/div[9]/div/div/div[2]/div/span/div/label/div[2]/div/div/div[3]/div").click()
    driver.find_element(By.XPATH, "//form[@id=\'mG61Hd\']/div[2]/div/div[2]/div[11]/div/div/div[2]/div/div/div[2]/textarea").click()
    driver.find_element(By.CSS_SELECTOR, ".u3bW4e .KHxj8b").send_keys("nothing")
    driver.find_element(By.CSS_SELECTOR, ".Y5sE8d .NPEfkd").click()
    driver.find_element(By.XPATH, "//a[2]").click()
    successCount+=1
print(successCount)

#-------------------------- ending/closing commands --------------------------
driver.quit()