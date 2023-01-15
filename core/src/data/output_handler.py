class OutputHandler:

    def __init__(self, connection_handler):
        self.connection_handler = connection_handler

    def write_employee_data(self, name, role, years_of_experience):
        # retrieve db connection
        conn = self.connection_handler.conn
        cur = self.connection_handler.cur

        # insert data
        query = "INSERT INTO public.employee (name, role, years_of_experience) " \
                f"VALUES ('{name}','{role}', {years_of_experience})"
        cur.execute(query)
        conn.commit()


        