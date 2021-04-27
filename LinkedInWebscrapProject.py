# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 10:53:39 2021

@author: soumy_000
"""


from selenium import webdriver as sw

driver_path="G:\practical\programs\Python\Selenium\Chrome drivers\chromedriver"

print("Enter your mail and password"+"\n")  # with space in between
email,password=map(str,input().split())
print(email)
print(password)

options = sw.ChromeOptions()
options.add_argument("--incognito")
options.add_argument("--headless")

caps = options.to_capabilities()



driv=sw.Chrome(executable_path=driver_path, desired_capabilities=caps)

rs=driv.get("https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")

driv.implicitly_wait(10)

mailbox=driv.find_element_by_xpath('//*[@id ="username"]')
mailbox.send_keys(email)

passWordBox = driv.find_element_by_xpath('//*[@id="password"]')
passWordBox.send_keys(password)

nextbutton=driv.find_element_by_xpath('//*[@id="organic-div"]/form/div[3]/button')
nextbutton.click()


notif= driv.find_elements_by_class_name('notification-badge__count ')

profileview= driv.find_elements_by_xpath('/html/body/div[7]/div[3]/div/div/div/div/div/div/div[1]/div[2]/div/ul/li[1]/div/a/div/div/div[2]/span')

postview= driv.find_elements_by_xpath('/html/body/div[7]/div[3]/div/div/div/div/div/div/div[1]/div[2]/div/ul/li[2]/div/a/div/div/div[2]/span')

for i in range(len(notif)):
    print("There are " + str(notif[i].get_attribute('innerHTML'))+" new notifications.")
    
for j in range(len(profileview)):
    print("There are " + str(profileview[j].get_attribute('innerHTML')).strip() + " profile views.")
        
for k in range(len(postview)):
    print("There are " + str(postview[k].get_attribute('innerHTML')).strip() + " post views.")    
     

driv.get("https://linkedin.com/m/logout")
driv.implicitly_wait(10)
driv.close()  