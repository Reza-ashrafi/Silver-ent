import json

from collectors.tsetmc_client import TSETMCClient


class SymbolCollector:

    def __init__(self):
        self.client = TSETMCClient()

    def collect(self):

        url = (
            "https://cdn.tsetmc.com/api/Instrument/GetInstrumentInfo"
        )

        response = self.client.get(url)

        data = json.loads(response)

        return data
