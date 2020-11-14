class Dados_Mensagem:
    
    def erro_conexao_bancodedados(nomerobo, ipservidor):
        return {"Mensagem": "Prezados,\n\n" + 
                    "Ocorreu um erro ao conectar na base de dados " +
                    ipservidor +
                    ".\n\n" +
                    "Att.\n" +
                    "Favor não responder essa mensagem pois é enviada automaticamente!",
                "Titulo": "Erro ao conectar na base - " + nomerobo}

    def erro_senha_invalida(nomerobo):
        return {"Mensagem": "Prezados,\n\n" +
                    "A senha usada no robo subject-0001 não esta mais funcionando, favor verificar." +
                    "\n\nAtt.\n\n" +
                    "Favor não responder essa mensagem pois é enviada automaticamente!",
                "Titulo": "Senha invalida robo - " + nomerobo}

    def erro_logar_conexao(nomerobo):
        return {"Mensagem": "Prezados,\n\n" + 
            "Não foi possivel logar no sistema Net SMS, houve erro de conexão.\n\n" +
            "Att.\n\n\n" + 
            "Favor não responder essa mensagem pois é enviada automaticamente!", 
            "Titulo": "Erro: Problema para conectar no NetSMS - " + nomerobo}

    def erro_arquivo():
        return {"Mensagem": "Prezados,\n\nO arquivo \"novosigma.exe\" foi movido, realizado copia para ambiente de produção\n\nAtt.\n\n\nFavor não responder essa mensagem pois é enviada automaticamente!", "Titulo": "Atenção: Arquivo do NET SMS movido"}

    def erro_desconhecido():
        return {"Mensagem": "Prezados,\n\nHouve um erro desconhecido na atualização, necessário realizar manualmente.\n\nAtt.\n\n\nFavor não responder essa mensagem pois é enviada automaticamente!", "Titulo": "Erro: Problema desconhecido na atualização NET SMS"}
    
    options = {"erro_conexao_bancodedados" : erro_conexao_bancodedados,
               "erro_senha_invalida" : erro_senha_invalida,
               "erro_logar_conexao" : erro_logar_conexao,
               "erro_arquivo" : erro_arquivo,
               "erro_desconhecido": erro_desconhecido,
    }


if __name__ == '__main__':
    dbp = Dados_Mensagem()
    print(dbp.options['erro_logar_conexao']('testemes'))