# coding=utf-8
from flask_sqlalchemy import SQLAlchemy
from random import choice

db = SQLAlchemy()


class Post(db.Model):
    """A Post class"""

    __tablename__ = "posts"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    slug = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text)

    def __init__(self, title, description):
        self.title = title
        self.slug = self.__get_unique_slugify(title)
        self.description = description

    def __repr__(self):
        """Display when printing a Post object"""

        return "<Post: {}>".format(self.title)

    def as_dict(self):
        """Convert object to dictionary"""

        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __get_unique_slugify(self, title):
        random_string = ''.join(choice('0123456789ABCDEF') for i in range(8))
        return title.replace(' ', '-')+'_'+random_string
