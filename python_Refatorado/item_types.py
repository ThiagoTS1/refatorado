from abc import ABC, abstractmethod


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class ItemUpdater(ABC):
    
    @abstractmethod
    def update_quality(self, item):
        pass
    
    @abstractmethod
    def update_sell_in(self, item):
        pass
    
    def _clamp_quality(self, item, new_quality):
        item.quality = max(0, min(50, new_quality))


class RegularItemUpdater(ItemUpdater):
    
    def update_quality(self, item):
        if item.quality > 0:
            degradation = 2 if item.sell_in <= 0 else 1
            new_quality = item.quality - degradation
            self._clamp_quality(item, new_quality)
    
    def update_sell_in(self, item):
        item.sell_in -= 1


class AgedBrieUpdater(ItemUpdater):
    
    def update_quality(self, item):
        if item.quality < 50:
            improvement = 2 if item.sell_in <= 0 else 1
            new_quality = item.quality + improvement
            self._clamp_quality(item, new_quality)
    
    def update_sell_in(self, item):
        item.sell_in -= 1


class BackstagePassUpdater(ItemUpdater):
    
    def update_quality(self, item):
        if item.sell_in <= 0:
            item.quality = 0
        elif item.sell_in <= 5:
            new_quality = item.quality + 3
            self._clamp_quality(item, new_quality)
        elif item.sell_in <= 10:
            new_quality = item.quality + 2
            self._clamp_quality(item, new_quality)
        else:
            new_quality = item.quality + 1
            self._clamp_quality(item, new_quality)
    
    def update_sell_in(self, item):
        item.sell_in -= 1


class SulfurasUpdater(ItemUpdater):
    
    def update_quality(self, item):
        pass
    
    def update_sell_in(self, item):
        pass


class ConjuredItemUpdater(ItemUpdater):
    
    def update_quality(self, item):
        if item.quality > 0:
            degradation = 4 if item.sell_in <= 0 else 2
            new_quality = item.quality - degradation
            self._clamp_quality(item, new_quality)
    
    def update_sell_in(self, item):
        item.sell_in -= 1


class ItemUpdaterFactory:
    
    @staticmethod
    def create_updater(item_name):
        if item_name == "Aged Brie":
            return AgedBrieUpdater()
        elif item_name == "Backstage passes to a TAFKAL80ETC concert":
            return BackstagePassUpdater()
        elif item_name == "Sulfuras, Hand of Ragnaros":
            return SulfurasUpdater()
        elif item_name.startswith("Conjured"):
            return ConjuredItemUpdater()
        else:
            return RegularItemUpdater()
