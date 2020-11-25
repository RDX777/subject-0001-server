import pandas

from classes.dadosexternosdiscador import MariaDBDiscador

class RegrasDiscador(MariaDBDiscador):

    def __init__(self):
        super().__init__()


    def __del__(self):
        super().__del__()


    def coleta_dados(self):
        dados_akiva = self._coleta_dados()
        if len(dados_akiva) != 0:
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
                        'GRUPO_DE_TABULACAO',
                        'TABULACAO_PRINCIPAL'
                    ]
            ]

            del objeto_pandas_completo

            try:
                return objeto_pandas_colunas[
                        (
                            objeto_pandas_colunas.TABULACAO_PRINCIPAL.str.contains('VENDA FINALIZADA NET', case=True, regex=False) |
                            objeto_pandas_colunas.TABULACAO_PRINCIPAL.str.contains('VENDA PENDENTE', case=True, regex=False) &
                            ~objeto_pandas_colunas.TABULACAO_PRINCIPAL.str.contains('VENDA CANCELADA', case=True, regex=False)
                        ) |
                        objeto_pandas_colunas.GRUPO_DE_TABULACAO.isin(['Agendamento _NETPF'])
                    ]
            except:
                return objeto_pandas_colunas[
                        objeto_pandas_colunas.TABULACAO_PRINCIPAL.str.contains('VENDA FINALIZADA NET', case=True, regex=False) |
                        objeto_pandas_colunas.TABULACAO_PRINCIPAL.str.contains('VENDA PENDENTE', case=True, regex=False) |
                        objeto_pandas_colunas.GRUPO_DE_TABULACAO.isin(['Auditor - Venda NETPF'])
                    ]
        else:
            return None


    def coleta_tabulacoes(self):
        objeto_pandas_completo = pandas.DataFrame(data=self._coleta_tabulacoes())

        return objeto_pandas_completo
