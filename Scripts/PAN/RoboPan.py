from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from pyvirtualdisplay import Display
from  Investimento import Investimento as inv
import json
dominio = "https://www.bancopan.com.br/produtos/investimentos/"

def start():
    print("Iniciando display virtual")
    display = Display(visible=0, size=(1024, 768))
    display.start()
    opt = Options()
    opt.headless = True
    driver = webdriver.Firefox(options=opt, executable_path=r'/opt/geckodriver')
    print("Capturando o dominio: " + dominio)
    driver.implicitly_wait(15)
    driver.get(dominio)
    elemento = driver.find_element(By.CLASS_NAME, "table-desktop")
    lista = gerarInvestimentoEsp(elemento)
    print("Fechando o driver ...")
    driver.quit()
    print("Parando o display ...")
    display.stop()
    toJson(lista)

def gerarInvestimentoEsp(elemento):
    listaInv = []
    print("Percorrendo o dominio ...")
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
                    valorMin = 100
                    ir ="Dado Indisponivel"
                    investimento = inv('Indefinido', dominio, rentabilidade, valorMin, ir, "Dado Indisponivel", tipo)
                    print("Elemento capturado - " + "Valor Minimo: " +valorMin + " - " + "Rentabilidade: " + rentabilidade)
                    listaInv.append(investimento)
                    break
        except Exception as ex:
            print(e)
            print("Erro na capura: " + str(e))
    return listaInv

def toJson(lista):
    print("Iniciando salvamento do json...")
    conteudo = []
    for linha in lista:
        conteudo.append({"dominio":linha.dominio, "prazo":linha.prazo, "rentabilidade":linha.rentabilidade, "valorMim":linha.valorMin, "ir":linha.ir, "liquidez":linha.liquidez, "tipo":linha.tipo})
    with open('jsonPan.json', 'w', encoding="utf8") as outfile:
        json.dump(conteudo, outfile, default="serialize")
    print("Json salvo!")
start()
