# Little Lemon Restaurant Backend

This is the final Capstone project for the Meta Back-End Developer Certificate. It is a Django-based API designed to handle restaurant menu management and table booking systems.

## Project Features
- **Menu API:** Endpoints to Create, Read, Update, and Delete menu items.
- **Booking API:** Endpoints to manage table reservations.
- **Authentication:** User registration and token-based authentication using Djoser and DRF.
- **Unit Testing:** Automated tests for the Menu model and API views.

## Prerequisites
- Python
- MySQL Server
- Pipenv (or Pip)

## How to Run This Project

### 1. Clone the Repository
```bash
git clone https://github.com/aishwaryakmp/LittleLemon.git
cd LittleLemon
```

### 2. Install Dependencies
This project uses **Pipenv** for dependency management.
```bash
pipenv install
pipenv shell
```
*(If you do not use Pipenv, you can install the requirements manually: `pip install django djangorestframework djoser mysqlclient`)*

### 3. Database Configuration
1. Make sure your MySQL server is running.
2. Create a new database named **`LittleLemon`** in MySQL:
   ```sql
   CREATE DATABASE LittleLemon;
   ```
3. Open the file `LittleLemon/settings.py`.
4. Locate the `DATABASES` section and update the `'USER'` and `'PASSWORD'` fields with your local MySQL credentials.

### 4. Run Migrations
Create the database tables:
```bash
python manage.py migrate
```

### 5. Run the Server
Start the development server:
```bash
python manage.py runserver
```

---

## API Endpoints

| Endpoint | Method | Description | Access |
|---|---|---|---|
| **/restaurant/menu/** | GET, POST | List all items or Create new item | Public |
| **/restaurant/menu/{id}** | GET, PUT, DELETE | Retrieve, Update, or Delete a single item | Public |
| **/restaurant/booking/tables/** | GET, POST | List or Create bookings | **Authenticated Only (Token)** |
| **/auth/users/** | POST | Register a new user | Public |
| **/api-token-auth/** | POST | Obtain Auth Token (Login) | Public |

---

## Testing
To run the included unit tests, execute the following command:
```bash
python manage.py test
```
**After creating this file, save and push it:**
```bash
git add README.md
git commit -m "Added documentation"
git push
```
