from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Book(db.Model):
    __tablename__ = "books"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(50))
    reviews = db.relationship("Review", backref="book", lazy=True)

class Review(db.Model):
    __tablename__ = "reviews"
    __table_args__ = (
        db.Index('ix_reviews_book_id', 'book_id'),  # Optimized index
    )
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(500))
    rating = db.Column(db.Integer)
    book_id = db.Column(db.Integer, db.ForeignKey("books.id"))
