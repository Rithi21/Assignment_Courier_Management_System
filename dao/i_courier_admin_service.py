from abc import ABC, abstractmethod
from entity.employee import Employee  # assuming your Employee class is in entities folder

class ICourierAdminService(ABC):

    @abstractmethod
    def addCourierStaff(self, employeeObj: Employee):
        pass
