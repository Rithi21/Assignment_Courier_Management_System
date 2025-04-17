import pyodbc
from util.db_connection import DBConnection

class CourierServiceDB:
    def __init__(self):
        self.conn = DBConnection.get_connection()
        self.cursor = self.conn.cursor()

    def insert_courier(self, courier_id, user_id, service_id, sender_name, sender_address,
                       receiver_name, receiver_address, weight, status,
                       tracking_number, dispatch_date, delivery_date):
        query = '''
        INSERT INTO Courier 
        (CourierID, UserID, ServiceID, SenderName, SenderAddress, ReceiverName, ReceiverAddress, 
         Weight, Status, TrackingNumber, DispatchDate, DeliveryDate)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        '''
        try:
            # Ensure correct datetime format
            if dispatch_date and not isinstance(dispatch_date, pyodbc.Date):
                from datetime import datetime
                if isinstance(dispatch_date, str):
                    dispatch_date = datetime.strptime(dispatch_date, "%Y-%m-%d")

            if delivery_date:
                if isinstance(delivery_date, str):
                    delivery_date = datetime.strptime(delivery_date, "%Y-%m-%d")
            else:
                delivery_date = None

            self.cursor.execute(query, (courier_id, user_id, service_id, sender_name, sender_address,
                                        receiver_name, receiver_address, weight, status,
                                        tracking_number, dispatch_date, delivery_date))
            self.conn.commit()
            print("Courier inserted successfully.")
        except Exception as e:
            print("Error inserting courier:", e)

    def update_courier_status(self, tracking_number, new_status):
        try:
            self.cursor.execute("UPDATE Courier SET Status = ? WHERE TrackingNumber = ?", 
                                (new_status, tracking_number))
            self.conn.commit()
            if self.cursor.rowcount > 0:
                print("Courier status updated.")
            else:
                print("Tracking number not found.")
        except Exception as e:
            print("Error updating status:", e)

    def view_courier_history(self, user_id):
        try:
            self.cursor.execute("SELECT * FROM Courier WHERE UserID = ?", (user_id,))
            return self.cursor.fetchall()
        except Exception as e:
            print("Error fetching history:", e)
            return []

    def generate_shipment_status_report(self):
        try:
            self.cursor.execute("SELECT TrackingNumber, Status FROM Courier")
            return self.cursor.fetchall()
        except Exception as e:
            print("Error fetching report:", e)
            return []

    def generate_revenue_report(self):
        try:
            self.cursor.execute('''
                SELECT SUM(CS.Cost) AS TotalRevenue
                FROM Courier C
                JOIN CourierServices CS ON C.ServiceID = CS.ServiceID
            ''')
            return self.cursor.fetchone()
        except Exception as e:
            print("Error calculating revenue:", e)
            return None

    def cancel_order(self, tracking_number):
        try:
            self.cursor.execute("SELECT Status FROM Courier WHERE TrackingNumber = ?", (tracking_number,))
            result = self.cursor.fetchone()
            if not result:
                print("Tracking number not found.")
                return
            if result[0] == "Delivered":
                print("Order already delivered. Cannot cancel.")
                return
            self.cursor.execute("UPDATE Courier SET Status = ? WHERE TrackingNumber = ?", ("Cancelled", tracking_number))
            self.conn.commit()  
            print(f"Order with tracking number {tracking_number} has been cancelled.")
        except Exception as e:
            print("Error cancelling order:", e)

    def close_connection(self):
        self.cursor.close()
        self.conn.close()
