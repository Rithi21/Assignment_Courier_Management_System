class InvalidEmployeeIdException(Exception):
    def __init__(self, message="Invalid Employee ID"):
        self.message = message
        super().__init__(self.message)
