import pyodbc

from classes.dadoslocal import Local
from classes.mail import MandarEmails
from classes.mensagensemails import Dados_Mensagem

class MsSQL:

    def __init__(self):
        local = Local()
        self.NOME_ROBO = local.get_nome_robo()
        endereco = local.get_dados('bdplanejamento', 'endereco', 'one')
        base = local.get_dados('bdplanejamento', 'base', 'one')
        login = local.get_dados('bdplanejamento', 'login', 'one')
        senha = local.get_dados('bdplanejamento', 'senha', 'one')
        contador = 0
        while True:
            try:
                self.__cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + endereco[2] + ';DATABASE=' + base[2] + ';UID=' + login[2] + ';PWD=' + senha[2])
                self._c = self.__cnxn.cursor()
                break
            except:
                contador += 1
                if contador == 20:
                    mensagem = Dados_Mensagem()
                    m = mensagem.options['erro_conexao_bancodedados'](self.NOME_ROBO[0], endereco[2])
                    mails = MandarEmails()
                    mails.mandar_mensagem(m['Mensagem'], m['Titulo'])
                    raise Exception('Erro na conexão com o Banco de Dados')


    def __fetch_in_dict(self, cursor, allorone = None):
        columns = [column[0] for column in cursor.description]
        if allorone == 'all':
            results = []
            for row in cursor.fetchall():
                results.append(dict(zip(columns, row)))
            return results
        elif allorone == 'one':
            row = cursor.fetchone()
            return dict(zip(columns, row))
        elif allorone is None:
            raise Exception('Tipo não definido')


    def get_dados(self):
        d = self._c.execute("""
            SELECT
                NOME_CLIENTE_PENDENTE,
                CPF_PENDENTE,
                CONTRATO_PENDENTE,
                CONTRATO_ATENDIMENTO,
                MUNICIPIO_PENDENTE,
                UF_PENDENTE,
                DATA_INICIO_CONTATO,
                DATA_FIM_CONTATO

            FROM 
                [MS-CAM-SERDB01\MSSQLSERVER01].[NET_PF].DBO.[CUSTOM]

            WHERE 
                GRUPO_DE_TABULACAO = 'Auditor - Venda NETPF' AND
                DATA_INICIO_CONTATO BETWEEN
                    DATEADD(DAY, -3, CONCAT(CONVERT(VARCHAR(10),GETDATE(),23), ' 00:00:00.000')) AND
                    DATEADD(DAY, -3,CONCAT(CONVERT(VARCHAR(10),GETDATE(),23), ' 23:59:59.999'))

            ORDER BY
                DATA_INICIO_CONTATO 
                
            ASC""")
        return self.__fetch_in_dict(d, 'all')
