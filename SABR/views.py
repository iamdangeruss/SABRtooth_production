from django.shortcuts import render
from django.http import HttpResponse
from SABR.models import Master, Batting, Pitching, Fielding, Battingpost, Pitchingpost, Fieldingpost,Teamsfranchises,Teams,Technologies

from SABR.forms import MasterForm
import os.path
 

import json



def index(request):
    
    return render(request, 'sabr/index.html')
    
def about(request):
    
    techs = Technologies.objects.all()
    context_dict = {'techs':techs}
    
    return render(request, 'sabr/about.html',context_dict)    
    
def player(request, playerid):
    context_dict = {}
    
    
    player = Master.objects.get(playerid=playerid)
    batting_list = Batting.objects.filter(playerid=playerid)
    pitching_list = Pitching.objects.filter(playerid=playerid)
    fielding_list = Fielding.objects.filter(playerid=playerid)
    battingPost_list = Battingpost.objects.filter(playerid=playerid)
    fieldingPost_list = Fieldingpost.objects.filter(playerid=playerid)
    pitchingPost_list = Pitchingpost.objects.filter(playerid=playerid)
    
    
    
    
        
    context_dict = {'player': player,'battinglines': batting_list,'pitchinglines': pitching_list,'fieldinglines': fielding_list,'battingpostlines': battingPost_list,'fieldingpostlines': fieldingPost_list,'pitchingpostlines': pitchingPost_list}
    
    # Render the response and send it back!
    return render(request, 'sabr/player.html', context_dict)
    

    
    
def search(request):
    error = False
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        if not q:
            error = True
        else:
            players = Master.objects.filter(player_fullname__icontains=q) 
            return render(request, 'sabr/search_results.html',
                {'players': players, 'query': q})
    
    return render(request, 'sabr/search_form.html', {'error': error})  
    
# BAD!
def bad_search(request):
    # The following line will raise KeyError if 'q' hasn't
    # been submitted!
    message = 'You searched for: %r' % request.GET['q']
    return HttpResponse(message)          

def get_players(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        players = Master.objects.filter(player_fullname__icontains=q) [:20]
        results = []
        for player in players:
            if player.debut:
            	startyear = str(player.debut.year)
            else:
            	startyear = ""
            if player.finalgame:
            	endyear = str(player.finalgame.year)
            else:
            	endyear = ""		
            player_json = {}
            player_json['id'] = player.playerid
            player_json['label'] = player.player_fullname + " " + startyear + "-" + endyear
            player_json['value'] = "/sabr/player/"+ player.playerid
            results.append(player_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)    
    

    