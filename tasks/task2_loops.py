#5. Write a Java program that uses a for loop to display all the orders for a specific customer.
def display_orders(customer_name, orders):
    for order in orders:
        if order["customer_name"] == customer_name:
            print(f"Order ID: {order['order_id']}, Status: {order['status']}")


#6. Implement a while loop to track the real-time location of a courier until it reaches its destination.
class Courier:
    def _init_(self, courier_id, location):
        self.courier_id = courier_id
        self.location = location
    
    def track_location(self, destination):
        while self.location != destination:
            print(f"Courier {self.courier_id} is at {self.location}. Moving towards {destination}...")
            self.location = "Next location"  # Simulating movement
        print(f"Courier {self.courier_id} has reached the destination: {destination}.")