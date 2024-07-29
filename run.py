<<<<<<< HEAD
from app import create_app, db
from app.models import Category, Question

app = create_app()

@app.route('/')
def home():
    return "Welcome to Community Pulse!"

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Создание таблиц, если их нет
        if not Category.query.first():
            sample_category = Category(name="General")
            sample_question = Question(text="What do you think about open source?", category=sample_category)
            db.session.add(sample_category)
            db.session.add(sample_question)
            db.session.commit()
    app.run(debug=True)  # Включение режима отладки
=======
from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
>>>>>>> e33c05c0128305e6a458ab2ca82b2fa65d8bfb1e
