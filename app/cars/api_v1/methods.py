from flask import Blueprint
from flask_restful import Api
from .resources import CarResource, CarListResource

cars_v1_0_bp = Blueprint('cars_v1_0_bp', __name__)
api = Api(cars_v1_0_bp)

api.add_resource(CarListResource, '/api/cars/', endpoint='cars_list_resource')
api.add_resource(CarResource, '/api/cars/<int:car_id>', endpoint='car_resource')