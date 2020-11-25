from classes.regrasexternodiscador import RegrasDiscador
from classes.regrasexternolocal import RegrasLocal

discador = RegrasDiscador()

local = RegrasLocal()

tabulacoes = discador.coleta_tabulacoes()

for index, row in tabulacoes.iterrows():
    local.insere_tabulacao(row.ID_CLASSIFICACO_BKO_1,
        row.CLASSIFICACO_BKO_1,
        row.ID_CLASSIFICACO_BKO_2,
        row.CLASSIFICACO_BKO_2,
        row.ID_CLASSIFICACO_BKO_3,
        row.CLASSIFICACO_BKO_3)