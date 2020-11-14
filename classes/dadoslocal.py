import os

import sqlite3

class Local:

    def __init__(self):
        self.sqliteConnection = sqlite3.connect(os.getcwd() + '\\bd\\configs.db')
        self.cursor = self.sqliteConnection.cursor()


    def __del__(self):
        self. desconectar()


    def conectar(self):
        return self.sqlc.cursor()


    def desconectar(self):
        self.cursor.close()


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


    def get_dados(self, nomesistema, tipodados, allorone = None):
        select = "select * from informacoes_aplicativos where NomeSistema = '" + nomesistema + "' and TipoDados = '" + tipodados + "' and status = '1'"
        self.cursor.execute(select)
        if allorone == 'one':
            return self.__fetch_in_dict(self.cursor, 'one')
        elif allorone == 'all':
            return self.__fetch_in_dict(self.cursor, 'all')
        else:
            raise Exception('Favor especificar um tipo')


    def get_nome_robo(self):
        select = "select * from main"
        self.cursor.execute(select)
        return self.__fetch_in_dict(self.cursor, 'one')
