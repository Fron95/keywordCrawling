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

def checkGoogleSectionOrder(driver, CSSQuery, debug ) :                
    elements = driver.find_elements(By.CSS_SELECTOR, CSSQuery)        
    result = [element.get_attribute('href') for element in elements]
    rank = 1
    try :
        for href in result :
            if 'tistory' in href :            
                return rank
            else :
                rank += 1
        return rank
    except Exception as e :
        if debug : print('in Ranking TISTORY PRIMARY, error occuered',e)
        return "not Defined"
    