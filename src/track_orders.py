class TrackOrders:
    # aqui deve expor a quantidade de estoque
    def __len__(self):
        if hasattr(self, 'orders'):
            return len(self.orders)
        else:
            return 0

    def add_new_order(self, customer, order, day):
        order = [customer, order, day]

        if hasattr(self, 'orders'):
            self.orders.append(order)
        else:
            self.orders = [order]

    def get_most_ordered_dish_per_customer(self, customer):
        customer_orders = list(filter(
            lambda order: order[0] == customer, self.orders))

        dishes = dict()

        for order in customer_orders:
            if order[1] in dishes:
                dishes[order[1]] += 1
            else:
                dishes[order[1]] = 1

        most_ordered = max(dishes, key=dishes.get)

        return most_ordered

    def get_never_ordered_per_customer(self, customer):
        customer_orders = list(filter(
            lambda order: order[0] == customer, self.orders))

        menu = set()

        for order in self.orders:
            menu.add(order[1])

        for customer_order in customer_orders:
            menu.discard(customer_order[1])

        return menu

    def get_days_never_visited_per_customer(self, customer):
        customer_orders = list(filter(
            lambda order: order[0] == customer, self.orders))

        days = set()

        for order in self.orders:
            days.add(order[2])

        for customer_order in customer_orders:
            days.discard(customer_order[2])

        return days

    def get_busiest_day(self):
        days = dict()

        for order in self.orders:
            if order[2] in days:
                days[order[2]] += 1
            else:
                days[order[2]] = 1

        busiest_day = max(days, key=days.get)

        return busiest_day

    def get_least_busy_day(self):
        days = dict()

        for order in self.orders:
            if order[2] in days:
                days[order[2]] += 1
            else:
                days[order[2]] = 1

        least_busy_day = min(days, key=days.get)

        return least_busy_day
