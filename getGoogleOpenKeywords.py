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

def getGoogleOpenKeywords(driver, word, CSSQuery, debug) :
    elements = driver.find_elements(By.CSS_SELECTOR, CSSQuery)
    result = [element.get_attribute('innerHTML').replace('<b>', "").replace("</b>","") for element in elements]
    

    return result