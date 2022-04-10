from app.db import db, BaseModelMixin

class Car (db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String)
    price = db.Column(db.Float)
    year = db.Column(db.String)
    color = db.Column(db.String)
    brand = db.relationship('Brand', backref='car', lazy=False, cascade='all, delete-orphan')

    def __init__(self, model, price, year, color, brand=[]):
        self.model = model
        self.price = price
        self.year = year
        self.color = color
        self.brand = brand

    def __repr__(self):
        return f'Car: ({self.model})'

    def __str__(self):
        return f'{self.model}'

class Brand (db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    car_id = db.Column(db.Integer, db.ForeignKey('car.id'), nullable=False)
    
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Brand: ({self.name})'

    def __str__(self):
        return f'{self.name}'