from pydantic import BaseModel

class EmployeeDataResponseAPI(BaseModel):
    all_employee_data: list

    @staticmethod
    def format_to_response(employee_data):
        response=[
            {
                "name": employee_data.iloc[employee]['name'],
                "role": employee_data.iloc[employee]['role'],
                "years_of_experience": employee_data.iloc[employee]['years_of_experience']
            }
        for employee in employee_data.index]

        return response