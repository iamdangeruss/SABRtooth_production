from django.contrib import admin
from SABR.models import Technologies, TeamLogos, Master

class TechnologiesAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'url')
    
class TeamLogosAdmin(admin.ModelAdmin):
    list_display = ('teamid', 'image', 'startyear','endyear')    

class MasterAdmin(admin.ModelAdmin):
    list_display = ('playerid', 'namefirst', 'namelast')
    search_fields = ['playerid', 'namefirst', 'namelast']     	

admin.site.register(Technologies,TechnologiesAdmin)
admin.site.register(TeamLogos,TeamLogosAdmin)
admin.site.register(Master,MasterAdmin)
