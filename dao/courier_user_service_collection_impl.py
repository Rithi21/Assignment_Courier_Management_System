from abc import ABC
from datetime import datetime
from entity.courier import Courier
from entity.courier_company_collection import CourierCompanyCollection
from dao.i_courier_user_service import ICourierUserService

class CourierUserServiceCollectionImpl(ICourierUserService, ABC):
    def __init__(self):

        self.company_obj = CourierCompanyCollection("HexaCourier")

    def place_order(self, courier_obj):
  
        Courier.generate_tracking_number()  
        courier_obj.tracking_number = Courier.tracking_id_counter

        self.company_obj.courier_details.append(courier_obj)

        print(f"[INFO] Courier placed with Tracking Number: {courier_obj.tracking_number}")
        return courier_obj.tracking_number

    def get_order_status(self, tracking_number):
        for courier in self.company_obj.courier_details:
            if courier.tracking_number == tracking_number:
                print(f"[INFO] Status for Tracking {tracking_number} is {courier.status}")
                return courier.status
        print(f"[ERROR] Tracking Number {tracking_number} not found.")
        return None

    def cancel_order(self, tracking_number):
        for courier in self.company_obj.courier_details:
            if courier.tracking_number == tracking_number:
                if courier.status.lower() == "delivered":
                    print(f"[WARNING] Cannot cancel delivered courier.")
                    return False
                courier.status = "Cancelled"
                print(f"[INFO] Courier with Tracking {tracking_number} cancelled.")
                return True
        print(f"[ERROR] Tracking Number {tracking_number} not found.")
        return False

    def get_assigned_order(self, courier_staff_id):
        assigned_orders = [
            courier for courier in self.company_obj.courier_details
            if courier.user_id == courier_staff_id
        ]
        print(f"[INFO] Orders assigned to Staff ID {courier_staff_id}:")
        for c in assigned_orders:
            print(c)
        return assigned_orders
