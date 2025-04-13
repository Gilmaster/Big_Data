# Bibliotecas 
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import os
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Abre o naveador e busca link do Site
browser = webdriver.Chrome()
browser.get('https://www.glassdoor.com.br/index.htm')
browser.maximize_window()
#variavel que gera tempo de espera dinamica
espera = WebDriverWait(browser,15)
#insere das no forme pa login e preciona o botão de login
browser.find_element(By.XPATH,"//input[@type='email']").send_keys("gabrielgb.user@gmail.com")
espera.until(EC.element_to_be_selected)
email = browser.find_element(By.XPATH,"//button[@data-test='email-form-button']")
email.click()
sleep(15)

#insere a senha no formulario e efetua o login
senha = browser.find_element(By.XPATH,"//input[@id='inlineUserPassword']").send_keys("ga91929394")
espera.until(EC.element_to_be_clickable)
login = browser.find_element(By.XPATH,"//button[@class='Button Button']")
login.click()
espera.until(EC.frame_to_be_available_and_switch_to_it)

#inicia uma nova aba e fixa as ações nela
browser.execute_script("window.open('https://www.glassdoor.com.br/Avalia%C3%A7%C3%B5es/Inter-Avalia%C3%A7%C3%B5es-E2483031.htm', '_blank');")
browser.switch_to.window(browser.window_handles[1])
espera.until(EC.frame_to_be_available_and_switch_to_it)

#Varredura das informações no site
while True: 
    try:
        #Guarda as informações desejadas
        cargo = browser.find_elements(By.XPATH,"//span[@class='review-avatar_avatarLabel__P15ey']")
        depoi = browser.find_elements(By.XPATH,"//span[@data-test='review-text-CONS']")

        #Gera a lista com as informações
        for cargo, depoi in zip(cargo, depoi):
            with open('relatos.csv','a',encoding='utf-8') as arquivo:
                arquivo.write(f'{cargo.text};{depoi.text}{os.linesep}')
     
    except:
        #Muda dinamicamnete as paginas
        botao_next = browser.find_element(By.XPATH, "//button[@data-test='next-page']")
        espera.until(EC.element_to_be_clickable)
        botao_next.click()
        print("Última página alcançada!")

        break

input('')