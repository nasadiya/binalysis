"""
Class to hold an asset object, properties and methods.
"""


class AssetObject:

    def __init__(self, client_object, asset_moniker):
        """
        :param client_object: Binance client object to access the account
        :param asset_moniker: moniker to identify the asset
        example - 'BTCUSD'
        """
        self.client = client_object
        self.asset_moniker = asset_moniker

    def server_time(self, server_time_moniker='serverTime'):
        return self.client.get_server_time()[server_time_moniker]

    def order_book(self):
        return self.client.get_order_book(symbol=self.asset_moniker)

    def averager_price(self, price_moniker='price'):
        return float(self.client.get_avg_price(symbol=self.asset_moniker)[
                         price_moniker])
1