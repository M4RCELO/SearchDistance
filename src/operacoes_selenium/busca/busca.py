from src.utils.constants import Constants

import time

class Busca:
    driver = None
    coluna = ''

    def __init__(self, driver, coluna):
        self.driver = driver
        self.coluna = coluna

    def procurar(self, local_atual, escrever_no_arquivo, i):
        self.driver.find_element_by_xpath(Constants.input_local_atual).send_keys(local_atual)
        self.driver.find_element_by_xpath(Constants.input_destino).send_keys(Constants.ifpb)
        time.sleep(5)

        self.driver.find_element_by_xpath(Constants.botao_pesquisar).click()
        time.sleep(5)

        self.driver.find_element_by_xpath(Constants.elemento_primeiro_registro).click()
        time.sleep(3)

        distancia = self.driver.find_element_by_xpath(Constants.elemento_distancia).text
        escrever_no_arquivo.escrever(self.coluna + str(i), distancia)
        time.sleep(3)

        self.driver.find_element_by_xpath(Constants.botao_voltar_para_pesquisa).click()