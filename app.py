# Bibliotecas 
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


# Abre o naveador e busca link do Site
browser = webdriver.Chrome()
browser.get('https://www.glassdoor.com.br/Avalia%C3%A7%C3%B5es/Inter-Avalia%C3%A7%C3%B5es-E2483031.htm')
browser.maximize_window()
sleep(15)

# Varredura das informações no site
while True:
    cargo = browser.find_elements(By.XPATH,"//span[@class='review-avatar_avatarLabel__P15ey']")
    depoi = browser.find_elements(By.XPATH,"//span[@data-test='review-text-CONS']")

    for cargo, depoi in zip(cargo, depoi):
        with open('relatos.csv','a',encoding='utf-8') as arquivo:
            arquivo.write(f'{cargo.text},{depoi.text}{os.linesep}')

    try:
        botao_proximo = browser.find_element(By.CLASS_NAME,"//a[@class='pagination_ListItemButton__se7rv']")
        ActionChains(browser).move_to_element(botao_proximo).click().perform()
        sleep(2)
    except:


        break


input('')