from uuid import uuid5

from sqlalchemy import DateTime
from ....Shared.Providers.db import db
from sqlalchemy.sql import func
from werkzeug.security import generate_password_hash


class Customer(db.Model):
    __tablename__ = "customers"

    id = db.Column(db.String(36), primary_key=True)
    name = db.Column(db.String(35), nullable=False)
    surname = db.Column(db.String(100), nullable=False)
    CPF = db.Column(db.String(100), nullable=False, unique=True, index=True)
    email = db.Column(db.String(100), nullable=False, unique=True, index=True)
    password = db.Column(db.String(64), nullable=False)
    created_at = db.Column(DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(DateTime(timezone=True), onupdate=func.now())

    def __init__(self, data: dict) -> None:
        self.id = uuid5,
        self.name = data['name'],
        self.surname = data['surname'],
        self.CPF = data['CPF'],
        self.email = data['email'],
        self.password = generate_password_hash(data['password'])
