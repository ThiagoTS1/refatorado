from item_types import Item, ItemUpdaterFactory


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            updater = ItemUpdaterFactory.create_updater(item.name)
            updater.update_quality(item)
            updater.update_sell_in(item)
