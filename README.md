# Courier Service API

## Overview
This project is a **Django Rest Framework (DRF)** based **Courier Service API** that allows users to manage parcels, track delivery status, and handle user authentication & authorization with **JWT**.

## Features
- **Admin** can add/update/delete parcels.
- **Delivery Driver** can view assigned parcels and update their delivery status.
- **Customer** can track their parcels and update the delivery address.
- **Role-based access control (RBAC)** implemented.
- **Soft delete** mechanism to prevent permanent data loss from database.

## Technologies Used
- **Backend:** Django, Django Rest Framework (DRF)
- **Authentication:** JWT (JSON Web Token)
- **Database:** SQLite (default) 


## Installation & Setup

Ensure you have installed:
- Python 3
- pip (Python package manager)
- Virtual environment tool (`venv`)

### Steps to Set Up the Project

1. **Clone the repository**
   ```sh
   git clone https://github.com/your-username/courier-service-api.git
   cd courier-service-api
   ```

2. **Create and activate a virtual environment**
   ```sh
   python -m venv venv  # Create venv
   source venv/bin/activate  # Mac/Linux
   venv\Scripts\activate  # Windows
   ```

3. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```

4. **Apply database migrations**
   ```sh
   python manage.py migrate
   ```

5. **Create a superuser (Admin access)**
   ```sh
   python manage.py createsuperuser
   ```
   Follow the prompts to create an admin user.

6. **Run the server**
   ```sh
   python manage.py runserver
   ```
   API will be available at `http://127.0.0.1:8000/`

---
## API Endpoints

### Authentication
- **Obtain Token**: `POST /api/token/`
  ```json
  {
    "username": "admin",
    "password": "admin"
  }
  ```
- **Refresh Token**: `POST /api/token/refresh/`

### Parcel Management (Admin)
- **Create Parcel**: `POST /api/packages/`
- **Update Parcel**: `PUT /api/packages/<int:pk>//`
- **Delete Parcel (Soft Delete)**: `DELETE /api/packages/<int:pk>//`

### Delivery Driver
- **View Assigned Parcels**: `GET /api/assigned_packages/`
- **Update Parcel Status**: `PATCH /api/update_status/<int:pk>//`

### Customer
- **Track Parcel**: `GET /api/track/<str:t_number>/`



## API Testing Tools  
- **Postman** (for manual testing)  
- **pytest-django** (for automated API testing in Django)  
- **cURL** (for CLI-based API testing)
- I used POSTMAN for API testing of this project.
- In below You will find a short tutorial of POSTMAN for testing your project.
  
### Testing with Postman  
1. Install Postman from [postman.com](https://www.postman.com/).  
2. Import the provided `Postman Collection` (if available).  
3. Use the following endpoints:  
   - **Get all parcels**: `GET /api/packages/`  
   - **Create a new parcel**: `POST /api/packages/`  
   - **Update a parcel**: `PUT /api/packages/<int:pk>/`  
   - **Delete a parcel**: `DELETE /api/packages/<int:pk>//`  
4. Use an authentication token.  






