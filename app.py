from flask import Flask, request, jsonify
from models import db, Book, Review
from schemas import BookSchema, ReviewSchema
from cache import cache
import os

app = Flask(__name__)

# Config
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books.db"  # Change to PostgreSQL for prod
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["CACHE_TYPE"] = "RedisCache"
app.config["CACHE_REDIS_URL"] = "redis://localhost:6379/0"

# Initialize
db.init_app(app)
cache.init_app(app)

# Create DB tables
with app.app_context():
    db.create_all()

# Schemas
book_schema = BookSchema()
review_schema = ReviewSchema()

# Routes
@app.route("/books", methods=["GET"])
@cache.cached(timeout=60, key_prefix="all_books")
def list_books():
    books = Book.query.all()
    return jsonify(book_schema.dump(books, many=True))

@app.route("/books", methods=["POST"])
def add_book():
    data = request.get_json()
    errors = book_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    book = Book(**data)
    db.session.add(book)
    db.session.commit()
    return jsonify(book_schema.dump(book)), 201

@app.route("/books/<int:book_id>/reviews", methods=["GET"])
def get_reviews(book_id):
    reviews = Review.query.filter_by(book_id=book_id).all()
    if not reviews:
        return jsonify({"error": "No reviews found"}), 404
    return jsonify(review_schema.dump(reviews, many=True))

@app.route("/books/<int:book_id>/reviews", methods=["POST"])
def add_review(book_id):
    data = request.get_json()
    errors = review_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    book = Book.query.get(book_id)
    if not book:
        return jsonify({"error": "Book not found"}), 404
    review = Review(**data, book_id=book_id)
    db.session.add(review)
    db.session.commit()
    return jsonify(review_schema.dump(review)), 201

# Optional Swagger UI
from flask_swagger_ui import get_swaggerui_blueprint
SWAGGER_URL = '/docs'
API_URL = '/static/swagger.json'  # Create this manually or export via Swagger tool
swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

if __name__ == "__main__":
    app.run(debug=True)
