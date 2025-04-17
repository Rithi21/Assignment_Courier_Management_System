"""9. Parcel Tracking: Create a program that allows users to input a parcel tracking number.Store the
tracking number and Status in 2d String Array. Initialize the array with values. Then, simulate the
tracking process by displaying messages like "Parcel in transit," "Parcel out for delivery," or "Parcel
delivered" based on the tracking number's status. """

tracking_data = [
    ["TRK001", "In Transit"],
    ["TRK002", "Out for Delivery"],
    ["TRK003", "Delivered"]
]

def track_parcel(tracking_number):
    for row in tracking_data:
        if row[0] == tracking_number:
            status = row[1]
            return f"Status for {tracking_number}: {status}"
    return "Tracking number not found"

"""10. Customer Data Validation: Write a function which takes 2 parameters, data-denotes the data and
detail-denotes if it is name addtress or phone number.Validate customer information based on
following critirea. Ensure that names contain only letters and are properly capitalized, addresses do not
contain special characters, and phone numbers follow a specific format (e.g., ###-###-####)."""

import re

def validate_customer_data(data, detail):
    if detail == "name":
        return data.isalpha() and data.istitle()
    elif detail == "address":
        return re.match("^[A-Za-z0-9\s,.-]+$", data) is not None
    elif detail == "phone":
        return re.match("^\d{3}-\d{3}-\d{4}$", data) is not None
    return False

"""11. Address Formatting: Develop a function that takes an address as input (street, city, state, zip code)
and formats it correctly, including capitalizing the first letter of each word and properly formatting the
zip code."""

def format_address(street, city, state, zip_code):
    def capitalize_words(text):
        return " ".join(word.capitalize() for word in text.split())

    formatted_address = f"{capitalize_words(street)}, {capitalize_words(city)}, {state.upper()} - {zip_code.zfill(6)}"
    return formatted_address

"""12. Order Confirmation Email: Create a program that generates an order confirmation email. The email
should include details such as the customer's name, order number, delivery address, and expected
delivery date."""

def generate_confirmation_email(name, order_no, address, delivery_date):
    return f"""
    Dear {name},

    Your order #{order_no} has been successfully placed.
    It will be delivered to:
    {address}

    Expected Delivery Date: {delivery_date}

    Thank you for choosing HexaCourier!
    """

"""13. Calculate Shipping Costs: Develop a function that calculates the shipping cost based on the distance
between two locations and the weight of the parcel. You can use string inputs for the source and
destination addresses."""

def calculate_shipping_cost(distance_km, weight_kg):
    base_rate = 5.0  # ₹ per km
    weight_rate = 10.0  # ₹ per kg
    return round((base_rate * distance_km) + (weight_rate * weight_kg), 2)


"""14. Password Generator: Create a function that generates secure passwords for courier system
accounts. Ensure the passwords contain a mix of uppercase letters, lowercase letters, numbers, and
special characters."""
import random
import string

def generate_password(length=10):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

"""15. Find Similar Addresses: Implement a function that finds similar addresses in the system. This can be
useful for identifying duplicate customer entries or optimizing delivery routes.Use string functions to
implement this."""
def find_similar_addresses(addresses, target):
    target = target.lower()
    similar = [addr for addr in addresses if target in addr.lower()]
    return similar
