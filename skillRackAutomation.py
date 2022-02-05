from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager as CM
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait as DWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located as present
from selenium.webdriver.support.expected_conditions import element_to_be_clickable as isclickable
from selenium.webdriver.support.expected_conditions import visibility_of_element_located as isvisible
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from easygui import msgbox, passwordbox, codebox, enterbox, ynbox
from keyboard import is_pressed, wait
from os.path import realpath
from pickle import dump, load
from time import sleep

line_xp = r"/html/body/div[2]/div[1]/div/div[2]/div/form/div[3]/div/div[2]/div/div/div/div[1]/div[3]/table/tbody/tr/td/div/div[1]/textarea"
c = "/html/body/div[2]/div[1]/div/div[2]/div/form/div[3]/div/div[2]/div/div/div/div[4]/div/div/button[1]"
c_code = "/html/body/div[2]/div[1]/div/div[2]/div/form/div[3]/div/div[2]/div/div/div/div[4]/div/div/div[1]/pre/code"
login_details = realpath("skill rack.pkl")
save = False

try:
    email, password = load(open(login_details, "rb"))
    print(f"Login details : {login_details}")

except FileNotFoundError:
    email = enterbox("Enter your E Mail:")
    password = passwordbox("Enter your Password:")
    save = True

if email is None or password is None:
    exit("Email Or Password cannot be None")

def byid(id):
    return driver.find_element(By.ID,id)

def byxp(xp):
    return driver.find_element(By.XPATH,xp)

driver = Chrome(executable_path = CM().install())
driver.get("https://www.skillrack.com/")

byid("j_id_e").click()
byid("input_j_id_s").send_keys(email)
byid("input_j_id_u").send_keys(password)
byid("j_id_w").click()

DWait(driver,3600).until(present((By.ID,"j_id_5z"))).click()
dump((email,password),open(login_details,"wb"))
print("....Login details saved....")

code_editor = DWait(driver,3600).until(present((By.ID,"editortxtCode")))
action = ActionChains(driver)

copy_from_sol = None
while copy_from_sol is None:
   copy_from_sol = ynbox(msg = "Do you want to copy from solution?\nIf not enabled, Select cancel.",title = "SkillRack Automation",choices = ["ok","cancel"])

print(copy_from_sol)

while not is_pressed("esc"):
    if copy_from_sol:
        DWait(driver,100).until(present((By.ID,"showbtn"))).click()
        DWait(driver,100).until(isclickable((By.XPATH,c))).click()
        DWait(driver,100).until(isclickable((By.XPATH,c_code))).click()
        code = byid("solnC").text
        print(f"Code : {code}")
    else:
        code = None
        while code is None:
           code = codebox("Paste the code here")
    code_editor = DWait(driver, 3600).until(present((By.ID, "editortxtCode")))
    code_editor.click()
    action.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
    action.key_down(Keys.BACKSPACE).key_up(Keys.BACKSPACE).perform()
    input_code = byxp(line_xp)
    for i in code.split("\n"):
        input_code.clear()
        input_code.send_keys(i)
        input_code.send_keys(Keys.SPACE)
        input_code.send_keys("\n")
    if copy_from_sol:
        DWait(driver,200).until(isclickable((By.ID,"j_id_bc"))).click()
        DWait(driver,200).until(isclickable((By.ID,"j_id_8e"))).click()
        DWait(driver,200).until(isclickable((By.ID,"pctbl:0:j_id_5b"))).click()
        DWait(driver,200).until(isclickable((By.ID,"j_id_5z"))).click()
    else:
        wait("alt")
driver.quit()



