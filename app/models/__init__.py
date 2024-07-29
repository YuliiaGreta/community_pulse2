from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .questions import Question
from .response import Response
from .category import Category