#7. Create an array to store the tracking history of a parcel, where each entry represents a location update.
tracking_history = ["Warehouse", "Dispatched", "In Transit", "Out for Delivery", "Delivered"]

def display_tracking_history():
    print("Tracking History:")
    for location in tracking_history:
        print(f"→ {location}")

#8. Implement a method to find the nearest available courier for a new order using an array of couriers.
couriers = [
    {"id": "C001", "distance": 12},
    {"id": "C002", "distance": 5},
    {"id": "C003", "distance": 9}
]


def find_nearest_courier(couriers):
    nearest = min(couriers, key=lambda x: x["distance"])
    return nearest["id"]