from dao.i_courier_user_service import ICourierUserService
from entity.courier_company import CourierCompany

class CourierUserServiceImpl(ICourierUserService):
    def __init__(self):
        self.company_obj = CourierCompany()

    def place_order(self, courier):
        print("Using array-based storage.")
        pass

    def get_order_status(self, tracking_number):
        pass

    def cancel_order(self, tracking_number):
        pass

    def get_assigned_order(self, courier_staff_id):
        pass
