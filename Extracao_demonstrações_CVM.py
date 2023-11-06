from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import pyautogui as pg


#criando o navegador

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)


#Acessando o site da CVM

navegador.get(r"https://cvmweb.cvm.gov.br/SWB/Sistemas/SCW/CPublica/CiaAb/FormBuscaCiaAb.aspx?TipoConsult=c")

# Pesquisando

navegador.find_element(By.ID,"txtCNPJNome").send_keys("guararapes")
navegador.find_element(By.ID,"btnContinuar").click()
navegador.find_element(By.ID,"dlCiasCdCVM__ctl2_Linkbutton4").click()
time.sleep(8)
navegador.find_element(By.ID,"filtrosPesquisa").click()
time.sleep(1)
navegador.find_element(By.XPATH,'//*[@id="divPeriodo"]/div[1]/div[3]/label').click()
navegador.find_element(By.ID,"txtDataIni").send_keys('01/01/2023')
navegador.find_element(By.ID,"txtDataFim").send_keys("31/12/2023")
time.sleep(1)
navegador.find_element(By.XPATH,'//*[@id="cboCategorias_chosen"]/a/span').click()
time.sleep(1)
pg.press('d')
time.sleep(1)
pg.press('f')
time.sleep(1)
pg.press('p')
time.sleep(1)
pg.press('enter')
time.sleep(1)
navegador.find_element(By.ID,"btnConsulta").click()
time.sleep(1)
navegador.find_element(By.CSS_SELECTOR,'i.fi-download').click()
