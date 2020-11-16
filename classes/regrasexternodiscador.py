import pandas

from classes.dadosexternosdiscador import MariaDBDiscador

class RegrasDiscador(MariaDBDiscador):

    def __init__(self):
        super().__init__()


    def __del__(self):
        super().__del__()


    def coleta_dados(self):
        objeto_pandas_completo = pandas.DataFrame(data=self._coleta_dados())

        objeto_pandas_colunas = objeto_pandas_completo[
                [
                    'SONDAGEM_ID',
                    'NOME_CLIENTE_PENDENTE',
                    'CPF_PENDENTE',
                    'CONTRATO_PENDENTE',
                    'MUNICIPIO_PENDENTE',
                    'DATA_INICIO_CONTATO',
                    'ID_TICKET',
                    'GRUPO_DE_TABULACAO'
                ]
        ]

        del objeto_pandas_completo

        return objeto_pandas_colunas[objeto_pandas_colunas.GRUPO_DE_TABULACAO.isin(['Auditor - Venda NETPF'])]


    def coleta_tabulacoes(self):
        objeto_pandas_completo = pandas.DataFrame(data=self._coleta_tabulacoes())

        return objeto_pandas_completo