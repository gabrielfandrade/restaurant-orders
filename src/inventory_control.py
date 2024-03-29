class InventoryControl:
    INGREDIENTS = {
        'hamburguer': ['pao', 'carne', 'queijo'],
        'pizza': ['massa', 'queijo', 'molho'],
        'misto-quente': ['pao', 'queijo', 'presunto'],
        'coxinha': ['massa', 'frango'],
    }
    MINIMUM_INVENTORY = {
        'pao': 50,
        'carne': 50,
        'queijo': 100,
        'molho': 50,
        'presunto': 50,
        'massa': 50,
        'frango': 50,
    }

    def __init__(self):
        self.orders = list()

        self.inventory = {
            'pao': 0,
            'carne': 0,
            'queijo': 0,
            'molho': 0,
            'presunto': 0,
            'massa': 0,
            'frango': 0,
        }

    def add_new_order(self, customer, order, day):
        new_order = [customer, order, day]

        inventory = self.inventory

        for ingredient in self.INGREDIENTS[order]:
            if self.inventory[ingredient] < self.MINIMUM_INVENTORY[ingredient]:
                inventory[ingredient] += 1
            else:
                return False

        self.inventory = inventory

        self.orders.append(new_order)

    def get_quantities_to_buy(self):
        return self.inventory

    def get_available_dishes(self):
        available_dishes = set()

        for dish, ingredients in self.INGREDIENTS.items():
            available = True

            for i in ingredients:
                if self.inventory[i] < self.MINIMUM_INVENTORY[i]:
                    continue
                else:
                    available = False
                    break

            if available:
                available_dishes.add(dish)

        return available_dishes
