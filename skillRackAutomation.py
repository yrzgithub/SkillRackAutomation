# Handle this code with care or else it may misbehave.
# Everything in this project is only for educational purpose.

import easygui 
import keyboard
from selenium import webdriver as Driver
from selenium.webdriver.support.expected_conditions import presence_of_element_located as located
from selenium.webdriver.support.wait import WebDriverWait as Wait
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager as cm
from selenium.webdriver.chrome.service import Service

driver = Driver.Chrome(service = Service(cm().install()))

driver.get("https://www.skillrack.com")
driver.maximize_window()

driver.find_element_by_id("j_id_e").click()  # login button

email = easygui.enterbox("Enter your E Mail:")
driver.find_element_by_id("input_j_id_s").send_keys(email)  # email

password = easygui.passwordbox("Enter your Password:")
driver.find_element_by_id("input_j_id_u").send_keys(password)  # password

driver.find_element_by_id("j_id_w").click()  # submit

easygui.msgbox(title="Note:",msg="select the task and open the code box.\nPress alt+s to open code box and paste the code in code box.\nAgain Press alt+s to repeat the action or to paste another code.\nFor Python, Set the cursor and press ctrl to copy the code line by line.")

xpath = "/html/body/div[2]/div[1]/div/div[2]/div/form/div[2]/div/div[2]/div/div/div/div[1]/div[3]/table/tbody/tr/td/div/div[1]/textarea"

cont=""
while cont!="Nope":
    Wait(driver, 3600).until(located((By.XPATH, xpath)))
    code = str(easygui.codebox("Paste the code here"))
    ip = driver.find_element_by_xpath(xpath)
    ip.clear()
    iplang = str(driver.find_element_by_id("langs_label").text)
    code = code.split("\n")
    for i in code:
        if "Python" in iplang:
            if i == "":
                continue
            keyboard.wait("ctrl")
        ip.send_keys(i.strip(" ") + " ")
        ip.send_keys("\n")

    keyboard.wait("alt+s")
    cont = easygui.buttonbox(msg="Do you want to continue?",choices=["Yup", "Nope"])

easygui.msgbox("This is only for educational purpose")
driver.quit()
