# HealthCare Project

This is a Django-based healthcare project designed to manage patient-doctor mappings, authentication, and other healthcare-related functionalities.

## Features
- **Patient and Doctor Models**: Manage patient and doctor data with mappings.
- **RESTful APIs**: Endpoints for managing healthcare data.
- **JWT Authentication**: Secure authentication with customizable token lifetimes.
- **Scalable Design**: Modular structure for easy scalability.

## Project Structure
- `authentication/`: Handles user authentication and JWT token management.
- `doctors/`: Manages doctor-related data and APIs.
- `patients/`: Manages patient-related data and APIs.
- `mappings/`: Contains endpoints for patient-doctor mappings.
- `healthcare_backend/`: Core project settings and configurations.

## Setup Instructions
1. **Clone the repository**:
   ```bash
   git clone https://github.com/susanta7029/HealthCare.git
   ```
2. **Navigate to the project directory**:
   ```bash
   cd HealthCare
   ```
3. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```
4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
5. **Set up the database**:
   - Ensure PostgreSQL is installed and running.
   - Create a database named `healthcare_db`.
   - Update the `DATABASE_URL` in the `.env` file with your PostgreSQL credentials, e.g.:
     ```
     DATABASE_URL=postgres://postgres:Susanta7029%40@localhost:5432/healthcare_db
     ```
6. **Apply migrations**:
   ```bash
   python manage.py migrate
   ```
7. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

## API Endpoints
### Authentication
- `POST /api/token/`: Obtain JWT token.
- `POST /api/token/refresh/`: Refresh JWT token.

### Doctors
- `GET /doctors/`: List all doctors.
- `POST /doctors/`: Add a new doctor.

### Patients
- `GET /patients/`: List all patients.
- `POST /patients/`: Add a new patient.

### Patient-Doctor Mappings
- `GET /mappings/`: List all mappings.
- `POST /mappings/`: Create a new mapping.

## Technologies Used
- **Django**: Backend framework.
- **Django REST Framework**: API development.
- **Simple JWT**: Authentication.
- **PostgreSQL**: Database.

## Contributing
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-branch-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add new feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-branch-name
   ```
5. Open a pull request.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact
For any inquiries or support, please contact:
- **Name**: Susanta
- **Email**: susanta7029@example.com
- **GitHub**: [susanta7029](https://github.com/susanta7029)
