from flask import Blueprint, request, jsonify
# from werkzeug.exceptions import BadRequestKeyError

from src.Modules.Customers.Model.Customers import Customer

customers_blueprints = Blueprint('customers', __name__)


@customers_blueprints.route('/', methods=['POST'])
def create_customer():
    return 0
