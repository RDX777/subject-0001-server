#Servidor subject-0001

import mariadb

from classes.dadoslocal import Local 


class MariaDB:

    def __init__(self):

        local = Local()
        self.NOME_ROBO = local.get_nome_robo()

        self.__login_bd = local.get_dados('bdlocal', 'login', 'one')['DadosSistema']
        self.__senha_bd = local.get_dados('bdlocal', 'senha', 'one')['DadosSistema']
        self.__endereco_bd = local.get_dados('bdlocal', 'endereco', 'one')['DadosSistema']
        self.__porta_bd = 3306
        self.__banco_bd = local.get_dados('bdlocal', 'base', 'one')['DadosSistema']

        self.__conexao_bd = self.__conectar(self.__login_bd, self.__senha_bd, self.__endereco_bd, self.__porta_bd, self.__banco_bd)

        self.__conexao = self._conectar_bd()

    
    def __del__(self):
        try:
            self.desconectar()
        except:
            print('Desconectado do banco de dados {}' . format(self.__endereco_bd))
    

    def __conectar(self, login_bd, senha_bd, endereco_bd, porta_bd, banco_bd):
        conn = mariadb.connect(
            user=login_bd,
            password=senha_bd,
            host=endereco_bd,
            port=porta_bd,
            database=banco_bd
            )
        conn.autocommit = True
        return conn


    def _conectar_bd(self):
        return self.__conexao_bd.cursor(dictionary=True)


    def desconectar(self):
        self.__conexao_bd.close()

    
    def _insere_vendas(self,
        sondagemid,
        nome,
        cpf,
        contrato,
        municipio,
        datacontrato,
        idticket):

        sp_procedure = """
            CALL sp_insere_vendas(
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?
            )
        """

        return self.__conexao.execute(sp_procedure,
                (
                    sondagemid,
                    nome,
                    cpf,
                    contrato,
                    municipio,
                    datacontrato,
                    idticket
                )
            )


    def limpa_erro_desconhecido(self):
        sp_procedure = "CALL sp_limpa_erro_desconhecido()"
        try:
            self.__conexao.execute(sp_procedure)
            return True
        except mariadb.Error as e:
            print(e)
            return False


    def _insere_tabulacao(self,
        tabulacaoid1,
        tabulacaodescricao1,
        tabulacaoid2,
        tabulacaodescricao2,
        tabulacaoid3,
        tabulacaodescricao3):

        sp_procedure = "CALL sp_insere_tabulacoes(?, ?, ?, ?, ?, ?)"

        self.__conexao.execute(sp_procedure,
                (
                    tabulacaoid1,
                    tabulacaodescricao1,
                    tabulacaoid2,
                    tabulacaodescricao2,
                    tabulacaoid3,
                    tabulacaodescricao3
                )
            )

        #return self.__conexao.fetchone()


