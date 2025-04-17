from dao.courier_user_service_collection_impl import CourierUserServiceCollectionImpl
from dao.i_courier_admin_service import ICourierAdminService

class CourierAdminServiceCollectionImpl(CourierUserServiceCollectionImpl, ICourierAdminService):
    def add_courier_staff(self, employee):
        self.company_obj.employee_details.append(employee)
        print(f"Employee {employee.employee_name} added.")
        return employee.employee_id
