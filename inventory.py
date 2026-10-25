
from datetime import datetime
from models import Book, Magazine, DigitalMedia


class InventoryManager:
    def __init__(self):
        self.__items = {}
        self.__audit_log = []

    def add_item(self, item):
        if item.item_id in self.__items:
            raise ValueError("An item with this ID already exists.")

        self.__items[item.item_id] = item
        self.__record_action("ADD", item, "Item added to inventory")

    def get_item(self, item_id):
        item = self.__items.get(item_id)

        if item is None:
            raise ValueError("Item ID not found.")

        return item

    def display_inventory(self):
        if not self.__items:
            print("\nInventory is empty.")
            return

        print("\n" + "=" * 85)
        print(f"{'ID':<10}{'TITLE':<25}{'TYPE':<18}{'PRICE':>10}{'STATUS':>15}")
        print("=" * 85)

        for item in self.__items.values():
            item_type = type(item).__name__
            print(
                f"{item.item_id:<10}"
                f"{item.title[:24]:<25}"
                f"{item_type:<18}"
                f"{item.price:>10.2f}"
                f"{'Checked Out' if item.is_checked_out else 'Available':>15}"
            )

        print("=" * 85)

    def checkout_item(self, item_id):
        item = self.get_item(item_id)
        item.checkout()
        self.__record_action("CHECKOUT", item, "Item checked out")
        print(f"Successfully checked out: {item.title}")

    def return_item(self, item_id, days=1):
        item = self.get_item(item_id)
        fee = item.calculate_fee(days)
        item.return_item()
        self.__record_action(
            "RETURN", item, f"Item returned; fee: Rs. {fee:.2f}"
        )
        print(f"Successfully returned: {item.title}")
        print(f"Fee for {days} day(s): Rs. {fee:.2f}")

    def __record_action(self, action, item, details):
        self.__audit_log.append({
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "action": action,
            "item_id": item.item_id,
            "title": item.title,
            "details": details
        })

    def display_audit_report(self):
        if not self.__audit_log:
            print("\nNo audit records available.")
            return

        print("\n" + "=" * 105)
        print(f"{'TIME':<20}{'ACTION':<12}{'ID':<10}{'TITLE':<25}{'DETAILS'}")
        print("=" * 105)

        for record in self.__audit_log:
            print(
                f"{record['time']:<20}"
                f"{record['action']:<12}"
                f"{record['item_id']:<10}"
                f"{record['title'][:24]:<25}"
                f"{record['details']}"
            )

        print("=" * 105)


def create_sample_inventory():
    inventory = InventoryManager()

    inventory.add_item(
        Book("B101", "Python Basics", 450, "John Smith", 250)
    )
    inventory.add_item(
        Magazine("M101", "Technology Today", 120, 12)
    )
    inventory.add_item(
        DigitalMedia("D101", "Python Tutorial", 200, "MP4", 500)
    )

    return inventory


def main():
    inventory = create_sample_inventory()

    while True:
        print("\n===== SMART INVENTORY SYSTEM =====")
        print("1. Display inventory")
        print("2. Check out item")
        print("3. Return item")
        print("4. Display audit report")
        print("5. Display item details and fee")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        try:
            if choice == "1":
                inventory.display_inventory()

            elif choice == "2":
                item_id = input("Enter item ID: ").strip()
                inventory.checkout_item(item_id)

            elif choice == "3":
                item_id = input("Enter item ID: ").strip()
                days = int(input("Enter number of days: "))

                if days < 0:
                    print("Days cannot be negative.")
                    continue

                inventory.return_item(item_id, days)

            elif choice == "4":
                inventory.display_audit_report()

            elif choice == "5":
                item_id = input("Enter item ID: ").strip()
                item = inventory.get_item(item_id)

                print("\nItem:", item)
                print("Representation:", repr(item))
                print("Title length:", len(item))
                print("Details:", item.display_metadata())
                print("Fee for 3 days: Rs.", f"{item.calculate_fee(3):.2f}")

            elif choice == "6":
                print("Thank you for using the Smart Inventory System!")
                break

            else:
                print("Invalid choice. Please enter a number from 1 to 6.")

        except ValueError as error:
            print("Error:", error)


if __name__ == "__main__":
    main()
