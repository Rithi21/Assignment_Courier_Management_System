class Payment:
    def __init__(self, payment_id, user_id, amount, method, status):
        self.__payment_id = payment_id
        self.__user_id = user_id
        self.__amount = amount
        self.__method = method
        self.__status = status

    def get_payment_id(self):
        return self.__payment_id

    def set_payment_id(self, payment_id):
        self.__payment_id = payment_id

    def get_user_id(self):
        return self.__user_id

    def set_user_id(self, user_id):
        self.__user_id = user_id

    def get_amount(self):
        return self.__amount

    def set_amount(self, amount):
        self.__amount = amount

    def get_method(self):
        return self.__method

    def set_method(self, method):
        self.__method = method

    def get_status(self):
        return self.__status

    def set_status(self, status):
        self.__status = status

    def __str__(self):
        return f"Payment[ID={self.__payment_id}, UserID={self.__user_id}, Amount={self.__amount}, Method={self.__method}, Status={self.__status}]"
