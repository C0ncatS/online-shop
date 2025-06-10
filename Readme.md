# 🛒 Django Online Shop

A complete and extensible e-commerce platform built with Django. This project supports shopping cart functionality, Stripe payments, order processing via webhooks, background task handling with Celery and RabbitMQ, caching with Redis, and real-time task monitoring with Flower. Ideal for learning or building a production-ready online store.

---

## 🚀 Features

- 🗂️ Product catalog with category filtering  
- 🛍️ Shopping cart with quantity and price tracking  
- 📦 Checkout with customer info collection  
- 💳 Stripe integration with webhook support via Stripe CLI  
- ✅ Order confirmation via webhook event `checkout.session.completed`  
- 📧 Post-payment email notification (via Celery task)  
- ⚡ Redis for caching  
- 🪄 Celery + RabbitMQ for background processing  
- 🌸 Flower dashboard for monitoring Celery tasks  
- 🛠️ Admin panel to manage products and orders  

---

## 🧑‍💻 User Flow

1. Browse products and filter by category.  
2. Click a product image to view details and select quantity.  
3. Add the product to the cart.  
4. Review cart contents and proceed to checkout.  
5. Fill in contact and shipping details.  
6. Confirm order summary and redirect to Stripe Checkout.  
7. Upon successful payment:  
   - Stripe sends a webhook to confirm payment.  
   - The backend verifies the event and marks the order as paid.  
8. Redirect to a success or failure page.  

---

## 🛠️ Tech Stack

| Component        | Technology         |
|------------------|--------------------|
| Backend          | Django              |
| Database         | MySQL (via Docker)  |
| Caching          | Redis               |
| Background Tasks | Celery + RabbitMQ   |
| Task Monitoring  | Flower              |
| Payments         | Stripe              |
| Emails           | SMTP |
| Frontend         | Django Templates (HTML/CSS) |

---

## 📦 Setup with Docker Compose

### 1. Clone the Repository

```bash
git clone https://github.com/C0ncatS/online-shop.git
cd online-shop
```

### 2. Create a `.env` File

```env
# Stripe
STRIPE_PUBLISHABLE_KEY=your-publishable-key
STRIPE_SECRET_KEY=your-secret-key
STRIPE_API_VERSION=XXXX-XX-XX
STRIPE_WEBHOOK_SECRET=your-webhook-secret

# Database
DATABASE_NAME=onlineshop
DATABASE_USER=shopuser
DATABASE_PASSWORD=shoppass
DATABASE_HOST=db
DATABASE_PORT=3306

# SMTP
EMAIL_HOST_USER=XXXX
EMAIL_HOST_PASSWORD=XXXX
DEFAULT_FROM_EMAIL=XXXX@XXXX.XXX
```

### 3. Build and Start All Services

```bash
docker compose up --build
```

This will launch:
- Django app at [http://localhost:8000](http://localhost:8000)  
- MySQL database  
- Redis cache  
- RabbitMQ with management UI ([http://localhost:15672](http://localhost:15672))  
- Celery worker  
- Flower task monitor at [http://localhost:5555](http://localhost:5555)

---

## ⚙️ Initial Setup

### Create Superuser

```bash
docker compose exec server python manage.py createsuperuser
```

---

## 🔐 Admin Panel

After creating a superuser, access the admin panel at:

[http://localhost:8000/admin/](http://localhost:8000/admin/)

---

## ✅ To-Do

- [ ] Add user registration/login  
- [ ] Add product search and pagination  
- [ ] Add production Docker settings  

---

## 🧪 Development Notes

- Uses Docker Compose to manage all services.  
- MySQL is the default database (via container).  
- Environment variables managed via `.env` and `python-decouple`.  
- Stripe CLI is required to simulate webhook events locally.  
- Redis and Celery handle background jobs; Flower helps you monitor them in real time.

---

## 📄 License

MIT License

---

Made with ❤️ by [@C0ncatS](https://github.com/C0ncatS)