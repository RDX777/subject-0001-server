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

        self._conexao = self._conectar_bd(self.__login_bd, self.__senha_bd, self.__endereco_bd, self.__porta_bd, self.__banco_bd)


    def _conectar_bd(self, login_bd, senha_bd, endereco_bd, porta_bd, banco_bd):
        conn = mariadb.connect(
            user=login_bd,
            password=senha_bd,
            host=endereco_bd,
            port=porta_bd,
            database=banco_bd
            )
        conn.autocommit = True
        return conn.cursor(dictionary=True)

    
    def __del__(self):
        self._conexao.close()


    def _desconectar(self):
        self.__del__()

    
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

        return self._conexao.execute(sp_procedure,
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
            self._conexao.execute(sp_procedure)
            return True
        except mariadb.Error as e:
            print(e)
            return False
