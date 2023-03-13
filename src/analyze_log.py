import csv


def analyze_log(path_to_file: str):
    orders = csv_importer(path_to_file)

    maria_eats = eats(orders, 'maria')

    arnaldo_ask_hamburguer = ask_hamburguer(orders, 'arnaldo')

    joao_never_ask = never_ask(orders, 'joao')

    joao_never_went = never_went(orders, 'joao')

    logs = [
        maria_eats,
        arnaldo_ask_hamburguer,
        joao_never_ask,
        joao_never_went
    ]

    txt_write(logs)


def csv_importer(path_to_file: str):
    if not path_to_file.endswith('.csv'):
        raise FileNotFoundError(f'Extensão inválida: {path_to_file}')
    else:
        try:
            with open(path_to_file) as file:
                reader = csv.reader(file, delimiter=",", quotechar='"')

                _, *data = reader

                orders = list()

                for order in data:
                    order_dict = dict()

                    order_dict['client'] = order[0]
                    order_dict['item'] = order[1]
                    order_dict['day'] = order[2]

                    orders.append(order_dict)

                return orders
        except FileNotFoundError:
            raise FileNotFoundError(f'Arquivo inexistente: {path_to_file}')


def eats(orders: list, client: str):
    items = items_ordered(orders, client)

    most_eat = max(items, key=items.get)

    return most_eat


def ask_hamburguer(orders: list, client: str):
    items = items_ordered(orders, client)

    hamburguer = items['hamburguer']

    return hamburguer


def never_ask(orders: list, client: str):
    orders_filtered = list(filter(
        lambda order: order['client'] == client, orders))

    menu = set()

    for order in orders:
        menu.add(order['item'])

    for client_order in orders_filtered:
        menu.discard(client_order['item'])

    return menu


def never_went(orders: list, client: str):
    orders_filtered = list(filter(
        lambda order: order['client'] == client, orders))

    days = set()

    for order in orders:
        days.add(order['day'])

    for client_order in orders_filtered:
        days.discard(client_order['day'])

    return days


def items_ordered(orders: list, client: str):
    orders_filtered = list(filter(
        lambda order: order['client'] == client, orders))

    items_ordered = dict()

    for order in orders_filtered:
        if order['item'] in items_ordered:
            items_ordered[order['item']] += 1
        else:
            items_ordered[order['item']] = 1

    return items_ordered


def txt_write(logs):
    file = open('data/mkt_campaign.txt', 'w')

    for line in logs:
        file.write(f'{line}\n')

    file.close()
