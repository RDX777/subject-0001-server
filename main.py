from classes.regrasexternodiscador import RegrasDiscador
from classes.regrasexternolocal import RegrasLocal

discador = RegrasDiscador()
dados = discador.coleta_dados()
discador.desconectar()

local = RegrasLocal()

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