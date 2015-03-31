from selectable.base import ModelLookup
from selectable.registry import registry
from SABR.models import Master



    
class MasterLookup(ModelLookup):
    model = Master
    search_field = 'playerid__icontains'
   
   
	
registry.register(MasterLookup)