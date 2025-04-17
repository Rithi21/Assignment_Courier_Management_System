class Courier:
    def __init__(self, courier_id, sender_address, receiver_address, weight, status):
        self.__courier_id = courier_id
        self.__sender_address = sender_address
        self.__receiver_address = receiver_address
        self.__weight = weight
        self.__status = status

    def get_courier_id(self):
        return self.__courier_id

    def set_courier_id(self, courier_id):
        self.__courier_id = courier_id

    def get_sender_address(self):
        return self.__sender_address

    def set_sender_address(self, sender_address):
        self.__sender_address = sender_address

    def get_receiver_address(self):
        return self.__receiver_address

    def set_receiver_address(self, receiver_address):
        self.__receiver_address = receiver_address

    def get_weight(self):
        return self.__weight

    def set_weight(self, weight):
        self.__weight = weight

    def get_status(self):
        return self.__status

    def set_status(self, status):
        self.__status = status

    def __str__(self):
        return f"Courier[ID={self.__courier_id}, From={self.__sender_address}, To={self.__receiver_address}, Weight={self.__weight}kg, Status={self.__status}]"
