
# RentMate API

RentMate is a Django REST Framework (DRF) based rent and utility tracking system for homeowners, tenants, and admins. It includes role-based access, CRUD operations for key models, Swagger documentation, and Celery integration.

---

## 📦 Setup Instructions

```bash
git clone <your-repo-url>
cd rentmate
python -m venv env
source env/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

---

## 🔐 Roles

- **Admin / Superadmin**: Full access to all resources.
- **Owner**: Can manage their own apartments, tenants, and utility bills.
- **Tenant**: Can view and update their own rent records and tenant info.

---

## 📘 API Documentation

Visit:  
[http://localhost:8000/api/docs/](http://localhost:8000/api/docs/)

---

## 🧭 API Endpoints

### 🏠 Apartments

| Method | Endpoint             | Description                   | Access          |
|--------|----------------------|-------------------------------|------------------|
| GET    | `/api/apartments/`   | List apartments               | Admin, Owner     |
| POST   | `/api/apartments/`   | Create apartment              | Owner            |
| PUT    | `/api/apartments/:id/`| Update apartment             | Owner (own only) |
| DELETE | `/api/apartments/:id/`| Delete apartment             | Admin only       |

---

### 👤 Tenants

| Method | Endpoint           | Description                 | Access            |
|--------|--------------------|-----------------------------|--------------------|
| GET    | `/api/tenants/`    | List tenants                | Admin, Self        |
| POST   | `/api/tenants/`    | Create tenant               | Owner only         |
| PUT    | `/api/tenants/:id/`| Update tenant               | Self or Admin      |
| DELETE | `/api/tenants/:id/`| Delete tenant               | Admin only         |

---

### 💡 Utility Bills

| Method | Endpoint             | Description                  | Access            |
|--------|----------------------|------------------------------|--------------------|
| GET    | `/api/bills/`        | List utility bills           | Admin, Owner       |
| POST   | `/api/bills/`        | Create utility bill          | Owner (own apt)    |
| PUT    | `/api/bills/:id/`    | Update utility bill          | Admin only         |
| DELETE | `/api/bills/:id/`    | Delete utility bill          | Admin only         |

---

### 💰 Rent Records

| Method | Endpoint              | Description                   | Access            |
|--------|-----------------------|-------------------------------|--------------------|
| GET    | `/api/rents/`         | List rent records             | Tenant, Admin      |
| POST   | `/api/rents/`         | Create rent record            | Tenant (self)      |
| PUT    | `/api/rents/:id/`     | Update rent record            | Tenant (self)      |
| DELETE | `/api/rents/:id/`     | Delete rent record            | Admin only         |

---

### 👥 User Accounts

| Method | Endpoint               | Description         |
|--------|------------------------|---------------------|
| POST   | `/api/accounts/register/` | Register a user (Owner only can register Tenant) |
| POST   | `/api/accounts/login/`    | Log in              |
| GET    | `/api/accounts/profile/`  | View own profile    |

---

## 📄 License

MIT License.
