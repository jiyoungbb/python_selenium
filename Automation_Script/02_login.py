from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Chrome 옵션 설정 (백그라운드로 실행하려면 옵션 추가)
options = Options()
options.add_argument("--start-maximized")  # 최대화된 창으로 시작 (선택)

# ChromeDriver 경로 지정 (경로 수정 필요)
service = Service("/Users/jiyoung/.cache/selenium/chromedriver/mac-arm64/134.0.6998.90/chromedriver")

# Chrome WebDriver 실행
driver = webdriver.Chrome(service=service, options=options)

# 네이버 로그인 페이지 열기
driver.get('https://nid.naver.com/nidlogin.login')

# ID 입력 필드 찾기
id_input = driver.find_element(By.ID, 'id')
id_input.send_keys('jiiyoung0906')  # 여기에 네이버 아이디 입력

# 비밀번호 입력 필드 찾기
password_input = driver.find_element(By.ID, 'pw')
password_input.send_keys('pd4991jq!')  # 여기에 네이버 비밀번호 입력

# 로그인 버튼 클릭
login_button = driver.find_element(By.ID, 'log.login')
login_button.click()

# 로그인 성공 시 나타날 요소 확인 (예: 사용자 이름)
try:
    user_name = driver.find_element(By.CSS_SELECTOR, ".user_name_selector")  # 사용자 이름 요소
    print("로그인 성공!")
except:
    print("로그인 실패!")

# 사용자 입력을 기다림
input("브라우저를 종료하려면 엔터를 누르세요...")

# 이제 브라우저 종료 (원하는 경우만 추가)
driver.quit()