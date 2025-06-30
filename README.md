# Vendor Management API

A simple RESTful API built with FastAPI to manage vendor data.

## 🚀 Features

- Create new vendors (POST `/vendors`)
- Retrieve all vendors with optional pagination and search (GET `/vendors`)
- Retrieve vendor details by ID (GET `/vendors/{id}`)
- Update vendor information (PUT `/vendors/{id}`)
- Delete a vendor (DELETE `/vendors/{id}`)

## 🛠️ Technologies Used

- Python 3.12
- FastAPI
- SQLAlchemy
- SQLite (can be switched to PostgreSQL)
- Pydantic v2
- Uvicorn (ASGI server)

## 📦 Setup and Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/vendor-management-api.git
   cd vendor-management-api
