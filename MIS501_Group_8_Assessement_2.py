#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Transportation Logistics System - Consolidated Solution
"""
import re

# ===================== GLOBAL DATA STORES =====================
fleet = []  # Format: {'vehicle_ID': str, 'Vehicle_type': str, 'Vehicle_Capacityy': int}
shipments = {}  # Format: {'SH123': {'origin': str, 'destination': str, 'weight': float, 'vehicle_id': str, 'status': str}}
delivered_shipments = {}  # Format: {'SH123': 'timestamp'}
vehicles = ["V001", "V002", "V003"]  # Available vehicle IDs

# ===================== FLEET MANAGEMENT (Part 1) =====================
def add_vehicle():
    vehicle_ID = input("Please enter your vehicle ID: ")
    for v in fleet:
        if v['vehicle_ID'] == vehicle_ID:
            print("Error: Vehicle ID already exists.")
            return
    Vehicle_type = input("Please enter vehicle type: ")
    try:
        Vehicle_Capacityy = int(input("Please enter vehicle capacity: "))
        if Vehicle_Capacityy <= 0:
            print("Error: Capacity must be a positive number.")
            return
    except ValueError:
        print("Error: Capacity must be an integer.")
        return
    fleet.append({'vehicle_ID': vehicle_ID, 'Vehicle_type': Vehicle_type, 'Vehicle_Capacityy': Vehicle_Capacityy})
    print("Vehicle added successfully.")

def update_vehicle():
    vehicle_ID = input("Please enter Vehicle ID to update: ")
    for vehicle in fleet:
        if vehicle['vehicle_ID'] == vehicle_ID:
            Vehicle_type = input("Please enter new Vehicle Type: ")
            try:
                Vehicle_Capacityy = int(input("Please enter new Vehicle Capacity: "))
                if Vehicle_Capacityy <= 0:
                    print("Error: Capacity must be a positive number.")
                    return
            except ValueError:
                print("Error: Capacity must be an integer.")
                return
            vehicle['Vehicle_type'] = Vehicle_type
            vehicle['Vehicle_Capacityy'] = Vehicle_Capacityy
            print("Vehicle updated successfully.")
            return
    print("Error: Vehicle ID not found.")

def remove_vehicle():
    vehicle_ID = input("Please enter Vehicle ID to remove: ")
    for vehicle in fleet:
        if vehicle['vehicle_ID'] == vehicle_ID:
            confirm = input("Confirm removal? (yes/no): ").lower()
            if confirm == "yes":
                fleet.remove(vehicle)
                print("Vehicle removed successfully.")
            else:
                print("Removal cancelled.")
            return
    print("Error: Vehicle ID not found.")

def view_vehicles():
    if not fleet:
        print("No vehicles in the fleet.")
    else:
        print("\nFleet Vehicles:")
        for vehicle in fleet:
            print(f"ID: {vehicle['vehicle_ID']}, Type: {vehicle['Vehicle_type']}, Capacity: {vehicle['Vehicle_Capacityy']}")
    input("\nPress Enter to return to menu.")

def fleet_management():
    while True:
        print("\nFleet Management Menu:")
        print("1. Add a vehicle")
        print("2. Update vehicle")
        print("3. Remove vehicle")
        print("4. View all vehicles")
        print("5. Return to Main Menu")
        choice = input("Select an option (1-5): ")
        if choice == "1":
            add_vehicle()
        elif choice == "2":
            update_vehicle()
        elif choice == "3":
            remove_vehicle()
        elif choice == "4":
            view_vehicles()
        elif choice == "5":
            break
        else:
            print("Invalid option. Try again.")

# ===================== SHIPMENT MANAGEMENT (Part 2) =====================
def create_shipment():
    shipment_id = input("Enter Shipment ID (e.g., SH123456AX): ")
    pattern = r"^SH\d{6}[A-Z]{2}$"

    if not re.match(pattern, shipment_id):
        print("Invalid format. Use SH123456AX format.")
        return

    if shipment_id in shipments:
        print("Shipment ID already exists.")
        return

    origin = input("Enter Origin location: ")
    destination = input("Enter Destination location: ")

    try:
        weight = float(input("Enter shipment weight (kg): "))
        if weight <= 0:
            print("Weight must be positive.")
            return
    except ValueError:
        print("Invalid weight input.")
        return

    print("Available vehicles:")
    for i, v in enumerate(vehicles):
        print(f"[{i + 1}] {v}")

    try:
        vehicle_index = int(input("Choose vehicle (1-3): "))
        if vehicle_index < 1 or vehicle_index > len(vehicles):
            print("Invalid vehicle selection.")
            return
    except ValueError:
        print("Invalid input.")
        return

    vehicle_id = vehicles[vehicle_index - 1]
    shipments[shipment_id] = {
        "origin": origin,
        "destination": destination,
        "weight": weight,
        "vehicle_id": vehicle_id,
        "status": "In Transit"
    }
    print(f"Shipment {shipment_id} created successfully.")

def track_shipment():
    shipment_id = input("Enter Shipment ID to track: ")
    if shipment_id not in shipments:
        print("Shipment not found.")
        return
    print(f"Status: {shipments[shipment_id]['status']}")

def view_all_shipments():
    if not shipments:
        print("No shipments found.")
        return

    for sid, details in shipments.items():
        print(f"\nShipment ID: {sid}")
        print(f"Origin: {details['origin']}")
        print(f"Destination: {details['destination']}")
        print(f"Weight: {details['weight']}kg")
        print(f"Vehicle: {details['vehicle_id']}")
        print(f"Status: {details['status']}")

    while True:
        if input("\nType 'exit' to return: ").lower() == 'exit':
            break

def shipment_management():
    while True:
        print("\nShipment Management Menu:")
        print("1. Create shipment")
        print("2. Track shipment")
        print("3. View all shipments")
        print("4. Return to Main Menu")
        choice = input("Select option (1-4): ")
        if choice == "1":
            create_shipment()
        elif choice == "2":
            track_shipment()
        elif choice == "3":
            view_all_shipments()
        elif choice == "4":
            break
        else:
            print("Invalid option.")

# ===================== DELIVERY MANAGEMENT (Part 3) =====================
def mark_shipment_delivered():
    shipment_id = input("Enter Shipment ID to mark delivered: ")
    if shipment_id not in shipments:
        print("Shipment not found.")
        return
    if shipments[shipment_id]['status'] == "Delivered":
        print("Already delivered.")
        return
    shipments[shipment_id]['status'] = "Delivered"
    delivered_shipments[shipment_id] = "Delivered"
    print(f"Shipment {shipment_id} marked as delivered.")

def view_delivery_status():
    shipment_id = input("Enter Shipment ID to check: ")
    if shipment_id in delivered_shipments:
        print("Status: Delivered")
    elif shipment_id in shipments:
        print(f"Status: {shipments[shipment_id]['status']}")
    else:
        print("Shipment not found.")

def delivery_management():
    while True:
        print("\nDelivery Management Menu:")
        print("1. Record delivery")
        print("2. Check status")
        print("3. Return to Main Menu")
        choice = input("Select option (1-3): ")
        if choice == "1":
            mark_shipment_delivered()
        elif choice == "2":
            view_delivery_status()
        elif choice == "3":
            break
        else:
            print("Invalid option.")

# ===================== MAIN MENU =====================
def main():
    while True:
        print("\n=== MAIN MENU ===")
        print("1. Fleet Management")
        print("2. Shipment Management")
        print("3. Delivery Management")
        print("4. Exit Program")
        choice = input("Enter choice (1-4): ")
        if choice == "1":
            fleet_management()
        elif choice == "2":
            shipment_management()
        elif choice == "3":
            delivery_management()
        elif choice == "4":
            print("Exiting program...")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()