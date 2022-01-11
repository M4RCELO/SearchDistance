import openpyxl

from src.utils.tratamento_distancia import TratamentoDistancia


class EscreverNoArquivo:

    arquivo = ''
    tratamento_distancia = None

    def __init__(self, arquivo):
        self.arquivo = arquivo
        self.tratamento_distancia = TratamentoDistancia()

    def escrever(self, coordenada, texto):
        xfile = openpyxl.load_workbook(self.arquivo)

        xfile["Planilha1"][coordenada] = self.tratamento_distancia.tratamento(texto)

        xfile.save(self.arquivo)