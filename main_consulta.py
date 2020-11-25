from classes.regrasexternodiscador import RegrasDiscador
from classes.regrasexternolocal import RegrasLocal

discador = RegrasDiscador()

local = RegrasLocal()

tabulacoes = discador.coleta_dados()

print(tabulacoes.shape)

discador.desconectar()
local.desconectar()

