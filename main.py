from classes.regrasexternodiscador import RegrasDiscador
from classes.regrasexternolocal import RegrasLocal

discador = RegrasDiscador()
dados = discador.coleta_dados()

local = RegrasLocal()
if dados is not None:
    for index, row in dados.iterrows():

        local.insere_vendas(row.SONDAGEM_ID,
            row.NOME_CLIENTE_PENDENTE,
            row.CPF_PENDENTE,
            row.CONTRATO_PENDENTE,
            row.MUNICIPIO_PENDENTE,
            row.DATA_INICIO_CONTATO,
            row.ID_TICKET
        )

local.limpa_erro_desconhecido()
local.limpa_pendente()

tabulacoes = discador.coleta_tabulacoes()

for index, row in tabulacoes.iterrows():
    local.insere_tabulacao(row.ID_CLASSIFICACO_BKO_1,
        row.CLASSIFICACO_BKO_1,
        row.ID_CLASSIFICACO_BKO_2,
        row.CLASSIFICACO_BKO_2,
        row.ID_CLASSIFICACO_BKO_3,
        row.CLASSIFICACO_BKO_3)

discador.desconectar()
