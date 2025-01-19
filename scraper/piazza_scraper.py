from requests_html import  HTMLSession
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

driver = webdriver.Chrome()

session = HTMLSession()

# go through post/... to get pages
# URL = "https://piazza.com/class/ky0ewiregcz421/"
URL = "https://piazza.com/class/ky0ewiregcz421/post/"

driver.get(URL)

driver.implicitly_wait(2)

driver.get(URL)
username = driver.find_element(By.ID, 'email_field')

password = driver.find_element(By.ID, 'password_field')

password.send_keys(Keys.RETURN)  
driver.implicitly_wait(2)

def queryFun(post):
    uri = URL + str(post)
    driver.get(uri)

    try:
        WebDriverWait(driver, 1).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert.accept()  # or .dismiss() or .send_keys()
        return "not here"
    except:
        print("No alert present")

    title = "" 
    try:
        title = driver.find_element(By.ID, 'postViewSummaryId').text
    except:
        title = "Not Found"

    question = ""
    try:
        question = driver.find_element(By.CSS_SELECTOR, '.render-html-content.overflow-hidden.latex_process').text
    except:
        question = "Note Found"
    
    student_answer = ""
    try:
        student_answer = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, '//article[@data-id="s_answer"]')))
        student_answer = student_answer.find_element(By.CSS_SELECTOR, '.render-html-content.overflow-hidden.latex_process').text
    except:
        student_answer = "Not Found"

    author = ""
    try: 
        author = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.text-right.col')))
        author = author.find_element(By.XPATH, '//span[@data-id="contributors"]').text
    except:
        author = "Not Found"
    
    post_type = ""
    try:
        post_type = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.text-left.pl-0.col-auto')))
        post_type = post_type.find_element(By.XPATH, '//span[@data-id="post_type"]').text
    except:
        post_type = "Not Found"
    
    instructor_answer = ""
    try:
        instructor_answer = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, '//article[@data-id="i_answer"]')))
        instructor_answer = instructor_answer.find_element(By.CSS_SELECTOR, '.render-html-content.overflow-hidden.latex_process').text
    except:
        instructor_answer = "Not Found"

    file_data = {
        "author": author,
        "position": "student",
        "course": "CPSC 110 2021WT2",
        "post_num": post,
        "link": uri,
        "title": title,
        "question": question,
        "student_answer": student_answer,
        "instructor_answer": instructor_answer
    }

    return file_data

for i in range(100, 1100):
    data = queryFun(i)
    if data == "not here":
        continue

    try:
        with open(f"data/file{i}.json", "w") as json_file:
            json.dump(data, json_file, indent=4)
        print("Data written to product.json successfully!")
    except IOError as e:
        print(f"Error writing to file: {e}")

driver.quit()
