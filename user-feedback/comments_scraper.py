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
from random import randint
import html.parser
from time import sleep
import re
import os

# Test code
# browser = webdriver.Chrome('/Users/christinaxu/Documents/pm_salary_proj/chromedriver')
# request = browser.get(url)
# time.sleep(3)
# source = browser.page_source
# print(soup)

# h3s = soup.find_all('h3', class_='h4 card-title')
# print(h3s)
# h3 = soup.find('h3', class_='h4 card-title')
# title = h3.a.text
# print(title)

# for h3 in h3s:
#    title = h3.a.text
#    print(title)

# Iterating through pages 
def enable_download_headless(browser,download_dir):
    browser.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
    params = {'cmd':'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': download_dir}}
    browser.execute("send_command", params)

options = webdriver.ChromeOptions()  #Initializing the webdriver
prefs = {'download.default_directory':'/Users/christinaxu/Documents/us-census-bureau-evolution-of-privacy-loss'}
options.add_experimental_option("prefs",prefs)
browser = webdriver.Chrome('/Users/christinaxu/Documents/pm_salary_proj/chromedriver')
download_dir = '/Users/christinaxu/Documents/us-census-bureau-evolution-of-privacy-loss/comments_pdfs'

titles = []
hrefs = []
links = []
comments = []
downloads = []

pages = np.arange(1,2,1)

for page in pages:
    page = 'https://www.regulations.gov/docket/USBC-2018-0009/comments?pageNumber=' + str(page)
    print(page)
    browser.get(page)
    soup = bs(browser.page_source, 'html.parser')
    a_s = soup.find_all('a', attrs={'href': re.compile("/comment/")})
     
    enable_download_headless(browser, download_dir)
    browser.get(url)
    
    try:
        classes = browser.find_element_by_xpath('//*[@class = "ember-view"]/div/a/span')
        classes.click()
   
    except NoSuchElementException:
        print('no attachments')
    
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
        driver = webdriver.Chrome('/Users/christinaxu/Documents/pm_salary_proj/chromedriver')
        driver.get(url)
        sleep(randint(2,10))
        soup1 = bs(driver.page_source, 'html.parser')
        
        comment = soup1.find('div', class_= "px-2").text
        comments.append(comment)
    
        download = soup1.find('a', class_= 'btn btn-default btn-block')
        
        if download is not None:
           downloads.append(download['href'])
        else: 
            downloads.append('')
              
     
        
       
       
        
    

        
        
    
        
               

        
        


    
    





   


    





