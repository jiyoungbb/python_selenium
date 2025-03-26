from selenium import webdriver

driver = webdriver.Chrome()  # 크롬 브라우저 실행
driver.get("https://www.google.com")  # 구글 열기

# driver.close()  # 현재 활성화된 탭(윈도우)만 닫음
driver.quit()  # 브라우저 전체 종료