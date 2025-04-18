from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

# 设置 ChromeDriver 路径
s = Service(executable_path=r"C:/Program Files/Google/Chrome/Application/chromedriver.exe")
driver = webdriver.Chrome(service=s)

# 打开目标页面
url = "https://demoqa.com/automation-practice-form"
driver.get(url)
driver.maximize_window()

try:
    # 输入姓名
    first_name = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "firstName"))
    )
    first_name.send_keys("小宝贝")

    last_name = driver.find_element(By.ID, "lastName")
    last_name.send_keys("测试员")

    # 输入手机号
    mobile = driver.find_element(By.ID, "userNumber")
    mobile.send_keys("1234567890")

    # 输入日期
    date_of_birth = driver.find_element(By.ID, "dateOfBirthInput")
    date_of_birth.click()

    month_dropdown = Select(driver.find_element(By.CLASS_NAME, "react-datepicker__month-select"))
    month_dropdown.select_by_visible_text("March")

    year_dropdown = Select(driver.find_element(By.CLASS_NAME, "react-datepicker__year-select"))
    year_dropdown.select_by_value("2000")

    driver.find_element(By.XPATH, "//div[contains(@class,'react-datepicker__day') and text()='15']").click()

    # 选择爱好
    hobbies = ["Sports", "Reading"]
    for hobby in hobbies:
        hobby_checkbox = driver.find_element(By.XPATH, f"//label[text()='{hobby}']")
        driver.execute_script("arguments[0].scrollIntoView();", hobby_checkbox)
        hobby_checkbox.click()

    # 提交表单
    submit_button = driver.find_element(By.ID, "submit")
    driver.execute_script("arguments[0].scrollIntoView();", submit_button)
    submit_button.click()

    # 检查提交结果
    success_msg = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, "modal-title"))
    )
    if "Thanks" in success_msg.text:
        print("提交成功！")
    else:
        print("提交失败？")

except Exception as e:
    print(f"发生错误: {e}")
finally:
    time.sleep(5)
    driver.quit()