from selenium import webdriver

# 크롬 옵션 설정 (M1 맥북에서 필요할 수도 있음)
options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# 크롬 드라이버 실행
driver = webdriver.Chrome(options=options)
driver.get("https://www.google.com")

print("구글 페이지 열림!")
driver.quit()
