from __future__ import annotations
from typing import TYPE_CHECKING, Dict, Any

if TYPE_CHECKING:
    from .client import QFEXTakerClient
    from .models import BBO


class TakerStrategy:
    """
    Users subclass this and override callbacks.
    """

    def __init__(self, client: "QFEXTakerClient"):
        self.client = client

    async def on_bbo(self, bbo: "BBO") -> None:
        raise NotImplementedError(
            "on_bbo() must be implemented in a TakerStrategy subclass"
        )

    async def on_trade(self, trade_msg: Dict[str, Any]) -> None:
        raise NotImplementedError(
            "on_trade() must be implemented in a TakerStrategy subclass"
        )

    async def on_fill(self, fill: Dict[str, Any]) -> None:
        """
        Called when we detect a fill delta for one of *your* orders.
        The payload will include:
          - order_response (raw)
          - filled_qty_delta (Decimal)
          - filled_notional_delta (Decimal)
        """
        raise NotImplementedError(
            "on_fill() must be implemented in a TakerStrategy subclass"
        )
