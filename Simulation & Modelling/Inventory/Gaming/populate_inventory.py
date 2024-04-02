from typing import Any
from Inventory.models import InventoryItems, DeliveryLocation
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def create_consoles(self):
        # create sample inventory items
        InventoryItems.objects.create(
            name='Nintendo Switch: Neon Blue Red Joy-Con',
            quantity= 143,
            price='KSH 47,000'
        )
        InventoryItems.objects.create(
            name='PlayStation 5: Digital Edition (Slim)',
            quantity= 487,
            price='KSH 74,799'
        )
        InventoryItems.objects.create(
            name='XBOX: Series S',
            quantity= 42,
            price='KSH 45,399'
        )
        InventoryItems.objects.create(
            name='XBOX: Series X',
            quantity= 66,
            price='KSH 89,500'
        )
        InventoryItems.objects.create(
            name='Nintendo Switch Oled',
            quantity= 212,
            price='KSH 53,500'
        )
    def create_games(self):
        InventoryItems.objects.create(
            name='Skulls & Bones (PS5)',
            quantity= 14,
            price='KES 8,400'
        )
        InventoryItems.objects.create(
            name='WWE 2K24 (XBOX)',
            quantity= 33,
            price='KES 6,850'
        )
        InventoryItems.objects.create(
            name='Marvel Spider-Man (PS5)',
            quantity= 73,
            price='KES 5,100'
        )
        InventoryItems.objects.create(
            name='Snufkin: Melody of Moonimvalley (Nintendo)',
            quantity= 6,
            price='KES 4,200'
        )
        InventoryItems.objects.create(
            name='Another Code - Recollection (Nintendo)',
            quantity= 6,
            price='KES 3,750'
        )
        InventoryItems.objects.create(
            name='Cyberpunk 2077: Phantom Liberty (XBOX)',
            quantity= 39,
            price='KES 7,300'
        )
    def create_locations(self):
        InventoryItems.objects.create(
            name='Embakasi'
        )
        InventoryItems.objects.create(
            name='Parklands'
        )
        
        InventoryItems.objects.create(
            name='Langata'
        )
        
        InventoryItems.objects.create(
            name='Doonholm'
        )
        InventoryItems.objects.create(
            name='South B'
        )
        InventoryItems.objects.create(
            name='Karen'
        )
        
    def handle(self, *args, **kwargs):
        self.create_consoles()
        self.create_games()
        self.create_location()
        self.stdout.write(self.style.SUCCESS('Data successfully populated'))