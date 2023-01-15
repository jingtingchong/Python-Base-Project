from typing import Union
from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from core.src.model.employee import get_salary, get_position, \
    get_employee_data, write_employee_data, upload_file
from service_provider.api.output_template.employee_output import EmployeeDataResponseAPI

# Initialise router
employee_router = APIRouter()


@employee_router.post("/salary_calculator/")
async def salary_calculator(years_of_experience: int):
    salary = get_salary(years_of_experience)
    position = get_position(years_of_experience)
    return JSONResponse(
        status_code=200,
        content={
            'years_of_experience': years_of_experience,
            'position': position,
            'salary': salary,
        }
    )


@employee_router.post("/retrieve_employee_data/")
async def retrieve_employee_data():
    employee_data = get_employee_data()
    return EmployeeDataResponseAPI(
        all_employee_data = \
            EmployeeDataResponseAPI.format_to_response(employee_data)
    )


@employee_router.post("/add_employee_data/")
async def add_employee_data(
    name: str,
    role: str,
    years_of_experience: int
):
    write_employee_data(name, role, years_of_experience)
    return JSONResponse(
        status_code=200,
        content={
            'message': 'updated employee data in database',
        }
    )


@employee_router.post("/upload_csv_file/")
async def upload_csv_file(filename: str, file: UploadFile = File(...)):
    file_path = upload_file(filename, file)
    return JSONResponse(
        status_code=200,
        content={
            'message': 'uploaded successfully',
            'file_path': file_path,
        }
    )

