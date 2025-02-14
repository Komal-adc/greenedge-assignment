# GreenEdge Project API

This is a **Django REST Framework (DRF)** project for managing user authentication, registration, and membership subscriptions. The API allows users to register, log in using **JWT authentication**, and manage their membership status.

## Features

- **User Registration** (with phone number authentication)
- **JWT-based Authentication** (Login, Logout, Token Refresh)
- **Membership Management** (Silver, Gold, Diamond tiers with expiry dates)
- **Admin Panel** for managing users and memberships

## Tech Stack

- **Backend:** Django, Django REST Framework
- **Authentication:** JWT (JSON Web Token)
- **Database:** SQLite (default)
- **Tools:** Postman for API testing, Git for version control

## Installation & Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/greenedge-membership.git
   cd greenedge-membership
   ```
2. **Create a Virtual Environment & Activate It**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Apply Migrations**
   ```bash
   python manage.py migrate
   ```
5. **Create a Superuser**
   ```bash
   python manage.py createsuperuser
   ```
6. **Run the Development Server**
   ```bash
   python manage.py runserver
   ```

## API Endpoints

| Method | Endpoint         | Description                     |
| ------ | ---------------- | ------------------------------- |
| POST   | `/api/register/` | Register a new user             |
| POST   | `/api/login/`    | Obtain JWT authentication token |

## Contributing

1. Fork the repository
2. Create a new branch (`feature/your-feature`)
3. Commit your changes
4. Push to the branch and create a pull request

**Developed by [Karan Bista]**
