from flask import request
from flask_restful import Resource
from .schemas import CarSchema
import json
from ..models import Car, Brand
from ...common.errorhandling import ObjectNotFound

car_schema = CarSchema()

class CarListResource(Resource):
    def get(self):
        cars = Car.get_all()
        result = car_schema.dump(cars, many=True)

        return result, 201
    
    def post(self):
        data = request.get_json()
        car_dict = car_schema.load(data)
        print(car_dict)
        car = Car(name=car_dict['name'],
                price=car_dict['price'],
                year=car_dict['year'],
                color=car_dict['color']
        )

        for brand in car_dict['brand']:
            car.brand.append(Brand(brand['name']))

        car.save()

        resp = car_schema.dump(car)

        return resp, 201

class CarResource(Resource):
    def get(self, car_id):
        car = Car.get_by_id(car_id)

        if car is None:
            raise ObjectNotFound('El coche no existe')

        resp = car_schema.dump(car)

        return resp