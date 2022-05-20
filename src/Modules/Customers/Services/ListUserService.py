from src.Modules.Customers.Model.Customers import Customer


class ListCustomerService:

    def execute(id: int):
        try:
            customer = Customer.getById(id)

            if customer == None:
                return None

            return customer
        except:
            return 0
