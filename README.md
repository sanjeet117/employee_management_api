# Employee Management API

A simple Employee Management REST API built using FastAPI with Pydantic validation and API Key authentication.

## Features

- Get all employees
- Get employee by ID
- Create a new employee
- Update an existing employee
- Delete an employee
- Pydantic data validation
- API Key authentication for protected endpoints
- Proper HTTP status codes
- Swagger API documentation

## Technologies Used

- Python
- FastAPI
- Pydantic
- Uvicorn
- python-dotenv

## Project Structure

```text
employee_management_api/
│
├── .env
├── .gitignore
├── main.py
├── README.md
├── requirements.txt
└── venv/
```

## Installation

Clone the repository and move into the project directory.

```bash
cd employee_management_api
```

Create and activate a virtual environment:

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the project root:

```env
API_KEY=your-secret-key
```

The `.env` file is excluded from GitHub using `.gitignore`.

**Do not commit real API keys or secrets to GitHub.**

## Run the Application

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

## API Endpoints

| Method | Endpoint | Authentication |
|---|---|---|
| GET | `/employees` | Not required |
| GET | `/employees/{employee_id}` | Not required |
| POST | `/employees` | Required |
| PUT | `/employees/{employee_id}` | Required |
| DELETE | `/employees/{employee_id}` | Required |

## API Key Authentication

Protected endpoints require the following HTTP header:

```text
X-API-Key: your-secret-key
```

### Missing API Key

If the API key is not provided:

```text
401 Unauthorized
```

Response:

```json
{
    "detail": "API key is missing"
}
```

### Invalid API Key

If an incorrect API key is provided:

```text
403 Forbidden
```

Response:

```json
{
    "detail": "Invalid API key"
}
```

### Valid API Key

If the correct API key is provided, the protected endpoint is allowed to execute.

## Example Employee

```json
{
    "name": "Amit Kumar",
    "email": "amit@example.com",
    "department": "IT",
    "salary": 55000
}
```

## Testing

The API can be tested using Swagger UI:

```text
http://127.0.0.1:8000/docs
```

The demonstration includes:

1. Successful GET request
2. Successful POST request with API key
3. Failed POST request without API key
4. Failed POST request with incorrect API key
5. Successful PUT request with API key
6. Successful DELETE request with API key

## Security

The API key is stored in the `.env` file and is not committed to GitHub.

The `.gitignore` file contains:

```text
.env
venv/
__pycache__/
*.pyc
```

This prevents sensitive information and unnecessary files from being pushed to the repository.

## Author

Super30 FastAPI Assignment