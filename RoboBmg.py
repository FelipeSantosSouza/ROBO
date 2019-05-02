from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from pyvirtualdisplay import Display
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
