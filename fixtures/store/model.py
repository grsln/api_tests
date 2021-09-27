from time import time
from typing import List

import attr


@attr.s
class StoreModel:
    name_store: str = attr.ib()

    @staticmethod
    def random():
        timestamp = int(time())
        name_store = f"store_{timestamp}"
        return StoreModel(name_store=name_store)


@attr.s
class StoreResponse:
    name: str = attr.ib()
    items: List[str] = attr.ib()
