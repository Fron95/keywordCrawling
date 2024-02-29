# 임포트
import pandas as pd
import numpy as np
import langchain 
import requests  # 이 부분을 추가해주세요
from bs4 import BeautifulSoup

# 서제스트 키워드 긁어오기
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def getOpenKeywords(url, tag, debug) :
    # 웹페이지 가져오기
    response = requests.get(url)
    # BeautifulSoup 객체 생성
    soup = BeautifulSoup(response.text, 'html.parser')
  
    words = soup.select(tag)
    wordsLength = len(words)
    if debug : print('from', url)
    if debug : print('getted openKeywords length', wordsLength)
    
    if(wordsLength > 0) :
        result = [word.text for word in words]
        return result
