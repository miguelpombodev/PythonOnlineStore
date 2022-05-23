from src.Error.ErrorMessage import ErrorMessage
from src.Modules.Customers.Model.Customers import Customer
from flask import jsonify


class CreateCustomerService:
    def execute(self, data: Customer):
        customerEmail = data['email']

        if Customer.getByEmail(customerEmail):
            return jsonify(message='Email already has an account'), 401

        customer = Customer(data)

        createdCustomer = customer.create()

        return createdCustomer
