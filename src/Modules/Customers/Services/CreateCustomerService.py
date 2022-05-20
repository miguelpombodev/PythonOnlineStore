from src.Modules.Customers.Model.Customers import Customer


class CreateCustomerService:
    def execute(self, data: dict):
        customer = Customer(data)

        createdCustomer = customer.create()

        return createdCustomer