from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
#from pyvirtualdisplay import Display
from  Investimento import Investimento as inv
import json
dominio = "https://www.bancopan.com.br/produtos/investimentos/"

def start():
    #display = Display(visible=0, size=(1024, 768))
    #display.start()
    opt = Options()
    opt.headless = True
    driver = webdriver.Firefox(options=opt, executable_path=r'C:/geckodriver')
    driver.get(dominio)
    elemento = driver.find_element(By.CLASS_NAME, "table-desktop")
    lista = gerarInvestimentoEsp(elemento)
    driver.quit()
    #display.stop()
    #toJson(lista)

def gerarInvestimentoEsp(elemento):
    listaInv = []
    elementos = elemento.find_elements(By.CLASS_NAME, "table-body__row-divider")
    for e in elementos:
        check = 0
        try:
            linha = e.find_elements(By.CLASS_NAME, "table-body__cell-data")
            for l in linha:
                
                print('-----')
                if(l.text in 'LCI') or (l.text in 'CDB'):
                    tipo = l.text
                    print(tipo)
                    check = 1
                elif(l.text not in '-') and (l.text not in '') and (check == 1):
                    rentabilidade = l.text
                    print(rentabilidade)
                    break
        except:
            print("Investimento Nulo!")
    return listaInv

def toJson(lista):
    conteudo = []
    for linha in lista:
        conteudo.append([{"dominio":linha.dominio, "prazo":linha.prazo, "rentabilidade":linha.rentabilidade, "aplicacao_min":linha.aplicacao_min, "ir":linha.ir, "liquidez":linha.liquidez, "tipo":linha.tipo}])
    with open('jsonBmg.json', 'w', encoding="utf8") as outfile:
        json.dump(conteudo, outfile, default="serialize")

start()
