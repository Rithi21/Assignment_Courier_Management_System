#1. Write a program that checks whether a given order is delivered or not based on its status.

def check_order_status(status):
    if status == "Delivered":
        print("Order is delivered.")
    elif status == "Processing":
        print("Order is being processed.")
    elif status == "Cancelled":
        print("Order has been cancelled.")
    else:
        print("Unknown order status.")

#2. Implement a switch-case statement to categorize parcels based on their weight into "Light","Medium," or "Heavy."
def categorize_parcel(weight):
    if weight < 5:
        print("Light parcel")
    elif 5 <= weight < 20:
        print("Medium parcel")
    else:
        print("Heavy parcel")

#3. Implement User Authentication 1. Create a login system for employees and customers using Java control flow statements.
def authenticate_user(user_type, username, password):
    if user_type == "employee":
        # Here we assume the credentials are predefined
        if username == "employee1" and password == "emp123":
            print("Employee login successful.")
        else:
            print("Invalid employee credentials.")
    elif user_type == "customer":
        if username == "customer1" and password == "cust123":
            print("Customer login successful.")
        else:
            print("Invalid customer credentials.")
    else:
        print("Invalid user type.")

#4. Implement Courier Assignment Logic 1. Develop a mechanism to assign couriers to shipments based on predefined criteria (e.g., proximity, load capacity) using loops.
def assign_couriers(couriers, shipments):
    for shipment in shipments:
        # Assign the first available courier for the shipment
        for courier in couriers:
            if courier["available"]:
                print(f"Courier {courier['name']} assigned to shipment {shipment}.")
                courier["available"] = False  # Mark as unavailable
                break