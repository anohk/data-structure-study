"""
There is a small hotdog stand.
Each customer has their own patience (1~9).
The hotdog stand makes one hotdog per time unit.
Each customer’s patience is decreased by 1 per time unit.
If a customer’s patience is 0, he left the queue before next time unit starts.
Input : number of customers, series of customer’s patience. Output : the number of hotdogs sold.
"""
from .queue_adt import Queue


class Customer:
    def __init__(self, patience=0):
        self.patience = patience


class HotDogStand:
    def __init__(self):
        self.queue = Queue()

    def sell(self):
        pass


def get_number_of_hotdog(patience_list):
    hotdog_stand = HotDogStand()
    for idx, patience in enumerate(patience_list):
        customer = Customer(patience)
        hotdog_stand.queue.enqueue(customer)

        print('CUSTOMER {}: patience {}'.format(idx, patience))

    while hotdog_stand.queue.count > 0:
        hotdog_stand.sell()
