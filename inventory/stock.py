"""A small in-memory stock ledger used by the warehouse scripts."""

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
        current = self.quantities.get(sku, 0)
        if quantity > current:
            raise ValueError(f"cannot ship {quantity} of {sku}: only {current} on hand")
        self.quantities[sku] = current - quantity
        return self.quantities[sku]

    def total_value(self, prices: dict[str, float]) -> float:
        """Value of everything on hand at the given unit prices."""
        return sum(quantity * prices[sku] for sku, quantity in self.quantities.items())

    def low_stock(self, threshold: int) -> list[str]:
        """SKUs whose quantity is below `threshold`, sorted by SKU."""
        return sorted(sku for sku, quantity in self.quantities.items() if quantity < threshold)
