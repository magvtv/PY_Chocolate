# Assuming you have a Django project with an app named 'inventory'

# models.py
from django.db import models

class InventoryItem(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

class DeliveryLocation(models.Model):
    name = models.CharField(max_length=100)

# inventory_management.py
from inventory.models import InventoryItem, DeliveryLocation

def check_inventory():
    items = InventoryItem.objects.all()
    for item in items:
        print(f"{item.name}: {item.quantity} available at {item.price} each")

def calculate_total_cost(item_name, quantity, location):
    item = InventoryItem.objects.get(name=item_name)
    total_cost = item.price * quantity
    # Additional logic for bulk purchase discount can be added here
    print(f"Total cost for {quantity} {item_name} to be delivered to {location}: {total_cost}")

def main():
    check_inventory()
    item_name = input("Enter the name of the item you need: ")
    quantity = int(input("Enter the quantity you need: "))
    location = input("Enter the delivery location: ")
    calculate_total_cost(item_name, quantity, location)

if __name__ == "__main__":
    main()
