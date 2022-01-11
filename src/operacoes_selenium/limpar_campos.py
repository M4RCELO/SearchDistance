from selenium.webdriver.common.keys import Keys
from src.utils.constants import Constants

class LimparCampos:

    driver = None

    def __init__(self, driver):
        self.driver = driver

    def limpar(self):

        self.driver.find_element_by_xpath(Constants.input_local_atual).send_keys(Keys.CONTROL, 'a')
        self.driver.find_element_by_xpath(Constants.input_local_atual).send_keys(Keys.BACKSPACE)

        self.driver.find_element_by_xpath(Constants.input_destino).send_keys(Keys.CONTROL, 'a')
        self.driver.find_element_by_xpath(Constants.input_destino).send_keys(Keys.BACKSPACE)
