import psycopg2

class Connect():
    def __init__(self, host, db_name, user, password, port):
        self.host = host
        self.db_name = db_name
        self.user = user
        self.password = password
        self.port = port
        
    def execute_query(self, query):
        try:
            connection = psycopg2.connect(user=self.user,
                                            password=self.password,
                                            host=self.host,
                                            port=self.port,
                                            database=self.db_name)
            cursor = connection.cursor()
            cursor.execute(query)
            connection.commit()
            count = cursor.rowcount
            print(count, "Record inserted successfully")
        except (Exception, psycopg2.Error) as error:
            print("Failed to insert record into table", error)
        
        finally:
            if connection:
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")
        
    