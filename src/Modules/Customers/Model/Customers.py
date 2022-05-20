from uuid import uuid4

from sqlalchemy import DateTime
from flask import jsonify
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
    password = db.Column(db.String(102), nullable=False)
    # created_at = db.Column(DateTime(timezone=True), server_default=func.now())
    # updated_at = db.Column(DateTime(timezone=True), server_onupdate=func.now())

    def __init__(self, data: dict) -> None:
        self.id = uuid4().hex,
        self.name = data['name'],
        self.surname = data['surname'],
        self.CPF = data['CPF'],
        self.email = data['email'],
        self.password = generate_password_hash(data['password'])

  
    def create(self):
        try:
            db.session.add(self)
            db.session.commit()
            return jsonify(
                id=self.id,
                name=self.name,
                surname=self.surname,
                CPF=self.CPF,
                email=self.email,
                password=self.password,
            ), 201
        except Exception as e:
            return jsonify(message= str(e) + "Internal Error ocurred trying save vessel"), 409
    
    @classmethod
    def getById(cls, id: int):
        customer = cls.query.filter_by(id==id).first()
        
        if customer:
            return customer
        
        return None
        
