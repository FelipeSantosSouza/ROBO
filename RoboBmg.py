from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
dominio = "https://www.bmginvestdigital.com.br/Home/investimentos"

def capturarConterudoEsp():
    driver = webdriver.PhantomJS()
    driver.get(dominio)
    elemento = driver.find_element(By.CLASS_NAME, "product")
    gerarInvestimentoEsp(elemento)
    driver.quit()

def gerarInvestimentoEsp(elemento):
    elementos = elemento.find_elements(By.CLASS_NAME, "product__details__list")
    for e in elementos:
        try:
            texto = e.text
            print("-----")
            prazo = texto[texto.index("Prazo:")+len("Prazo:"):texto.index("Taxa*:")-1]
            print(prazo)
        except:
            print("Investimento Nulo!")

capturarConterudoEsp()
