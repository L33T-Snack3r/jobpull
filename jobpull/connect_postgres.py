import psycopg2
from loguru import logger

class PostgresConnector:

    def __init(self, 
                host: str = "localhost",        # or 127.0.0.1
                port: int = 5432,
                dbname: str = "jobs_db",
                user: str = "postgres",
                password: str = "postgres"):
        
        self.host = host
        self.port = port
        self.dbname = dbname
        self.user = user
        self.password = password

    def execute_query(self, query : str, inputvars : list, insertion : bool = True) -> list | None:
        #1. Open connection
        connector = psycopg2.connect(host=self.host, 
                                          port=self.port,
                                          dbname=self.dbname,
                                          user=self.user,
                                          password=self.password)
        cur = connector.cursor()

        #2. Execute query
        result = None
        if insertion:
            cur.executemany(query, inputvars)
            logger.info("Insertion query executed successfully")
        else:
            cur.execute(query, inputvars)
            result = cur.fetchall()
            logger.info("Select query executed successfully")

        #3. Close connection
        cur.close()
        connector.close()

        return result

        
