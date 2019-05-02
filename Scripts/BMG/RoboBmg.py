from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from pyvirtualdisplay import Display
from  Investimento import Investimento as inv

dominio = "https://www.bmginvestdigital.com.br/Home/investimentos"

def capturarConterudoEsp():
    display = Display(visible=0, size=(1024, 768))
    display.start()
    opt = Options()
    opt.headless = True
    driver = webdriver.Firefox(options=opt, executable_path=r'/opt/geckodriver')
    driver.get(dominio)
    elemento = driver.find_element(By.CLASS_NAME, "product")
    gerarInvestimentoEsp(elemento)
    driver.quit()
    display.stop()

def gerarInvestimentoEsp(elemento):
    listaInv = []
    elementos = elemento.find_elements(By.CLASS_NAME, "product__details__list")
    for e in elementos:
        try:
            texto = e.text
            prazo = texto[texto.index("Prazo:")+len("Prazo:"):texto.index("Taxa*:")-1]
            rentabilidade = texto[texto.index("*:")+len("*:"):texto.index("%")-1]
            aplicacao_min = texto[texto.index("R$")+len("R$"):texto.index("Li")-1]
            ir = texto[texto.index("IR:")+len("IR:"):texto.index("Apl")-1]
            liquidez = -1
            tipo = "CDB"
            investimento = inv(prazo, dominio, rentabilidade, aplicacao_min, ir, liquidez, tipo)
            listaInv.append(investimento)
        except:
            print("Investimento Nulo!")
    for linha in listaInv:
        print(linha)

capturarConterudoEsp()
