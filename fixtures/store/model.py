from typing import List

import attr


@attr.s
class StoreResponse:
    name: str = attr.ib()
    items: List[str] = attr.ib()
