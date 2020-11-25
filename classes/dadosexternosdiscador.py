import mariadb

from classes.dadoslocal import Local 


class MariaDBDiscador:

    def __init__(self):

        local = Local()
        self.NOME_ROBO = local.get_nome_robo()['NomeRobo']
    
        self.__login_bd = local.get_dados('bddiscador', 'login', 'one')['DadosSistema']
        self.__senha_bd = local.get_dados('bddiscador', 'senha', 'one')['DadosSistema']
        self.__endereco_bd = local.get_dados('bddiscador', 'endereco', 'one')['DadosSistema']
        self.__porta_bd = 3306
        self.__banco_bd = local.get_dados('bddiscador', 'base', 'one')['DadosSistema']
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


    def _coleta_dados(self):
        select = "CALL spr_alert_net_pf_v2(DATE_SUB(CURDATE(), INTERVAL 2 DAY));"
        self.__conexao.execute(select)
   
        return self.__conexao.fetchall()


    def _coleta_tabulacoes(self):
        select = "CALL spr_classificacao_backoffice_module10();"
        self.__conexao.execute(select)
        return self.__conexao.fetchall()
