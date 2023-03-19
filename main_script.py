from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import csv

m_main_data=[]
main_data=[]
main_name_l=[]
second_name_l=[]
no_of_beds_l=[]
date_l=[]
price_l=[]
Service_fee_l=[]
total_bef_taxes_l=[]
amenities_l=[]
clealiness_l=[]
communication_l=[]
location_l=[]
check_in_l=[]
accuracy_l=[]
links=[]
chrome_options =webdriver.ChromeOptions()
s=Service(ChromeDriverManager().install())
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=s,options=chrome_options)
wait=WebDriverWait(driver, 60)
url="https://www.airbnb.com/s/uganda/homes"
driver.get(url)

main_name= wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@class='t1jojoys dir dir-ltr']")))
main_name=driver.find_elements(By.XPATH,"//div[@class='t1jojoys dir dir-ltr']")

ff=0
while (ff<len(main_name)):
    element=wait.until(EC.element_to_be_clickable((By.XPATH,f"//div[@class='c4mnd7m dir dir-ltr']//a[@class='rfexzly dir dir-ltr'][1]")))
    link=driver.find_elements(By.XPATH,f"//div[@class='c4mnd7m dir dir-ltr']//a[@class='rfexzly dir dir-ltr'][1]")
    # time.sleep(2)
    link=link[ff].get_attribute('href')
    links.append(link)
    ff+=1

print("LEngth")
print(len(main_name))

i=0

while(i<len(main_name)):
    # driver.get(url)

    main_name= wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@class='t1jojoys dir dir-ltr']")))
    main_name=driver.find_elements(By.XPATH,"//div[@class='t1jojoys dir dir-ltr']")[i].text
    main_name_l.append(main_name)

    second_name= wait.until(EC.element_to_be_clickable((By.XPATH,"//span[@class='t6mzqp7 dir dir-ltr']")))
    second_name=driver.find_elements(By.XPATH,"//span[@class='t6mzqp7 dir dir-ltr']")[i].text
    second_name_l.append(second_name)

    no_of_beds=driver.find_elements(By.XPATH,"//div[@class='f15liw5s s1cjsi4j dir dir-ltr']//span[contains(text(),'bed')]")[i].text
    no_of_beds_l.append(no_of_beds)
    date=driver.find_elements(By.XPATH,"//div[@class='f15liw5s s1cjsi4j dir dir-ltr']//span[contains(text(),'–')]")[i].text
    date_l.append(date)

    price= wait.until(EC.element_to_be_clickable((By.XPATH,"//span[@class='a8jt5op dir dir-ltr']")))
    price=driver.find_elements(By.XPATH,"//span[@class='a8jt5op dir dir-ltr']")[11+i].text
    price_l.append(price)
    i+=1

h=0
print(links)
i=0
while(h<len(links)):
        # print(i)
        print("no of home")
        print(i+1)
        driver.get(links[h])
        # time.sleep(100)
        time.sleep(2)
        try:
            service_fee=wait.until(EC.element_to_be_clickable((By.XPATH,"//span[@class='_1k4xcdh']")))
            service_fee=driver.find_elements(By.XPATH,"//span[@class='_1k4xcdh']")[1].text
            Service_fee_l.append(service_fee)
            # print("SERVice fee :-")
            # print(service_fee)
        except:
          Service_fee_l.append("-")
        try:
            total_bef_taxes=driver.find_elements(By.XPATH,"//span[@class='_1k4xcdh']")[2].text
            total_bef_taxes_l.append(total_bef_taxes)
        except:
            total_bef_taxes_l.append("-")
        
        # wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@class='_gw4xx4']")))
        wait.until(EC.element_to_be_clickable((By.XPATH,"//button[contains(@class,'b65jmrv v7aged4')]")))        
        amenties=driver.find_elements(By.XPATH,"//button[contains(@class,'b65jmrv v7aged4')]")[0]
        driver.execute_script("arguments[0].click();", amenties)

        wmenities=wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@class='_gw4xx4']")))
        amenities=driver.find_elements(By.XPATH,"//div[@class='_gw4xx4']")
        # print("Amenties:-")
        # print(amenities)
        # time.sleep(100)
        amenities_l_l=[]
        for amen in amenities:
            amenities_l_l.append(amen.text)
        amenities_l.append(amenities_l_l)
        # //span[@class='i1h5tsj6 dir dir-ltr']
        time.sleep(2)
        driver.find_elements(By.XPATH,"//span[@class='i1h5tsj6 dir dir-ltr']")[-1].click()
        try:
            clealiness=wait.until(EC.element_to_be_clickable((By.XPATH,"//span[@class='_4oybiu']")))
            clealiness=driver.find_elements(By.XPATH,"//span[@class='_4oybiu']")[0].text
            # print(clealiness)
        
            accuracy=driver.find_elements(By.XPATH,"//span[@class='_4oybiu']")[1].text
            communication=driver.find_elements(By.XPATH,"//span[@class='_4oybiu']")[2].text
            location=driver.find_elements(By.XPATH,"//span[@class='_4oybiu']")[3].text
            check_in=driver.find_elements(By.XPATH,"//span[@class='_4oybiu']")[4].text
            clealiness_l.append(clealiness)
            accuracy_l.append(accuracy)
            check_in_l.append(check_in)
            location_l.append(location)
            communication_l.append(communication)
        except:
            clealiness_l.append("-")
            accuracy_l.append("-")
            check_in_l.append("-")
            location_l.append("-")
            communication_l.append("-")
        h+=1
        i+=1
# zipped_lists = zip
# (main_name_l,
#  second_name_l,
#  date_l,
# no_of_beds_l,

# price_l,
# Service_fee_l,
# total_bef_taxes_l,
# amenities_l,
# clealiness_l,
# communication_l,
# accuracy_l,
# location_l,
# check_in_l,

# )
header = ['Main_name','Second Name','Date','No of Beds','Price','Service Fee','Total before taxes','Amenities','Cleanliness','Communication','Accuracy','Location','Check in']
with open('output.csv', 'w', newline='',encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)

    # Write the header row
    writer.writerow(header)

    # Write the data rows
    for i in range(len(main_name)):
        row_data = [main_name_l[i],second_name_l[i],
no_of_beds_l[i],
date_l[i],
price_l[i],
Service_fee_l[i],
total_bef_taxes_l[i],
amenities_l[i],
clealiness_l[i],
communication_l[i],
location_l[i],
check_in_l[i],
accuracy_l[i],
links[i]]
        writer.writerow(row_data)

