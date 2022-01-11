from src.utils.constants import Constants

class VoltarParaPesquisa:
    driver = None

    def __init__(self, driver):
        self.driver = driver

    def voltar(self):
        self.driver.find_element_by_xpath(Constants.botao_voltar_para_pesquisa).click()