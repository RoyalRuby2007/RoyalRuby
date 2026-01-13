from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
import time  
import pandas as pd
from pathlib import Path

# Get the folder where the script is actually located
script_location = Path(__file__).parent

# Join that path with your filename
file_path = str(script_location / "test.csv")

df = pd.read_csv(file_path)

def from_ma_sv_to_gmail_of_the_student(ma_sv):
    return f"{ma_sv}@vnu.edu.vn"

def get_the_value_from_the_dataset():
    student_email_and_data = []
    data_records = df.to_dict(orient = "records")
    for student_data in data_records:
        content_of_the_gmail = f"{student_data["STT"]} {student_data["Mã_SV"]} {student_data["Họ_và_tên"]} {student_data["Ngày_sinh"]} {student_data["Lớp"]} {student_data["Điểm_TP_1"]} {student_data["Điểm_TP_2"]} {student_data["Tổng_điểm"]}"
        student_email_and_data.append([student_data["Mã_SV"], content_of_the_gmail])
    return student_email_and_data

student_email_and_data = get_the_value_from_the_dataset()


#automatically install the undetected bot chromedriver
driver = uc.Chrome()
#open gmail
driver.get("https://mail.google.com/mail/u/0/#inbox")

for student_data in student_email_and_data:
    #Click the compose button of gmail
    WebDriverWait(driver, 1000).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[6]/div[3]/div/div[2]/div[2]/div[1]/div[1]/div/div"))
    )
    compose = driver.find_element(By.XPATH, "/html/body/div[6]/div[3]/div/div[2]/div[2]/div[1]/div[1]/div/div")
    compose.click()

    #Fill the receiver gmail and subject
    WebDriverWait(driver, 1000).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[25]/div[2]/div/div/div[1]/div[2]/div[1]/div[1]/div/div/div/div[2]/div/div/div[4]/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[1]/td[2]/div/div/div[1]/div/div[3]/div/div/div/div/div/input"))
    )

    receiver_gmail_input = driver.find_element(By.XPATH, "/html/body/div[25]/div[2]/div/div/div[1]/div[2]/div[1]/div[1]/div/div/div/div[2]/div/div/div[4]/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[1]/td[2]/div/div/div[1]/div/div[3]/div/div/div/div/div/input")
    receiver_gmail_input.send_keys(from_ma_sv_to_gmail_of_the_student(student_data[0]))

    subject_input = driver.find_element(By.XPATH, "/html/body/div[25]/div[2]/div/div/div[1]/div[2]/div[1]/div[1]/div/div/div/div[2]/div/div/div[4]/table/tbody/tr/td[2]/form/div[3]/input")
    subject_input.send_keys("Bảng điểm của sinh viên")

    #Input the content of the gmail
    WebDriverWait(driver, 1000).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[25]/div[2]/div/div/div[1]/div[2]/div[1]/div[1]/div/div/div/div[2]/div/div/div[4]/table/tbody/tr/td[2]/table/tbody/tr[1]/td/div/div[2]/div[2]/div[3]/div/table/tbody/tr/td[2]/div[2]/div/div[1]"))
    )
    input_content = driver.find_element(By.XPATH, "/html/body/div[25]/div[2]/div/div/div[1]/div[2]/div[1]/div[1]/div/div/div/div[2]/div/div/div[4]/table/tbody/tr/td[2]/table/tbody/tr[1]/td/div/div[2]/div[2]/div[3]/div/table/tbody/tr/td[2]/div[2]/div/div[1]")
    input_content.send_keys(student_data[1])

    #Click the send Button
    WebDriverWait(driver, 1000).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[25]/div[2]/div/div/div[1]/div[2]/div[1]/div[1]/div/div/div/div[2]/div/div/div[4]/table/tbody/tr/td[2]/table/tbody/tr[2]/td/div/div/div[4]/table/tbody/tr/td[1]/div/div[2]/div[1]"))
    )
    send_button = driver.find_element(By.XPATH, "/html/body/div[25]/div[2]/div/div/div[1]/div[2]/div[1]/div[1]/div/div/div/div[2]/div/div/div[4]/table/tbody/tr/td[2]/table/tbody/tr[2]/td/div/div/div[4]/table/tbody/tr/td[1]/div/div[2]/div[1]")
    send_button.click()
    time.sleep(2)

time.sleep(10000)
driver.quit()