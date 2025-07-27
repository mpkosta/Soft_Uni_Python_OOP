class Customer:
    id = 1

    def __init__(self, name: str, address: str, email: str):
        self.name = name
        self.address = address
        self.email = email
        self.id = Customer.id
        Customer.id += 1

    # @staticmethod
    # def get_next_id():
    #     return Customer.id

    @classmethod
    def get_next_id(cls):
        return cls.id #same as above


