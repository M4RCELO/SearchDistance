from src.operacoes_arquivo.escrever_arquivo import EscreverNoArquivo
from src.operacoes_selenium.busca.busca import Busca
from src.operacoes_selenium.configurar_driver import ConfigurarDriver
from src.operacoes_selenium.limpar_campos import LimparCampos
from src.operacoes_selenium.voltar_pesquisa import VoltarParaPesquisa
from src.services.get_linhas_arquivo import GetLinhasArquivo

import time

class ProcurarDistancia:
    arquivo = ''
    coluna = ''
    linha_inicial = 0

    def __init__(self, arquivo, arquivo_driver, coluna, linha_inicial):
        self.arquivo = arquivo
        self.arquivo_driver = arquivo_driver
        self.coluna = coluna
        self.linha_inicial = linha_inicial

    def procurar(self):

        i = self.linha_inicial
        escrever_no_arquivo = EscreverNoArquivo(self.arquivo)

        get_linhas_arquivo = GetLinhasArquivo(self.arquivo)
        configurar_driver = ConfigurarDriver(self.arquivo_driver)
        limpar_campos = LimparCampos(configurar_driver.driver)
        voltar_pesquisa = VoltarParaPesquisa(configurar_driver.driver)

        busca = Busca(configurar_driver.driver, self.coluna)

        linhas_arquivo = get_linhas_arquivo.get_linhas()

        configurar_driver.configuracao_inicial()

        while (True):

            if i == len(linhas_arquivo) + 2:
                break

            cep = str(linhas_arquivo[i - 2]['CEP'])
            cidade = str(linhas_arquivo[i - 2]['Cidade'])
            time.sleep(2)

            limpar_campos.limpar()

            try:
                if cep == '-':
                    busca.procurar(cidade,escrever_no_arquivo,i)

                else:
                    busca.procurar(cep, escrever_no_arquivo, i)
            except:

                limpar_campos.limpar()

                try:
                    busca.procurar(cidade,escrever_no_arquivo,i)
                except:
                    escrever_no_arquivo.escrever(self.coluna + str(i), "ERRO")
                    voltar_pesquisa.voltar()

            i += 1

        configurar_driver.driver.quit()
