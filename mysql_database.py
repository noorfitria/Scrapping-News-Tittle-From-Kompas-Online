import json
from mysql.connector import connect
    
class MySqlDB:
    def __init__(self):
        with open('db_cred_kompas.json') as f:
            tokens = json.load(f)
            
        self.username = tokens.get('user')
        self.password = tokens.get('password')
        self.dbname = tokens.get('database')
    
    def open_connection(self):
        try:
            self.db = connect(
            host = 'localhost',
            user = self.username,
            password = self.password,
            database = self.dbname
            )
            print(f"Koneksi Berhasil")
        except Exception as e:
            print(f"Koneksi Gagal : {e}")
        
    def create_db(self):
        query = f'''
            create database if not exists {self.dbname}
        '''
        try:
            my_cursor = self.db.cursor()
            my_cursor.execute(query)
            my_cursor.close()
            print(f"Pembuatan Database dengan nama {self.dbname} Berhasil")
        except Exception as e:
            print(f"Pembuatan Database Gagal : {e}")
        
    def create_table(self):
        query = f'''
            CREATE Table IF NOT EXISTS artikel(
            id int primary key auto_increment,
            title VARCHAR(255) not null
            )
        '''
        try:
            my_cursor = self.db.cursor()
            my_cursor.execute(query)
            my_cursor.close()
            print(f"Pembuatan Tabel Berhasil")
        except Exception as e:
            print(f"Pembuatan Tabel Gagal : {e}")
        
    def search_all(self):
        query = '''
            SELECT *
            FROM ARTIKEL
            '''
        try:
            cursor_db = self.db.cursor()
            cursor_db.execute(query)
            result = cursor_db.fetchall()
            cursor_db.close()
            
            for title in result:
                print(title)
        except Exception as e:
            print(f"Pengambilan Data Gagal : {e}")
            
    def insert_titles(self, titles:list=[]):
        try:
            cursor_db = self.db.cursor()
            for title in titles:
                query = f'''
                INSERT INTO ARTIKEL (title)
                VALUES ("{title}")
                '''
                print(query)
                cursor_db.execute(query)
            self.db.commit()
            cursor_db.close()
            print("Penambahan Data Berhasil")
        except Exception as e:
            print(f"Penambahan Data Gagal : {e}")
            self.db.rollback()
            
    def close_connection(self):
        self.db.close()
        
        
if __name__ == "__main__":
    db = MySqlDB()
    db.open_connection()
    # db.create_db()
    # db.create_table()