from src.Modules.Customers.Services.CreateCustomerService import CreateCustomerService
from src.Modules.Customers.Services.ListUserService import ListCustomerService


class CustomerController:

    def create(self, data):
        createCustomerService = CreateCustomerService()

        createdCustomer = createCustomerService.execute(data)

        return createdCustomer

    def list(self):
        listUserService = ListCustomerService()

        customer = listUserService(id)

        return customer
