#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 21:46:53 2022

@author: christinaxu
"""
from bs4 import BeautifulSoup as bs
import numpy as np
import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import html.parser
import time
from time import sleep
import re
import os

# Iterating through pages 
titles = []
hrefs = []
links = []
comments = []
downloads = []

def enable_download_headless(browser,download_dir):
    browser.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
    params = {'cmd':'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': download_dir}}
    browser.execute("send_command", params)
     
pages = np.arange(1,2,1)

for page in pages:
    options = webdriver.ChromeOptions()
    browser = webdriver.Chrome('/Users/christinaxu/Documents/pm_salary_proj/chromedriver', options=options)
    page = 'https://www.regulations.gov/docket/USBC-2018-0009/comments?pageNumber=' + str(page)
    browser.get(page)
    time.sleep(5)
    
    soup = bs(browser.page_source, 'html.parser')
    #print(soup)
    
    a_s = soup.find_all('a', attrs={'href': re.compile("/comment/")})
    
    for a in a_s:
        # print(a)
        titles.append(a.text) # comment titles
        hrefs.append(a['href']) # comment links
        base_url = 'https://www.regulations.gov'
        for href in hrefs:
            link = base_url + href
            if link not in links:
                links.append(link)
        
    for url in links:
        browser.get(url)
        time.sleep(5)
        
        soup1 = bs(browser.page_source, 'html.parser')
        
        comment = soup1.find('div', class_= "px-2").text
        comments.append(comment)
        
        prefs = {'download.default_directory':'/Users/christinaxu/Documents/us-census-bureau-evolution-of-privacy-loss'}
        options.add_experimental_option("prefs",prefs)
    
        download_dir = '/Users/christinaxu/Documents/us-census-bureau-evolution-of-privacy-loss/comment-pdfs'
        
        enable_download_headless(browser, download_dir)
        
        try:
            classes = browser.find_element_by_xpath('//*[@class="ember-view"]/div/a/span')
            classes.click()
            
        except NoSuchElementException:
            pass
       
       
        
    

        
        
    
        
               

        
        


    
    





   


    





