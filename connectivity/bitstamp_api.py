import json

from connectivity import api
from connectivity.observable import Observable


class BitstampAPI(Observable):
    def __init__(self):
        super().__init__()
        self.credentials = json.load(open('../credentials.json', 'r'))
        self.c = self.credentials['CLIENT_ID']
        self.k = self.credentials['API_KEY']
        self.s = self.credentials['API_SECRET']

        print('CLIENT_ID  (truncated) = {}[...]'.format(self.c[0:3]))
        print('API_KEY    (truncated) = {}[...]'.format(self.k[0:10]))
        print('API_SECRET (truncated) = {}[...]'.format(self.s[0:10]))

        self.observers = []

    def buy_limit_order(self, amount, price):
        return api.buy_limit_order(self.c, self.k, self.s, amount, price)

    def api_cancel_order(self, order_id):
        return api.cancel_order(self.c, self.k, self.s, order_id)

    def sell_limit_order(self, amount, price):
        return api.sell_limit_order(self.c, self.k, self.s, amount, price)

    def last_transactions(self):
        return api.user_transactions(self.c, self.k, self.s)

    @staticmethod
    def order_book():
        return api.order_book()

    def account_balance(self):
        return api.account_balance(self.c, self.k, self.s)

    def open_orders(self):
        return api.open_orders(self.c, self.k, self.s)

    def poll(self):
        return {'key': 'price_update'}
