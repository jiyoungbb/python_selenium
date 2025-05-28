from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Chrome 옵션 설정
options = Options()
options.add_argument("--start-maximized")  # 최대화된 창으로 시작 (선택)

# ChromeDriver 경로 지정
service = Service("/Users/jiyoung/.cache/selenium/chromedriver/mac-arm64/134.0.6998.90/chromedriver")  # 경로 수정

# Chrome WebDriver 실행
driver = webdriver.Chrome(options=options)

# 크롬 브라우저 열기
driver.get("https://www.google.com")

# 사용자 입력을 기다림
input("브라우저를 종료하려면 엔터를 누르세요...")

# 이제 브라우저 종료 (원하는 경우만 추가)ㅇ
driver.quit()