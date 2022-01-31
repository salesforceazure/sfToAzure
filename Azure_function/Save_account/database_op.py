import psycopg2
import pandas as pd

class Database_op:
    def __init__(self):
        # Update connection string information
        self.database="citus"
        self.user = "citus" 
        self.password = "Vedity@123"
        self.host = "c.comoscls.postgres.database.azure.com"
        self.port = "5432"
        self.sslmode = "require"
        self.connection_string = "postgresql://" + self.user + ":" + self.password + "@" + self.host + ":" + self.port + "/" + self.database # Make database connection string.
        
    def start_connection(self):
        self.conn = psycopg2.connect(database = self.database, user = self.user , password = self.password, host = self.host, port = self.port) #Get connection object by initializing connection to database. 
        self.cursor = self.conn.cursor()    
        return self.conn, self.cursor
    
    def close_connection(self):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
        
    def insert_data(self,accountnumber, name):
        _,cursor = self.start_connection()
        print("Connection established")        
        cursor.execute("INSERT INTO salesforce.account (accountnumber, name) VALUES (%s, %s);", (accountnumber, name))
        print("Row inserted")    
        self.close_connection()                    
        return "Data inserted successfully"

    def get_data(self):
        _,cursor = self.start_connection()
        query = "SELECT * FROM salesforce.account;"
        df = pd.read_sql_query(query, con=self.conn)
        print(df.head())
        self.close_connection()
        return df
    
    # def get_accname_accnumber(self,accountnumber,accountname):
    #     _,cursor = self.start_connection()
    #     try:
    #         query = "SELECT name FROM salesforce.account WHERE accountnumber = {} AND accountname={};".format(accountnumber,accountname)
    #         df = pd.read_sql_query(query, con=self.conn)
    #         self.close_connection()
    #         return 1
    #     except:        
    #         return 0
                
        