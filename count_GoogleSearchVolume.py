# 임포트
import pandas as pd
import numpy as np
import langchain 
import requests
from bs4 import BeautifulSoup

# 서제스트 키워드 긁어오기
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def countGoogleSearchVolume(driver, CSSQuery, debug) :        
# 웹 드라이버 초기화 (Chrome 사용을 가정)
    elements = driver.find_elements(By.CSS_SELECTOR, CSSQuery)
    result = [element.text for element in elements]    
    # 필요한 글자처리
    if len(result) > 0 :
        result = result[0] # 값 추출
        result = result.split(' ')[2]
        result = int(result.replace('개', '').replace(',',''))
        return result
    else :
        return 'NODATA'


