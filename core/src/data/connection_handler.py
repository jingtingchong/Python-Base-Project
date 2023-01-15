import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

class ConnectionHandler:

    def __init__(self):
        self.connect_to_db()
    
    def connect_to_db(self):
        self.conn = psycopg2.connect(
            host=os.getenv('POSTGRES_HOST'),
            port=os.getenv('POSTGRES_PORT'),
            database=os.getenv('POSTGRES_DB'),
            user=os.getenv('POSTGRES_USER'),
            password=os.getenv('POSTGRES_PASSWORD')
        )
        self.cur = self.conn.cursor()

    def close_connection(self):
        self.cur.close()

