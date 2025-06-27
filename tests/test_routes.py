import pytest
from app import app, db, Book, Review

@pytest.fixture
def client():
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    with app.test_client() as client:
        with app.app_context():
            db.drop_all()  # 👈 Add this line to clear previous tables/data
            db.create_all()
        yield client
        with app.app_context():
            db.session.remove()
            db.drop_all()

def test_list_books_empty(client):
    response = client.get("/books")
    assert response.status_code == 200
    assert response.json == []

def test_add_book(client):
    response = client.post("/books", json={"title": "1984", "author": "Orwell"})
    assert response.status_code == 201
    assert response.json["title"] == "1984"

def test_add_review(client):
    client.post("/books", json={"title": "Dune", "author": "Herbert"})
    response = client.post("/books/1/reviews", json={"text": "Epic!", "rating": 5})
    assert response.status_code == 201
    assert response.json["text"] == "Epic!"
