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
        return self.client.time()[server_time_moniker]

    def order_book(self):
        return self.client.depth(symbol=self.asset_moniker)

    def ticker_price(self, price_moniker='price'):
        return float(self.client.ticker_price(symbol=self.asset_moniker)[
                         price_moniker])
1