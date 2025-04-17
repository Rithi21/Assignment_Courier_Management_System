class Employee:
    def __init__(self, employee_id, name, role, contact_number, email):
        self.__employee_id = employee_id
        self.__name = name
        self.__role = role
        self.__contact_number = contact_number
        self.__email = email

    def get_employee_id(self):
        return self.__employee_id

    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_role(self):
        return self.__role

    def set_role(self, role):
        self.__role = role

    def get_contact_number(self):
        return self.__contact_number

    def set_contact_number(self, contact_number):
        self.__contact_number = contact_number

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def __str__(self):
        return f"Employee[ID={self.__employee_id}, Name={self.__name}, Role={self.__role}, Contact={self.__contact_number}, Email={self.__email}]"
