from selenium import webdriver
import os, time
from src.utils.constants import Constants
from selenium.webdriver.firefox.options import Options

class ConfigurarDriver:

    driver = None

    def __init__(self, caminho_driver):
        self.driver = webdriver.Chrome(os.path.join(caminho_driver))

    def configuracao_inicial(self):
        options = Options()
        options.add_argument('--headless')
        self.driver.get("https://www.google.com.br/maps")
        time.sleep(7)
        self.driver.find_element_by_xpath(Constants.botao_rotas).click()
        time.sleep(2)
        self.driver.find_element_by_xpath(Constants.botao_carro).click()

