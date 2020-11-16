import pandas

from classes.dadosexternoslocal import MariaDB

class RegrasLocal(MariaDB):

    def __init__(self):
        super().__init__()


    def __del__(self):
        super().__del__()


    def insere_vendas(self,
        sondagemid,
        nome,
        cpf,
        contrato,
        municipio,
        datacontrato,
        idticket):


        if nome is not None:
            nome = nome.strip().upper()

        try:
            if int(contrato) == 0:
                contrato = None
        except:
            contrato = None

        if municipio is not None:
            municipio = municipio.strip().upper()

        datacontrato = datacontrato.to_pydatetime()

        return self._insere_vendas(
            sondagemid,
            nome,
            cpf,
            contrato,
            municipio,
            datacontrato,
            idticket)

    
    def insere_tabulacao(self,
        tabulacaoid1,
        tabulacaodescricao1,
        tabulacaoid2,
        tabulacaodescricao2,
        tabulacaoid3,
        tabulacaodescricao3):

        if pandas.isnull(tabulacaoid3):
            tabulacaoid3 = None

        return self._insere_tabulacao(tabulacaoid1,
        tabulacaodescricao1,
        tabulacaoid2,
        tabulacaodescricao2,
        tabulacaoid3,
        tabulacaodescricao3)
