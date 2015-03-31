from selectable.base import ModelLookup
from selectable.registry import registry

from sabr.models import Master


class FruitLookup(ModelLookup):
    model = Fruit
    search_field = 'name__icontains'
    
class PlayerLookup(ModelLookup)
	model = Master
	search_field = 'playerid__icontains'
	
registry.register(PlayerLookup)