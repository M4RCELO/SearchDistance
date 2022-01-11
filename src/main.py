from src.procurar_distancia.procurar_distancia import ProcurarDistancia
from src.utils.constants import Constants

arquivo = Constants.arquivo
arquivo_driver = Constants.arquivo_driver
coluna = Constants.coluna_distancia
linha_inicial = int(input(Constants.mensagem_input))

procurar_distancia = ProcurarDistancia(arquivo, arquivo_driver, coluna, linha_inicial)
procurar_distancia.procurar()