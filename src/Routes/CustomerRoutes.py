from flask import Blueprint, request
from src.Modules.Customers.Controllers.CustomersController import CustomerController
# from werkzeug.exceptions import BadRequestKeyError

customers_blueprints = Blueprint('customers', __name__)


customersController = CustomerController()

@customers_blueprints.route('/create', methods=['POST'])
def create_customer():

    data = dict(request.json)

    createdCustomer = customersController.create(data)

    return createdCustomer

@customers_blueprints.route('/', methods=['GET'])
def list_customer():
    id = request.args.get("id")

    customer = customersController.list(id)

    return customer
