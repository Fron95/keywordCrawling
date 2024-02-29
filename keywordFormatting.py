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

def keywordFormatting(words, format, debug) :
    if type(words) == list :
        if len(words) > 0 :
            result = {}
            for word in words :
                result[word] = format.copy()        
            return result.copy()    
            
    else :
        return