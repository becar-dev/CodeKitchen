# 🍽️ CodeKitchen

A smart restaurant management system built with Django and DRF for modern developers — from kitchen orders to customer satisfaction, all powered by clean code, APIs, and automation.

## 🔧 Technologies

- Python 3.x
- Django 5.2.3
- Django REST Framework
- Simple JWT (Authentication)
- drf-yasg (Swagger API Docs)

---

## ⚙️ Installation & Setup

### 1️⃣ Clone and activate virtual environment

```bash
git clone https://github.com/becar-dev/CodeKitchen.git
cd CodeKitchen
python -m venv venv
# Activate:
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4️⃣ Create superuser (optional)

```bash
python manage.py createsuperuser
```

### 5️⃣ Run the development server

```bash
python manage.py runserver
```

---

## 🔐 Authentication

JWT Authentication is used.

- Get token:
  `POST /api/token/`
- Refresh token:
  `POST /api/token/refresh/`

Include access token as:
```
Authorization: Bearer <your_token>
```

---

## 📚 API Documentation

Interactive Swagger and Redoc documentation are available:

- Swagger UI: [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)
- Redoc UI: [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/)

---

## 🧩 Core Features (MVP)

### ✅ 1. Buyurtma zanjiri
- Ofitsiant buyurtmani kiritadi → Oshxona uni ko‘radi → Statuslar: `new → pending → cooking → done`

### ✅ 2. Ombor hisoboti
- Har bir buyurtmada kerakli mahsulotlar avtomatik ombordagi miqdordan ayiriladi

### ✅ 3. Oddiy hisobot
- Kun oxirida: nechta buyurtma, eng ko‘p buyurtma qilingan taomlar

---

## 🍽️ Sample Dishes (MenuItems)

- Beshbarmoq
- Qovurilgan baliq
- Qiyma shashlik
- Jaz shashlik
- Tovuq shashlik

---

## 🔗 Useful Links

- Telegram Support: [@becar_dev](https://t.me/becar_dev)
- GitHub Repo: [https://github.com/becar-dev/CodeKitchen](https://github.com/becar-dev/CodeKitchen)

---