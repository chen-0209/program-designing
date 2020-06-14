#!/usr/bin/env python
# coding: utf-8

# In[9]:


from selenium import webdriver
import time
import re

def is_number(num):
    pattern = re.compile(r'^[-+]?[-0-9]\d*\.\d*|[-+]?\.?[0-9]\d*$')
    result = pattern.match(num)
    if result:
        return True
    else:
        return False


def not_empty(s):
    return s and s.strip()


def get_results(url):
    option = webdriver.ChromeOptions()
    option.add_argument("headless")
    driver = webdriver.Chrome("/Users/yu/chromedriver")
    results = []
    results_dict = {}
    driver.get(url)
    time.sleep(3)   
    elements = driver.find_elements_by_class_name("section-result")
    for element in elements:
        d = re.split("\n|·",element.text)
        results.append(d)

    while True:
        try:
            python_button = driver.find_element_by_xpath("//button[@aria-label='下一頁']")
            python_button.click()
            time.sleep(3)
            elements = driver.find_elements_by_class_name("section-result")

            for element in elements:
                d = re.split("\n|·",element.text)
                results.append(d)

        except:
            driver.close()
            names_list = []
            results_len = len(results)
            for result in results:
                names_list.append(result[0])
                del result[0]

            features_list = [{} for i in range(results_len)]
            for i in range(results_len):
                if is_number(results[i][0][:3]):
                    features_list[i]["star"] = results[i][0]
                    del results[i][0]
                else:
                    features_list[i]["star"] = None

            for i in range(results_len):
                if re.match(r"\$+",results[i][0]):
                    features_list[i]["price"] = results[i][0]
                    del results[i][0]
                else:
                    features_list[i]["price"] = None
            
            for i in range(results_len):
                features_list[i]["catagory"] = results[i][0]
                del results[i][0]
                
            for i in range(results_len):
                fliter_result = list(filter(not_empty,results[i]))
                features_list[i]["others"] = fliter_result
                
            return dict(zip(names_list,features_list))            


locs = ["公館餐廳", "溫州街餐廳", "118餐廳", "六張犁餐廳", "台大學生餐廳"]
main_url = "https://www.google.com.tw/maps/search"
for loc in locs:
    url = ("/").join([main_url,loc])
    k = get_results(url)
    f = open("/Users/yu/Downloads/" + loc + ".txt", "w+")
    f.write(str(k))
    f.close()

