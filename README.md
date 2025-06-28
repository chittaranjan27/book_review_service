# 📘 Book Review API

This is a RESTful **Book Review Service** built with **Flask**, **SQLite**, **SQLAlchemy**, and **Redis**. It allows users to create books, add reviews, and retrieve data efficiently using caching. The project includes proper data modeling, database migration setup, unit tests, and error handling.

## 🚀 Features

- 📚 Add and list books	
- 📝 Add and list reviews for a book
- ⚡ Redis caching on GET `/books`
- 🧪 Unit + integration tests with Pytest
- 🛠️ SQLite for local DB, SQLAlchemy ORM
- ✅ Clean error responses
- 🗂️ Modular folder structure

## 📁 Project Structure

backend/
├── app.py               # Flask app and routes
├── models.py            # Book & Review SQLAlchemy models
├── schemas.py           # Marshmallow validation schemas
├── cache.py             # Redis cache setup
├── tests/               # Pytest test cases
│ └── test_routes.py
├── requirements.txt     # Python dependencies
└── README.md

## 🔧 Setup Instructions

### 1️⃣   Clone and Setup Environment

git clone https://github.com/chittaranjan27/book_review_service.git
cd book_review_services
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip freeze > requirements.txt

🗄️ Running Database Migrations
This project uses SQLite (file-based DB), so no manual migrations are needed.

✅ Tables are automatically created on first run using db.create_all() inside app.py.

🧠 Redis Setup
sudo apt update
sudo apt install redis
sudo service redis start
redis-cli ping
Output: PONG

▶️ Run the Flask Service
python app.py
Default server: http://127.0.0.1:5000

🔍 API Endpoints

GET all books-
http://127.0.0.1:5000/books

GET reviews for a book
http://127.0.0.1:5000/books/1/reviews

POST a new book
http://127.0.0.1:5000/books
Body: raw → JSON

POST a review for a book
http://127.0.0.1:5000/books/1/reviews
Body: raw → JSON

✅ Run Tests

Run tests: PYTHONPATH=$(pwd) pytest tests/

📹 Live Walkthrough (5 mins)
🎥 Link to video recording demonstrating:
Code structure
Key design decisions
How to run and test
Redis/cache explanation
Test results

✍️ Design Decisions
Flask was used for its simplicity and flexibility.
Used SQLAlchemy ORM for database interactions.
SQLite used in dev (PostgreSQL ready with minor changes).
Redis improves performance for /books endpoint.
Validation via Marshmallow.
Modular file separation for clarity.
