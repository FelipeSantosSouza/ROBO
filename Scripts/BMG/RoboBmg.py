from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from pyvirtualdisplay import Display
from  Investimento import Investimento as inv
import json
dominio = "https://www.bmginvestdigital.com.br/Home/investimentos"

def start():
    print("Iniciando display virtual")
    display = Display(visible=0, size=(1024, 768))
    display.start()
    opt = Options()
    opt.headless = True
    driver = webdriver.Firefox(options=opt, executable_path=r'/opt/geckodriver')
    print("Capturando o dominio: " + dominio)
    driver.implicitly_wait(30)
    driver.get(dominio)
    driver.find_element(By.XPATH,"//span[contains(.,'Mostrar todos os CDB BMG DI')]").click()
    driver.find_element(By.XPATH,"//span[contains(.,'Mostrar todos os CDB BMG IPCA +')]").click()
    driver.find_element(By.XPATH,"//span[contains(.,'Mostrar todos os CDB BMG PRÉ')]").click()
    elemento = driver.find_element(By.CLASS_NAME, "product")
    print(elemento)
    lista = gerarInvestimentoEsp(elemento)
    print("Fechando o driver ...")
    driver.quit()
    print("Parando o display ...")
    display.stop()
    toJson(lista)

def validacao(elemento):
    if ('\n' in elemento):
        elemento = elemento.replace("\n", "")
    return elemento

def gerarInvestimentoEsp(elemento):
    listaInv = []
    print("Percorrendo o dominio ...")
    elementos = elemento.find_elements(By.CLASS_NAME, "product__details__list")
    for e in elementos:
        try:
            texto = e.text
            prazo = texto[texto.index("Prazo:")+len("Prazo:"):texto.index("Taxa*:")-1]
            rentabilidade = texto[texto.index("*:")+len("*:"):texto.index("%")+1]
            valorMin = texto[texto.index("R$")+len("R$"):texto.index("Li")-1]
            print("Elemento capturado - " + "Valor Minimo: " +valorMin + " - " + "Rentabilidade: " + rentabilidade + " - " + "Prazo: " + prazo)
            ir = texto[texto.index("IR:")+len("IR:"):texto.index("Apl")-1]
            liquidez = "Dado Indisponível"
            tipo = "CDB"
            investimento = inv(validacao(str(prazo)), validacao(str(dominio)), validacao(str(rentabilidade)), validacao(str(valorMin).strip()), 
            validacao(str(ir)), validacao(str(liquidez)), validacao(str(tipo)))
            listaInv.append(investimento)
        except:
           print("Erro na capura do elemento: " + str(e))
    return listaInv

def toJson(lista):
    print("Iniciando salvamento do json...")
    conteudo = []
    for linha in lista:
        conteudo.append({"dominio":linha.dominio, "prazo":linha.prazo, "rentabilidade":linha.rentabilidade, "valorMim":linha.valorMin, "ir":linha.ir, "liquidez":linha.liquidez, "tipo":linha.tipo})
    with open('jsonBmg.json', 'w', encoding="utf8") as outfile:
        json.dump(conteudo, outfile, default="serialize")
    print("Json salvo!")


start()
