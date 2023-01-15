import pandas as pd 


class DataHandler:

    def __init__(self, input_handler):
        self.employee_details = None
        self.input_handler = input_handler

        # Request input handler to initialize and populate data handler
        input_handler.initialize_data_handler(self)
        

