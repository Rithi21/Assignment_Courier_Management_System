from dao.courier_user_service_impl import CourierUserServiceImpl
from dao.i_courier_admin_service import ICourierAdminService

class CourierAdminServiceImpl(CourierUserServiceImpl, ICourierAdminService):
    def add_courier_staff(self, employee):
        self.company_obj.employee_details.append(employee)
        return employee.employee_id
