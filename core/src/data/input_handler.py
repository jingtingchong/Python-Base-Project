import pandas as pd


class InputHandler:

    def __init__(self, connection_handler):
        self.connection_handler = connection_handler

    def initialize_data_handler(self, data_handler):
        # retrieve db connection
        conn = self.connection_handler.conn
        # call all input handler methods to populate data handler 
        self.__init_employee_details_from_db(data_handler, conn)


    def __init_employee_details_from_db(self, data_handler, conn):
        query = "SELECT * FROM public.employee"
        data_handler.employee_details = pd.read_sql(query, conn)





