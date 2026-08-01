 # E-Commerce Product Management REST API

## Project Description

This project is a REST API developed using "FastAPI" and "SQLAlchemy" for managing an E-Commerce Product System.

The API performs CRUD (Create, Read, Update, Delete) operations on five product categories:

- Mobiles
- Laptops
- Tablets
- Smartwatches
- Headphones

The project also includes:

- Data Validation using Pydantic
- Error Handling
- Automatic Swagger Documentation
- SQLite Database
- Seed Data (50 Records)


## Technologies Used:

- Python 3.x
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Uvicorn



## Project Structure

Ecommerce rest api
│
├── database.py
├── models.py
├── schemas.py
├── crud.py
├── main.py
├── seed_data.py
├── requirements.txt
└── readme.md




# Installation

### Step 1: Clone the Repository

```bash
git clone <https://github.com/sairamarige/Ecommerce-rest-api.git>
```

# Step 2: Open Project

```bash
cd Ecommerce rest api
```

# Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

If requirements.txt is not available:

```bash
pip install fastapi sqlalchemy uvicorn pydantic
```



# Seed Database:
Run the following command to insert sample data.

bash:
python seed_data.py

This inserts:
- 10 Mobiles
- 10 Laptops
- 10 Tablets
- 10 Smartwatches
- 10 Headphones
Total Records = 50


## Run the Application

bash
uvicorn main:app --reload


Server URL:
http://127.0.0.1:8000


Swagger Documentation:
http://127.0.0.1:8000/docs


Alternative API Documentation:
http://127.0.0.1:8000/redoc




# REST API Endpoints:

# Mobile:

| Method | Endpoint |
|---------|----------|
| POST | /mobiles |
| GET | /mobiles |
| GET | /mobiles/{id} |
| PUT | /mobiles/{id} |
| DELETE | /mobiles/{id} |



# Laptop:

| Method | Endpoint |
|---------|----------|
| POST | /laptops |
| GET | /laptops |
| GET | /laptops/{id} |
| PUT | /laptops/{id} |
| DELETE | /laptops/{id} |



# Tablet:

| Method | Endpoint |
|---------|----------|
| POST | /tablets |
| GET | /tablets |
| GET | /tablets/{id} |
| PUT | /tablets/{id} |
| DELETE | /tablets/{id} |



# SmartWatch:

| Method | Endpoint |
|---------|----------|
| POST | /smartwatches |
| GET | /smartwatches |
| GET | /smartwatches/{id} |
| PUT | /smartwatches/{id} |
| DELETE | /smartwatches/{id} |



# Headphone:

| Method | Endpoint |
|---------|----------|
| POST | /headphones |
| GET | /headphones |
| GET | /headphones/{id} |
| PUT | /headphones/{id} |
| DELETE | /headphones/{id} |


# Features:
- RESTful API
- CRUD Operations
- Five Product Categories
- Data Validation
- Error Handling
- Automatic Swagger Documentation
- SQLAlchemy ORM
- SQLite Database
- Seed Data Support
- Modular Project Structure



# Database Tables:
- mobiles
- laptops
- tablets
- smartwatches
- headphones



# Sample Data:
Each table contains 10 sample records.
Total Sample Records = 50


# Author:
Name: Arige Sairam
Project: E-Commerce Product Management REST API
Technology: FastAPI + SQLAlchemy + SQLite
