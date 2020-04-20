import sqlite3
import backend.client as clt

class DataBase:

    '''
    La clase DataBase contiene todas las propiedades de una base de datos,
    tambien contiene un patron de diseño singleton para que solo se pueda instanciar
    una vez
    Args:
        database_name (str): Nombre del archivo que queremos abrir
    
    Attributes:
        db (str): Nombre del archivo .db
        route (str): Ruta del archivo .db
        conn (Conenction): Objeto Connection del modulo sqlite3 para realizar la conexion a la db
        cursor (Cursor): Objeto Cursor que permite realizar consultas a la db
        python_to_sql (dict): Diccionario que transforma tipos de datos de python a sqlite
    
    '''

    # Constructor
    class Instance:
        def __init__(self, database_name):
            self._db = database_name
            self._route = 'backend/db/'
            self._conn = sqlite3.connect(self._route + self._db, check_same_thread=False)
            self._cursor = self._conn.cursor()
            self._python_to_sql = {
                'str':'TEXT',
                'int':'INTEGER'
            }
            self._tables = {}

        # Getters 
        @property
        def conn(self):
            return self._conn

        @property
        def cursor(self):
            return self._cursor

        @property
        def db_name(self):
            return "Restringido"

        def get_tables(self):
            self.cursor.execute('SELECT name from sqlite_master where type="table"')
            tables = self.cursor.fetchall()
            
            for i in tables:
                print(i[0])
        
        def create_table(self, table, param, ext):
            '''
            Metodo para crear una tabla en la base de datos

            Args:
                table (str): Nombre de la tabla que se quiere crear
                param (list): Lista que contiene los datos para crear la tabla
            '''
            table_string = (f'CREATE TABLE {table} (')
            for i in range(len(param)):
                table_string += (f'{param[i][0]} {self._python_to_sql[param[i][1]]} {ext[param[i][0]]}, ')
            table_string = (table_string[:-2] + ')')
            
            try:
                self.cursor.execute(table_string)
            except:
                print('Table already exists')
            
        def insert_data(self, data, table):
            '''
            Metodo para insertar datos a la base de datos

            Args:
                data (list): Lista con los datos que se quieren insertar en la db
                table (str): Nombre de la tabla

            # '''
            dat = (f'INSERT INTO {table} VALUES (')
            for i in range(len(data)):
                dat += (str(data[i]) + ', ')
            dat = dat[:-2] + ')'
            self.cursor.execute(dat)
            self.conn.commit()
            #print(self.cursor.fetchall())

        def select_data(self, query):
            '''
            Metodo para hacer consultas a la base de datos
            '''
            
            self.cursor.execute(query)
            data = self.cursor.fetchall()
            return(data)
            #return(self.cursor.fetchall())


        @db_name.setter
        def db_name(self, name):
            if not hasattr(self, 'instance'):
                cls.instance = self.Instance(database_name = name)
            else:          
                class InvalidActionError(ValueError):
                    pass
                raise InvalidActionError("El nombre de la base de datos no se puede modificar")    
        
    # Singleton design pattern        
    def __new__(cls, db):
        if not hasattr(cls, 'instance'):
            cls.instance = cls.Instance(database_name = db)
        return cls.instance

