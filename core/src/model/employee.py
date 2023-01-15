import shutil
from core.src.data.connection_handler import ConnectionHandler
from core.src.data.input_handler import InputHandler
from core.src.data.data_handler import DataHandler
from core.src.data.output_handler import OutputHandler

def get_salary(years_of_experience):
    salary = years_of_experience*1000
    return salary

def get_position(years_of_experience):
    if years_of_experience < 2:
        position = 'junior'
    elif years_of_experience <= 4:
        position = 'senior'
    elif years_of_experience <= 6:
        position = 'manager'
    elif years_of_experience <= 10:
        position = 'senior manager'
    elif years_of_experience <= 20:
        position = 'general manager and above'
    return position

def get_employee_data():
    # retrieve data from db 
    connection_hander = ConnectionHandler()
    connection_hander.connect_to_db()
    input_handler = InputHandler(connection_hander)
    data_handler = DataHandler(input_handler)
    connection_hander.close_connection()
    return data_handler.employee_details

def write_employee_data(name, role, years_of_experience):
    # write data into db
    connection_hander = ConnectionHandler()
    connection_hander.connect_to_db()
    output_handler = OutputHandler(connection_hander)
    output_handler.write_employee_data(
        name=name,
        role=role,
        years_of_experience=years_of_experience
    )
    connection_hander.close_connection()

def upload_file(filename, file):
    # define file path 
    file_path = f"data/02_inputs/{filename}-api.csv"
    # save file 
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    file.file.close()
    return file_path

