from entity.courier import Courier
from entity.employee import Employee
from entity.location import Location

class CourierCompanyCollection:
    def __init__(self, companyName=""):
        self.__companyName = companyName
        self.__courierDetails = []      
        self.__employeeDetails = []     
        self.__locationDetails = []     

    def getCompanyName(self):
        return self.__companyName

    def setCompanyName(self, name):
        self.__companyName = name

    def getCourierDetails(self):
        return self.__courierDetails

    def setCourierDetails(self, courierList):
        self.__courierDetails = courierList

    def getEmployeeDetails(self):
        return self.__employeeDetails

    def setEmployeeDetails(self, employeeList):
        self.__employeeDetails = employeeList

    def getLocationDetails(self):
        return self.__locationDetails

    def setLocationDetails(self, locationList):
        self.__locationDetails = locationList


    def addCourier(self, courier: Courier):
        self.__courierDetails.append(courier)

    def addEmployee(self, employee: Employee):
        self.__employeeDetails.append(employee)

    def addLocation(self, location: Location):
        self.__locationDetails.append(location)

    def __str__(self):
        return (f"CourierCompanyCollection("
                f"Name={self.__companyName}, "
                f"Couriers={len(self.__courierDetails)}, "
                f"Employees={len(self.__employeeDetails)}, "
                f"Locations={len(self.__locationDetails)})")
