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

    def test_remove_more_than_stock_is_rejected(self):
        stock = Inventory({"apple": 2})
        with self.assertRaises(ValueError) as caught:
            stock.remove("apple", 5)
        self.assertEqual(str(caught.exception), "cannot ship 5 of apple: only 2 on hand")
        self.assertEqual(stock.quantities, {"apple": 2})

    def test_remove_unknown_sku_is_rejected(self):
        stock = Inventory({"apple": 2})
        with self.assertRaises(ValueError) as caught:
            stock.remove("pear", 1)
        self.assertEqual(str(caught.exception), "cannot ship 1 of pear: only 0 on hand")
        self.assertEqual(stock.quantities, {"apple": 2})

    def test_remove_exactly_all_stock(self):
        stock = Inventory({"apple": 2})
        self.assertEqual(stock.remove("apple", 2), 0)
        self.assertEqual(stock.quantities, {"apple": 0})

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


if __name__ == "__main__":
    unittest.main()
