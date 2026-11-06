import unittest

from inventory.stock import Inventory


class InventoryTest(unittest.TestCase):
    def test_add_accumulates(self):
        stock = Inventory()
        stock.add("apple", 3)
        self.assertEqual(stock.add("apple", 2), 5)

    def test_remove_reduces_quantity(self):
        stock = Inventory({"apple": 5})
        self.assertEqual(stock.remove("apple", 2), 3)

    def test_quantities_must_be_positive(self):
        stock = Inventory()
        with self.assertRaises(ValueError):
            stock.add("apple", 0)
        with self.assertRaises(ValueError):
            stock.remove("apple", -1)

    def test_total_value(self):
        stock = Inventory({"apple": 2, "pear": 1})
        self.assertAlmostEqual(stock.total_value({"apple": 0.5, "pear": 1.25}), 2.25)

    def test_low_stock(self):
        stock = Inventory({"apple": 1, "pear": 10, "fig": 0})
        self.assertEqual(stock.low_stock(5), ["apple", "fig"])
        self.assertEqual(stock.low_stock(threshold=5), ["apple", "fig"])

    def test_low_stock_only_returns_the_requested_skus(self):
        stock = Inventory({"apple": 1, "pear": 2, "fig": 0, "plum": 9})
        self.assertEqual(stock.low_stock(5, ["apple", "pear"]), ["apple", "pear"])
        self.assertEqual(stock.low_stock(5, ["plum"]), [])
        self.assertEqual(stock.low_stock(5, ["apple", "plum"]), ["apple"])

    def test_low_stock_unknown_skus_count_as_zero(self):
        stock = Inventory({"apple": 1, "pear": 10})
        self.assertEqual(stock.low_stock(5, ["pear", "kiwi"]), ["kiwi"])
        # A requested SKU the ledger never saw is below any positive threshold.
        self.assertEqual(stock.low_stock(1, ["unknown"]), ["unknown"])
        self.assertEqual(stock.low_stock(0, ["unknown"]), [])

    def test_low_stock_threshold_is_exclusive(self):
        stock = Inventory({"apple": 4, "pear": 5, "fig": 6})
        self.assertEqual(stock.low_stock(5), ["apple"])
        self.assertEqual(stock.low_stock(5, ["apple", "pear", "fig"]), ["apple"])

    def test_low_stock_skus_are_sorted_and_deduplicated(self):
        stock = Inventory({"apple": 1, "fig": 0, "pear": 10})
        self.assertEqual(
            stock.low_stock(5, ["fig", "apple", "fig", "pear", "apple"]),
            ["apple", "fig"],
        )

    def test_low_stock_skus_accepts_any_iterable(self):
        stock = Inventory({"apple": 1, "pear": 10})
        self.assertEqual(stock.low_stock(5, {"apple", "pear"}), ["apple"])
        self.assertEqual(stock.low_stock(5, iter(["apple"])), ["apple"])
        self.assertEqual(stock.low_stock(5, ("apple",)), ["apple"])
        self.assertEqual(stock.low_stock(5, []), [])

    def test_low_stock_single_sku_as_string(self):
        stock = Inventory({"apple": 1, "pear": 10})
        self.assertEqual(stock.low_stock(5, "apple"), ["apple"])
        self.assertEqual(stock.low_stock(5, "pear"), [])
        self.assertEqual(stock.low_stock(5, "kiwi"), ["kiwi"])


if __name__ == "__main__":
    unittest.main()
