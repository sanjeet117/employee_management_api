from fastapi import FastAPI, HTTPException, Header, Depends, status
from pydantic import BaseModel, Field
from dotenv import load_dotenv
import os


# Load environment variables from .env file
load_dotenv()

API_KEY = os.getenv("API_KEY")


app = FastAPI(
    title="Employee Management API",
    description="Employee CRUD API with API Key Authentication",
    version="1.0.0"
)


# --------------------------------------------------
# Pydantic Models
# --------------------------------------------------

class EmployeeCreate(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    email: str
    department: str = Field(min_length=2, max_length=50)
    salary: float = Field(gt=0)


class EmployeeResponse(EmployeeCreate):
    id: int


# --------------------------------------------------
# Sample Employee Data
# --------------------------------------------------

employees = {
    1: {
        "id": 1,
        "name": "Rahul Sharma",
        "email": "rahul@example.com",
        "department": "IT",
        "salary": 50000
    },
    2: {
        "id": 2,
        "name": "Priya Patel",
        "email": "priya@example.com",
        "department": "HR",
        "salary": 45000
    }
}


# --------------------------------------------------
# API Key Authentication
# --------------------------------------------------

def verify_api_key(x_api_key: str | None = Header(default=None)):
    
    if x_api_key is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="API key is missing"
        )

    if x_api_key != API_KEY:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid API key"
        )

    return x_api_key


# --------------------------------------------------
# GET - All Employees
# --------------------------------------------------

@app.get(
    "/employees",
    response_model=list[EmployeeResponse],
    status_code=status.HTTP_200_OK
)
def get_employees():

    return list(employees.values())


# --------------------------------------------------
# GET - Employee by ID
# --------------------------------------------------

@app.get(
    "/employees/{employee_id}",
    response_model=EmployeeResponse,
    status_code=status.HTTP_200_OK
)
def get_employee(employee_id: int):

    if employee_id not in employees:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Employee not found"
        )

    return employees[employee_id]


# --------------------------------------------------
# POST - Create Employee
# Protected Endpoint
# --------------------------------------------------

@app.post(
    "/employees",
    response_model=EmployeeResponse,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(verify_api_key)]
)
def create_employee(employee: EmployeeCreate):

    new_id = max(employees.keys()) + 1

    new_employee = {
        "id": new_id,
        **employee.model_dump()
    }

    employees[new_id] = new_employee

    return new_employee


# --------------------------------------------------
# PUT - Update Employee
# Protected Endpoint
# --------------------------------------------------

@app.put(
    "/employees/{employee_id}",
    response_model=EmployeeResponse,
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(verify_api_key)]
)
def update_employee(
    employee_id: int,
    employee: EmployeeCreate
):

    if employee_id not in employees:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Employee not found"
        )

    updated_employee = {
        "id": employee_id,
        **employee.model_dump()
    }

    employees[employee_id] = updated_employee

    return updated_employee


# --------------------------------------------------
# DELETE - Delete Employee
# Protected Endpoint
# --------------------------------------------------

@app.delete(
    "/employees/{employee_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    dependencies=[Depends(verify_api_key)]
)
def delete_employee(employee_id: int):

    if employee_id not in employees:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Employee not found"
        )

    del employees[employee_id]

    return None