import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Text File
Data = open("demo.txt","w")

#Data Scrap Proccess
driver = webdriver.Chrome('D:/Kapampangan Research Paper/chromedriver.exe') #Driver Directory
driver.get('insert website to data scrap') #Website

main = driver.find_element_by_class_name("entry-content") #Where to Find the Scrap 
print(main.text)
Data.write(main.text)


#Inputing The Data Scrap into Text File
Data.close()


##Converting Text Into Json
def write_json(data, filename="D:/Kapampangan Research Paper/data/additional.json"):
    with open(filename, "a+") as f:
        json.dump(data, f, indent=4)


with open("D:/Kapampangan Research Paper/data/kapampanganwords1.json") as json_file:
    data = json.load(json_file)
    temp = data["kapampanganWords"]
    
    with open("D:/Kapampangan Research Paper/demo.txt", "r") as f:
        words = f.read()
        words = words.replace(',','')
        words = words.replace('.','')
        words = words.replace('?','')
        words = words.replace('!','')
        words = words.replace('-','')
        words = words.replace('1','')
        words = words.replace('2','')
        words = words.replace('3','')
        words = words.replace('4','')
        words = words.replace('5','')
        words = words.replace('6','')
        words = words.replace('7','')
        words = words.replace('8','')
        words = words.replace('9','')
        words = words.replace('0','')
        words = words.replace(' ','\n')
        words = words.split('\n')


        while "" in words:
            words.remove("")
            
        
        for i in words:
            if i.isalpha()==False:
                continue
            y = {"token": i.lower()}
            temp.append(y)

driver.close()
write_json(data)
