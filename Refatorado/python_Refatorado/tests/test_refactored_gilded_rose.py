import unittest
from gilded_rose import Item, GildedRose


class TestRefactoredGildedRose(unittest.TestCase):

    def test_regular_item_quality_decreases_by_1(self):
        items = [Item("Regular Item", 10, 20)]
        gilded_rose = GildedRose(items)
        
        gilded_rose.update_quality()
        
        self.assertEqual(19, items[0].quality)
        self.assertEqual(9, items[0].sell_in)

    def test_regular_item_quality_decreases_by_2_after_sell_date(self):
        items = [Item("Regular Item", 0, 20)]
        gilded_rose = GildedRose(items)
        
        gilded_rose.update_quality()
        
        self.assertEqual(18, items[0].quality)
        self.assertEqual(-1, items[0].sell_in)

    def test_regular_item_quality_never_negative(self):
        items = [Item("Regular Item", 0, 0)]
        gilded_rose = GildedRose(items)
        
        gilded_rose.update_quality()
        
        self.assertEqual(0, items[0].quality)

    def test_aged_brie_quality_increases(self):
        items = [Item("Aged Brie", 10, 20)]
        gilded_rose = GildedRose(items)
        
        gilded_rose.update_quality()
        
        self.assertEqual(21, items[0].quality)
        self.assertEqual(9, items[0].sell_in)

    def test_aged_brie_quality_increases_by_2_after_sell_date(self):
        items = [Item("Aged Brie", 0, 20)]
        gilded_rose = GildedRose(items)
        
        gilded_rose.update_quality()
        
        self.assertEqual(22, items[0].quality)
        self.assertEqual(-1, items[0].sell_in)

    def test_aged_brie_quality_never_exceeds_50(self):
        items = [Item("Aged Brie", 10, 50)]
        gilded_rose = GildedRose(items)
        
        gilded_rose.update_quality()
        
        self.assertEqual(50, items[0].quality)

    def test_sulfuras_never_changes(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 10, 80)]
        gilded_rose = GildedRose(items)
        
        gilded_rose.update_quality()
        
        self.assertEqual(80, items[0].quality)
        self.assertEqual(10, items[0].sell_in)

    def test_backstage_pass_quality_increases_by_1_when_sell_in_greater_than_10(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 15, 20)]
        gilded_rose = GildedRose(items)
        
        gilded_rose.update_quality()
        
        self.assertEqual(21, items[0].quality)
        self.assertEqual(14, items[0].sell_in)

    def test_backstage_pass_quality_increases_by_2_when_sell_in_10_or_less(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 20)]
        gilded_rose = GildedRose(items)
        
        gilded_rose.update_quality()
        
        self.assertEqual(22, items[0].quality)
        self.assertEqual(9, items[0].sell_in)

    def test_backstage_pass_quality_increases_by_3_when_sell_in_5_or_less(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 20)]
        gilded_rose = GildedRose(items)
        
        gilded_rose.update_quality()
        
        self.assertEqual(23, items[0].quality)
        self.assertEqual(4, items[0].sell_in)

    def test_backstage_pass_quality_drops_to_0_after_concert(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 20)]
        gilded_rose = GildedRose(items)
        
        gilded_rose.update_quality()
        
        self.assertEqual(0, items[0].quality)
        self.assertEqual(-1, items[0].sell_in)

    def test_backstage_pass_quality_never_exceeds_50(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 49)]
        gilded_rose = GildedRose(items)
        
        gilded_rose.update_quality()
        
        self.assertEqual(50, items[0].quality)

    def test_conjured_item_quality_decreases_by_2(self):
        items = [Item("Conjured Mana Cake", 10, 20)]
        gilded_rose = GildedRose(items)
        
        gilded_rose.update_quality()
        
        self.assertEqual(18, items[0].quality)
        self.assertEqual(9, items[0].sell_in)

    def test_conjured_item_quality_decreases_by_4_after_sell_date(self):
        items = [Item("Conjured Mana Cake", 0, 20)]
        gilded_rose = GildedRose(items)
        
        gilded_rose.update_quality()
        
        self.assertEqual(16, items[0].quality)
        self.assertEqual(-1, items[0].sell_in)

    def test_conjured_item_quality_never_negative(self):
        items = [Item("Conjured Mana Cake", 0, 1)]
        gilded_rose = GildedRose(items)
        
        gilded_rose.update_quality()
        
        self.assertEqual(0, items[0].quality)

    def test_multiple_items_update_correctly(self):
        items = [
            Item("Regular Item", 10, 20),
            Item("Aged Brie", 10, 20),
            Item("Sulfuras, Hand of Ragnaros", 10, 80),
            Item("Backstage passes to a TAFKAL80ETC concert", 10, 20),
            Item("Conjured Mana Cake", 10, 20)
        ]
        gilded_rose = GildedRose(items)
        
        gilded_rose.update_quality()
        
        self.assertEqual(19, items[0].quality)
        self.assertEqual(9, items[0].sell_in)
        
        self.assertEqual(21, items[1].quality)
        self.assertEqual(9, items[1].sell_in)
        
        self.assertEqual(80, items[2].quality)
        self.assertEqual(10, items[2].sell_in)
        
        self.assertEqual(22, items[3].quality)
        self.assertEqual(9, items[3].sell_in)
        
        self.assertEqual(18, items[4].quality)
        self.assertEqual(9, items[4].sell_in)


if __name__ == '__main__':
    unittest.main()
