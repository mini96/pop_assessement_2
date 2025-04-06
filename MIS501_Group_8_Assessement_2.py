# Transportation Logistics System - MIS501 Assessment 2

# Global data storage (using lists and tuples)
fleet = []  # Format: (vehicle_id, vehicle_type, capacity)
shipments = []  # Format: (shipment_id, origin, destination, weight, vehicle_id, status)
delivered = []  # Format: (shipment_id, delivery_time)

def display_main_menu():
    """Display the main menu and return user choice."""
    print("\n=== Main Menu ===")
    print("1. Fleet Management")
    print("2. Shipment Management")
    print("3. Delivery Management")
    print("4. Quit Application")
    return input("Enter your choice (1-4): ")

# ===== Part 1: Fleet Management (Skeleton) =====
def fleet_management():
    """Fleet Management submenu   """
    while True:
        print("\n=== Fleet Management ===")
        print("1. Add a vehicle")
        print("2. Update vehicle information")
        print("3. Remove a vehicle")
        print("4. View all vehicles")
        print("5. Quit fleet management")
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            continue  # Groupmate to implement
        elif choice == "2":
            continue
        elif choice == "3":
            continue
        elif choice == "4":
            continue
        elif choice == "5":
            break
        else:
            print("Invalid choice. Try again.")

# ===== Part 2: Shipment Management (Fully Implemented) =====
def shipment_management():
    """Shipment Management submenu   """
    while True:
        print("\n=== Shipment Management ===")
        print("1. Create a new shipment")
        print("2. Track a shipment")
        print("3. View all shipments")
        print("4. Quit shipment management")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            create_shipment()
        elif choice == "2":
            track_shipment()
        elif choice == "3":
            view_shipments()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Try again.")

def create_shipment():
    """Create a new shipment with validated inputs."""
    print("\n--- Create New Shipment ---")
    
    # Input validation for Shipment ID (unique)
    while True:
        shipment_id = input("Enter Shipment ID: ")
        if not shipment_id:
            print("Error: Shipment ID cannot be empty.")
            continue
        if any(ship[0] == shipment_id for ship in shipments):
            print("Error: Shipment ID already exists.")
            continue
        break

    origin = input("Enter Origin: ")
    destination = input("Enter Destination: ")
    
    # Input validation for Weight (positive numeric)
    while True:
        weight = input("Enter Weight (kg): ")
        if weight.replace('.', '', 1).isdigit() and float(weight) > 0:
            weight = float(weight)
            break
        print("Error: Weight must be a positive number.")

    # Display available vehicles (assuming fleet is populated)
    print("\nAvailable Vehicles:")
    for vehicle in fleet:
        print(f"ID: {vehicle[0]}, Type: {vehicle[1]}, Capacity: {vehicle[2]}")

    # Input validation for Vehicle ID (exists in fleet)
    while True:
        vehicle_id = input("Enter Vehicle ID: ")
        if any(vehicle[0] == vehicle_id for vehicle in fleet):
            break
        print("Error: Vehicle ID not found in fleet.")

    # Add shipment to list
    shipments.append((shipment_id, origin, destination, weight, vehicle_id, "In transit"))
    print("Shipment created successfully!")

def track_shipment():
    """Track a shipment by ID."""
    print("\n--- Track Shipment ---")
    shipment_id = input("Enter Shipment ID: ")
    
    for shipment in shipments:
        if shipment[0] == shipment_id:
            print(f"Status: {shipment[5]}")
            return
    
    print("Error: Shipment ID not found.")

def view_shipments():
    """Display all shipments in a tabular format."""
    print("\n--- All Shipments ---")
    print("ID\tOrigin\tDestination\tWeight\tVehicle ID\tStatus")
    print("-" * 60)
    for shipment in shipments:
        print(f"{shipment[0]}\t{shipment[1]}\t{shipment[2]}\t{shipment[3]}\t{shipment[4]}\t{shipment[5]}")
    print("\nTo exit the menu, type 'Exit'.")

# ===== Part 3: Delivery Management (Skeleton) =====
def delivery_management():
    """Delivery Management submenu   """
    while True:
        print("\n=== Delivery Management ===")
        print("1. Record delivery for a shipment")
        print("2. View delivery status for a shipment")
        print("3. Quit delivery management")
        choice = input("Enter your choice (1-3): ")
        
        if choice == "1":
            continue  # Groupmate to implement
        elif choice == "2":
            continue
        elif choice == "3":
            break
        else:
            print("Invalid choice. Try again.")

# ===== Main Program =====
if __name__ == "__main__":
    print("=== Transportation Logistics System ===")
    
    # Sample data for testing (can be removed)
    fleet.append(("V001", "Truck", 5000))
    fleet.append(("V002", "Van", 2000))
    
    while True:
        choice = display_main_menu()
        if choice == "1":
            fleet_management()
        elif choice == "2":
            shipment_management()
        elif choice == "3":
            delivery_management()
        elif choice == "4":
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")