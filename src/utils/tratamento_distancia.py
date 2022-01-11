class TratamentoDistancia:

    def tratamento(self,texto):

        if texto == "ERRO":
            return "ERRO"

        texto_split = texto.split()
        try:
            saida = texto_split[0].replace(",", ".")
        except:
            saida = texto_split[0]

        return saida