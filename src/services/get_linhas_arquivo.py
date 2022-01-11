import pandas as pd

class GetLinhasArquivo:

    arquivo = ''

    def __init__(self,arquivo):
        self.arquivo = arquivo

    def get_linhas(self):

        linhas = []
        xl = pd.ExcelFile(self.arquivo)
        sheetnames = xl.sheet_names
        for sheet in sheetnames:
            df = xl.parse(sheet)
            qtd_linhas = df.shape[0]
            for i in range(0, qtd_linhas):
                atual = i + 2
                linhas.append(
                    {
                        'Linha': atual,
                        'CEP': str(df.loc[i, 'CEP']),
                        'Cidade': str(df.loc[i, 'CIDADE']),
                    }
                )

        return linhas