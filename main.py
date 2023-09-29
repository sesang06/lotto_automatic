from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.chrome.options import Options

# 아이디
id = ""
# 비밀번호
password = ""
# 구매횟수 (5개까지 가능)
number = 1

chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
# WebDriver 객체 생성 (여기서는 Chrome을 사용)
driver = webdriver.Chrome(options=chrome_options)

# 웹 페이지 접속
driver.get("https://dhlottery.co.kr/user.do?method=login&returnUrl=")

try:
    # 아이디와 비밀번호 입력 필드가 나타날 때까지 대기
    username = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "userId")))
    password = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#article > div:nth-child(2) > div > form > div > div.inner > fieldset > div.form > input[type=password]:nth-child(2)")))

    username.send_keys(id)
    password.send_keys(password)
    # 로그인 버튼 클릭
    login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="article"]/div[2]/div/form/div/div[1]/fieldset/div[1]/a')))
    login_button.click()


    time.sleep(10)
    # 추가 작업...

    driver.get('https://ol.dhlottery.co.kr/olotto/game/game645.do')

    time.sleep(5)
    driver.execute_script('javascript:closepopupLayerAlert();')
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "num2")))
    element.click()

    # <select> 요소가 나타날 때까지 대기
    select_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "amoundApply")))

    # Select 객체 생성
    select = Select(select_element)

    # 1 옵션을 선택
    select.select_by_value(str(number))

    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "btnSelectNum")))
    element.click()

    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "btnBuy")))
    element.click()

    element = WebDriverWait(driver, 10).until((EC.presence_of_element_located((By.CSS_SELECTOR, "#popupLayerConfirm > div > div.btns > input:nth-child(1)"))))
    element.click()

finally:
    # 웹드라이버 종료
    driver.quit()
