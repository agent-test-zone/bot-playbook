"""A small in-memory stock ledger used by the warehouse scripts."""

from collections.abc import Iterable
from dataclasses import dataclass, field


@dataclass
class Inventory:
    """Quantities on hand, keyed by SKU."""

    quantities: dict[str, int] = field(default_factory=dict)

    def add(self, sku: str, quantity: int) -> int:
        """Receive `quantity` units of `sku` and return the new quantity."""
        if quantity <= 0:
            raise ValueError("quantity must be positive")
        self.quantities[sku] = self.quantities.get(sku, 0) + quantity
        return self.quantities[sku]

    def remove(self, sku: str, quantity: int) -> int:
        """Ship `quantity` units of `sku` and return the new quantity."""
        if quantity <= 0:
            raise ValueError("quantity must be positive")
        self.quantities[sku] = self.quantities.get(sku, 0) - quantity
        return self.quantities[sku]

    def total_value(self, prices: dict[str, float]) -> float:
        """Value of everything on hand at the given unit prices."""
        return sum(quantity * prices[sku] for sku, quantity in self.quantities.items())

    def low_stock(self, threshold: int, skus: Iterable[str] | None = None) -> list[str]:
        """SKUs whose quantity is below `threshold`, sorted by SKU, one entry each.

        When `skus` is given, only those SKUs are considered; a SKU that is not
        on the ledger counts as quantity 0. A single SKU may be passed as a
        string instead of an iterable of strings.
        """
        if skus is None:
            return sorted(sku for sku, quantity in self.quantities.items() if quantity < threshold)
        if isinstance(skus, str):
            skus = [skus]
        return sorted(sku for sku in set(skus) if self.quantities.get(sku, 0) < threshold)
