# 서제스트 키워드 긁어오기
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
## 로직정의 및 실행
def seleniumClickAndCrawling(driver, clickElementCSSQuery, dataCSSQuery, debug) :
    # 2. 검색창 클릭
    search_box = driver.find_element(By.CSS_SELECTOR, clickElementCSSQuery)
    search_box.click()
    if debug : print('click okay')

    # 잠시 대기 (동적 콘텐츠 로딩을 위함)
    time.sleep(2)

    # 3. "아메리카노" 텍스트가 포함된 태그들 선택 및 텍스트 수집
    elements = driver.find_elements(By.CSS_SELECTOR, dataCSSQuery)

    if clickElementCSSQuery == '#searchform textarea.gLFyf' : # 구글특수처리
        result = [element.get_attribute('innerHTML').replace('<b>', "").replace("</b>","") for element in elements]
        
    else :
        result = [element.text for element in elements]
    
    if debug : print('getted suggest keywords', len(result))

    return result