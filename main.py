from dao.courier_service_db import CourierServiceDB
from exception.tracking_number_not_found_exception import TrackingNumberNotFoundException


def main():
    db = CourierServiceDB()
    
    while True:
        print("\n===== Courier Management System =====")
        print("1. Insert Courier")
        print("2. Update Courier Status")
        print("3. View Courier History by User ID")
        print("4. Generate Shipment Status Report")
        print("5. Generate Revenue Report")
        print("6. Cancel Order")
        print("7. Exit")
        choice = input("Enter your choice: ")

        try:
            if choice == '1':
                courier_id = int(input("Enter Courier ID: "))
                user_id = int(input("Enter User ID: "))
                service_id = int(input("Enter Service ID: "))
                sender_name = input("Enter Sender Name: ")
                sender_address = input("Enter Sender Address: ")
                receiver_name = input("Enter Receiver Name: ")
                receiver_address = input("Enter Receiver Address: ")
                weight = float(input("Enter Weight (kg): "))
                status = "Pending"
                tracking_number = input("Enter Tracking Number: ")
                dispatch_date = input("Enter Dispatch Date (YYYY-MM-DD HH:MM:SS): ")
                delivery_date = input("Enter Delivery Date (YYYY-MM-DD): ")

                db.insert_courier(courier_id, user_id, service_id, sender_name, sender_address,
                                  receiver_name, receiver_address, weight, status,
                                  tracking_number, dispatch_date, delivery_date)

            elif choice == '2':
                tracking_number = input("Enter Tracking Number: ")
                status = input("Enter New Status (e.g., In Transit, Delivered): ")
                if not db.update_courier_status(tracking_number, status):
                    raise TrackingNumberNotFoundException()

            elif choice == '3':
                user_id = int(input("Enter User ID: "))
                history = db.view_courier_history(user_id)
                print("\nCourier History:")
                if history:
                    for record in history:
                        print(record)
                else:
                    print("No courier history found for this user.")

            elif choice == '4':
                report = db.generate_shipment_status_report()
                print("\nShipment Status Report:")
                for record in report:
                    print(f"Tracking Number: {record.TrackingNumber}, Status: {record.Status}")

            elif choice == '5':
                revenue = db.generate_revenue_report()
                if revenue and revenue.TotalRevenue:
                    print(f"\nTotal Revenue: ₹{revenue.TotalRevenue:.2f}")
                else:
                    print("\nTotal Revenue: ₹0.00")

            elif choice == '6':
                tracking_number = input("Enter Tracking Number to Cancel: ")
                if not db.cancel_order(tracking_number):
                    raise TrackingNumberNotFoundException()

            elif choice == '7':
                print("Exiting the system. Thank you!")
                db.close_connection()
                break

            else:
                print("Invalid choice! Please enter a number between 1 and 7.")

        except TrackingNumberNotFoundException as e:
            print("Error:", e)


        except ValueError:
            print("Invalid input type! Please enter numbers where expected.")

        except Exception as e:
            print("An unexpected error occurred:", e)

if __name__ == "__main__":
    main()
