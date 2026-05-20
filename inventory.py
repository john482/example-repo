# ==========================
# inventory.py (OOP Synthesis)
# ==========================

from tabulate import tabulate  # Optional table formatting

# ====== Absolute file path (OneDrive folder) ======
INVENTORY_FILE = r"C:\Users\ps2707536\OneDrive - Surbana Jurong Private Limited\01. PS - University & Training\02. Qualifications\01. SUN - AI & Software Engineering\Level 1 - Foundations of AI Engineering\M03T07 – OOP – Synthesis\inventory.txt"


# ========= The beginning of the class ==========
class Shoe:
    """
    Shoe class representing one stock item.
    Attributes:
        country, code, product, cost, quantity
    """

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        """Returns the cost of the shoes."""
        return self.cost

    def get_quantity(self):
        """Returns the quantity of the shoes."""
        return self.quantity

    def __str__(self):
        """Returns a user-friendly string representation of the shoe object."""
        return (
            f"Country: {self.country} | "
            f"Code: {self.code} | "
            f"Product: {self.product} | "
            f"Cost: {self.cost} | "
            f"Quantity: {self.quantity}"
        )


# ========= The end of the class ==========
# ========= Data store (required list) ==========
shoes_list = []  # stores Shoe objects


# ========= File rewriting ==========
def write_shoes_data():
    """
    Writes the current shoes_list back to INVENTORY_FILE in the same format:
    Country,Code,Product,Cost,Quantity
    ...
    """
    try:
        with open(INVENTORY_FILE, "w", encoding="utf-8") as file:
            file.write("Country,Code,Product,Cost,Quantity\n")
            for shoe in shoes_list:
                file.write(
                    f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n"
                )
    except PermissionError:
        print("Permission error: Close inventory.txt if it is open in Excel/Notepad and try again.")
    except Exception as e:
        print("An unexpected error occurred while writing:", e)


# ========= Functions outside the class ==========
def read_shoes_data():
    """
    Opens INVENTORY_FILE, reads data, creates Shoe objects, appends to shoes_list.
    Uses try/except for error handling and skips the first line (header).
    """
    shoes_list.clear()  # avoid duplicate loads if called again

    try:
        with open(INVENTORY_FILE, "r", encoding="utf-8") as file:
            lines = file.readlines()

        # Skip header line
        for line in lines[1:]:
            line = line.strip()
            if not line:
                continue

            data = line.split(",")
            if len(data) != 5:
                # Defensive: skip malformed lines
                continue

            country, code, product, cost, quantity = data

            try:
                cost = float(cost)
                quantity = int(quantity)
            except ValueError:
                # Defensive: skip lines that can't be converted
                continue

            shoe = Shoe(country, code, product, cost, quantity)
            shoes_list.append(shoe)

    except FileNotFoundError:
        print("File not found:")
        print(INVENTORY_FILE)
    except PermissionError:
        print("Permission error: Close inventory.txt if it is open elsewhere and try again.")
    except Exception as e:
        print("An unexpected error occurred while reading:", e)


def capture_shoes():
    """
    Allows a user to capture data about a shoe, creates a Shoe object,
    and appends it to shoes_list. Saves to file afterwards.
    """
    print("\n=== Capture New Shoe ===\n")
    country = input("Enter country: ").strip()
    code = input("Enter code: ").strip()
    product = input("Enter product: ").strip()

    # Defensive: cost input
    while True:
        try:
            cost = float(input("Enter cost: ").strip())
            if cost < 0:
                print("Cost cannot be negative. Try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number for cost.")

    # Defensive: quantity input
    while True:
        try:
            quantity = int(input("Enter quantity: ").strip())
            if quantity < 0:
                print("Quantity cannot be negative. Try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a whole number for quantity.")

    new_shoe = Shoe(country, code, product, cost, quantity)
    shoes_list.append(new_shoe)

    write_shoes_data()
    print("\nShoe added and saved.")


def view_all():
    """
    Iterates over shoes_list and prints details in a table using tabulate.
    (Optional in the task brief: table formatting using tabulate.)
    """
    print("\n=== View All Shoes ===\n")
    if not shoes_list:
        print("No shoes loaded. (Check inventory.txt or load data.)")
        return

    table_data = []
    for shoe in shoes_list:
        table_data.append([shoe.country, shoe.code, shoe.product, shoe.cost, shoe.quantity])

    headers = ["Country", "Code", "Product", "Cost", "Quantity"]
    print(tabulate(table_data, headers=headers, tablefmt="grid"))


def re_stock():
    """
    Finds the shoe object with the lowest quantity, asks user if they want
    to add quantity, updates it, and writes changes back to file.
    """
    print("\n=== Restock Lowest Quantity Item ===\n")
    if not shoes_list:
        print("No shoes loaded.")
        return

    lowest_shoe = min(shoes_list, key=lambda s: s.quantity)
    print("Lowest stock item found:\n")
    print(lowest_shoe)

    choice = input("Do you want to restock this item? (y/n): \n").strip().lower()
    if choice != "y":
        print("Restock cancelled.\n")
        return

    while True:
        try:
            add_qty = int(input("Enter quantity to add: ").strip())
            if add_qty < 0:
                print("Quantity to add cannot be negative. Try again.\n")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a whole number.\n")

    lowest_shoe.quantity += add_qty
    write_shoes_data()

    print("Restock complete and file updated.\n")
    print("Updated item:\n")
    print(lowest_shoe)


def search_shoe():
    """
    Searches for a shoe from the list using the shoe code and prints it.
    Returns the found Shoe object or None.
    """
    print("\n=== Search Shoe by Code ===\n")
    if not shoes_list:
        print("No shoes loaded.")
        return None

    search_code = input("Enter shoe code: ").strip()
    for shoe in shoes_list:
        if shoe.code == search_code:
            print("Shoe found:")
            print(shoe)
            return shoe

    print("\nShoe not found.\n")
    return None


def value_per_item():
    """
    Calculates the total value for each item (value = cost * quantity)
    and prints it for all shoes.
    """
    print("\n=== Value Per Item ===\n")
    if not shoes_list:
        print("No shoes loaded.")
        return

    for shoe in shoes_list:
        value = shoe.cost * shoe.quantity
        print(f" {shoe.product} | {shoe.code} | Value: {value}")


def highest_qty():
    """
    Determines the product with the highest quantity and prints it as being for sale.
    """
    print("\n=== Highest Quantity Item (For Sale) ===\n")
    if not shoes_list:
        print("No shoes loaded.")
        return

    highest_shoe = max(shoes_list, key=lambda s: s.quantity)
    print("Item with highest quantity (FOR SALE):\n")
    print(highest_shoe)


# ========= Main Menu ==========
def main():
    # Load data on startup
    read_shoes_data()

    while True:
        print(
            """
=============================
      NIKE INVENTORY MENU
=============================
1. View all shoes
2. Capture new shoe
3. Search shoe by code
4. Restock (lowest quantity)
5. Value per item
6. Highest quantity (for sale)
7. Reload data from file
8. Exit
"""
        )

        choice = input("Enter your choice (1-8): ").strip()

        if choice == "1":
            view_all()
        elif choice == "2":
            capture_shoes()
        elif choice == "3":
            search_shoe()
        elif choice == "4":
            re_stock()
        elif choice == "5":
            value_per_item()
        elif choice == "6":
            highest_qty()
        elif choice == "7":
            read_shoes_data()
            print("Data reloaded.")
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 8.")


if __name__ == "__main__":
    main()