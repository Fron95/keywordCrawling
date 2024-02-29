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

def countDaumADs(url, word, tags, debug) :
    response = requests.get(url) # 페이지 가져오기
    soup = BeautifulSoup(response.text, 'html.parser') # BeautifulSoup 객체 생성

    num_advertisement = 0
    for tag in tags :        
        contents = soup.select(tag)     # 광고섹션
        contentsLength = len(contents)     # 광고섹션갯수
        for i in range(contentsLength) :
            num_advertisement += len(contents[i].find_all(recursive=False))     # 광고갯수합산
    #디버그용 if debug : print(word,'광고갯수 : ',num_advertisement)
    return num_advertisement