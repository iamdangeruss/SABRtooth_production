from django.db import models
from django.contrib import admin

class TeamLogos(models.Model):
	teamid = models.CharField(max_length=3)
	image = models.ImageField(upload_to='teams', blank=True, null=True)
	startyear = models.IntegerField(blank=True, null=True)
	endyear = models.IntegerField(blank=True, null=True) 

class Master(models.Model):
    playerid = models.CharField(db_column='playerID', primary_key=True, max_length=10)  # Field name made lowercase.
    birthyear = models.IntegerField(db_column='birthYear', blank=True, null=True)  # Field name made lowercase.
    birthmonth = models.IntegerField(db_column='birthMonth', blank=True, null=True)  # Field name made lowercase.
    birthday = models.IntegerField(db_column='birthDay', blank=True, null=True)  # Field name made lowercase.
    birthcountry = models.CharField(db_column='birthCountry', max_length=50, blank=True)  # Field name made lowercase.
    birthstate = models.CharField(db_column='birthState', max_length=2, blank=True)  # Field name made lowercase.
    birthcity = models.CharField(db_column='birthCity', max_length=50, blank=True)  # Field name made lowercase.
    deathyear = models.IntegerField(db_column='deathYear', blank=True, null=True)  # Field name made lowercase.
    deathmonth = models.IntegerField(db_column='deathMonth', blank=True, null=True)  # Field name made lowercase.
    deathday = models.IntegerField(db_column='deathDay', blank=True, null=True)  # Field name made lowercase.
    deathcountry = models.CharField(db_column='deathCountry', max_length=50, blank=True)  # Field name made lowercase.
    deathstate = models.CharField(db_column='deathState', max_length=2, blank=True)  # Field name made lowercase.
    deathcity = models.CharField(db_column='deathCity', max_length=50, blank=True)  # Field name made lowercase.
    namefirst = models.CharField(db_column='nameFirst', max_length=50, blank=True)  # Field name made lowercase.
    namelast = models.CharField(db_column='nameLast', max_length=50, blank=True)  # Field name made lowercase.
    namegiven = models.CharField(db_column='nameGiven', max_length=255, blank=True)  # Field name made lowercase.
    weight = models.IntegerField(blank=True, null=True)
    height = models.FloatField(blank=True, null=True)
    bats = models.CharField(max_length=1, blank=True)
    throws = models.CharField(max_length=1, blank=True)
    debut = models.DateTimeField(blank=True, null=True)
    finalgame = models.DateTimeField(db_column='finalGame', blank=True, null=True)  # Field name made lowercase.
    retroid = models.CharField(db_column='retroID', max_length=9, blank=True)  # Field name made lowercase.
    bbrefid = models.CharField(db_column='bbrefID', max_length=9, blank=True)  # Field name made lowercase.
    player_fullname = models.CharField(max_length=50, blank=True)
    image = models.ImageField(upload_to='profile', blank=True, null=True)
    
    #reformat height in feet and inches
    def readheight(self):
    	feet = "{:.0f}".format(int(self.height / 12))
    	inches= "{:.0f}".format(self.height % 12)
    	return str(feet) + "'" + str(inches) +"''"
    
    

    def __str__(self):              
        return self.playerid
                
    
    class Meta:
        #managed = False
        db_table = 'Master'
        
class Teamsfranchises(models.Model):
    franchid = models.CharField(db_column='franchID', primary_key=True, max_length=3)  # Field name made lowercase.
    franchname = models.CharField(db_column='franchName', max_length=50, blank=True)  # Field name made lowercase.
    active = models.CharField(max_length=2, blank=True)
    naassoc = models.CharField(db_column='NAassoc', max_length=3, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TeamsFranchises'          
        
class Teams(models.Model):
    yearid = models.IntegerField(db_column='yearID')  # Field name made lowercase.
    lgid = models.CharField(db_column='lgID', max_length=2)  # Field name made lowercase.
    teamid = models.CharField(db_column='teamID', max_length=3)  # Field name made lowercase.
    #franchid = models.CharField(db_column='franchID', max_length=3, blank=True)  # Field name made lowercase.
    franchid = models.ForeignKey(Teamsfranchises)
    divid = models.CharField(db_column='divID', max_length=1, blank=True)  # Field name made lowercase.
    rank = models.IntegerField(db_column='Rank', blank=True, null=True)  # Field name made lowercase.
    g = models.IntegerField(db_column='G', blank=True, null=True)  # Field name made lowercase.
    ghome = models.IntegerField(db_column='Ghome', blank=True, null=True)  # Field name made lowercase.
    w = models.IntegerField(db_column='W', blank=True, null=True)  # Field name made lowercase.
    l = models.IntegerField(db_column='L', blank=True, null=True)  # Field name made lowercase.
    divwin = models.CharField(db_column='DivWin', max_length=1, blank=True)  # Field name made lowercase.
    wcwin = models.CharField(db_column='WCWin', max_length=1, blank=True)  # Field name made lowercase.
    lgwin = models.CharField(db_column='LgWin', max_length=1, blank=True)  # Field name made lowercase.
    wswin = models.CharField(db_column='WSWin', max_length=1, blank=True)  # Field name made lowercase.
    r = models.IntegerField(db_column='R', blank=True, null=True)  # Field name made lowercase.
    ab = models.IntegerField(db_column='AB', blank=True, null=True)  # Field name made lowercase.
    h = models.IntegerField(db_column='H', blank=True, null=True)  # Field name made lowercase.
    number_2b = models.IntegerField(db_column='2B', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3b = models.IntegerField(db_column='3B', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    hr = models.IntegerField(db_column='HR', blank=True, null=True)  # Field name made lowercase.
    bb = models.IntegerField(db_column='BB', blank=True, null=True)  # Field name made lowercase.
    so = models.IntegerField(db_column='SO', blank=True, null=True)  # Field name made lowercase.
    sb = models.IntegerField(db_column='SB', blank=True, null=True)  # Field name made lowercase.
    cs = models.IntegerField(db_column='CS', blank=True, null=True)  # Field name made lowercase.
    hbp = models.IntegerField(db_column='HBP', blank=True, null=True)  # Field name made lowercase.
    sf = models.IntegerField(db_column='SF', blank=True, null=True)  # Field name made lowercase.
    ra = models.IntegerField(db_column='RA', blank=True, null=True)  # Field name made lowercase.
    er = models.IntegerField(db_column='ER', blank=True, null=True)  # Field name made lowercase.
    era = models.FloatField(db_column='ERA', blank=True, null=True)  # Field name made lowercase.
    cg = models.IntegerField(db_column='CG', blank=True, null=True)  # Field name made lowercase.
    sho = models.IntegerField(db_column='SHO', blank=True, null=True)  # Field name made lowercase.
    sv = models.IntegerField(db_column='SV', blank=True, null=True)  # Field name made lowercase.
    ipouts = models.IntegerField(db_column='IPouts', blank=True, null=True)  # Field name made lowercase.
    ha = models.IntegerField(db_column='HA', blank=True, null=True)  # Field name made lowercase.
    hra = models.IntegerField(db_column='HRA', blank=True, null=True)  # Field name made lowercase.
    bba = models.IntegerField(db_column='BBA', blank=True, null=True)  # Field name made lowercase.
    soa = models.IntegerField(db_column='SOA', blank=True, null=True)  # Field name made lowercase.
    e = models.IntegerField(db_column='E', blank=True, null=True)  # Field name made lowercase.
    dp = models.IntegerField(db_column='DP', blank=True, null=True)  # Field name made lowercase.
    fp = models.FloatField(db_column='FP', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(max_length=50, blank=True)
    park = models.CharField(max_length=255, blank=True)
    attendance = models.IntegerField(blank=True, null=True)
    bpf = models.IntegerField(db_column='BPF', blank=True, null=True)  # Field name made lowercase.
    ppf = models.IntegerField(db_column='PPF', blank=True, null=True)  # Field name made lowercase.
    teamidbr = models.CharField(db_column='teamIDBR', max_length=3, blank=True)  # Field name made lowercase.
    teamidlahman45 = models.CharField(db_column='teamIDlahman45', max_length=3, blank=True)  # Field name made lowercase.
    teamidretro = models.CharField(db_column='teamIDretro', max_length=3, blank=True)  # Field name made lowercase.
    djangoid = models.IntegerField(db_column='djangoid', primary_key=True)

    class Meta:
        managed = False
        db_table = 'Teams'


       

class Batting(models.Model):
    playerid = models.ForeignKey(Master)  # Field name made lowercase.
    yearid = models.IntegerField(db_column='yearID')  # Field name made lowercase.
    stint = models.IntegerField()
    teamid = models.CharField(db_column='teamID', max_length=3, blank=True)  # Field name made lowercase.
    #teamid = models.ForeignKey(Teams)
    #teamid = models.ManyToManyField(Teams)
    #teamid2 = models.CharField(db_column='teamID', max_length=3, blank=True)  # Field name made lowercase.
    lgid = models.CharField(db_column='lgID', max_length=2, blank=True)  # Field name made lowercase.
    g = models.IntegerField(db_column='G', blank=True, null=True)  # Field name made lowercase.
    g_batting = models.IntegerField(db_column='G_batting', blank=True, null=True)  # Field name made lowercase.
    ab = models.IntegerField(db_column='AB', blank=True, null=True)  # Field name made lowercase.
    r = models.IntegerField(db_column='R', blank=True, null=True)  # Field name made lowercase.
    h = models.IntegerField(db_column='H', blank=True, null=True)  # Field name made lowercase.
    number_2b = models.IntegerField(db_column='2B', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3b = models.IntegerField(db_column='3B', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    hr = models.IntegerField(db_column='HR', blank=True, null=True)  # Field name made lowercase.
    rbi = models.IntegerField(db_column='RBI', blank=True, null=True)  # Field name made lowercase.
    sb = models.IntegerField(db_column='SB', blank=True, null=True)  # Field name made lowercase.
    cs = models.IntegerField(db_column='CS', blank=True, null=True)  # Field name made lowercase.
    bb = models.IntegerField(db_column='BB', blank=True, null=True)  # Field name made lowercase.
    so = models.IntegerField(db_column='SO', blank=True, null=True)  # Field name made lowercase.
    ibb = models.IntegerField(db_column='IBB', blank=True, null=True)  # Field name made lowercase.
    hbp = models.IntegerField(db_column='HBP', blank=True, null=True)  # Field name made lowercase.
    sh = models.IntegerField(db_column='SH', blank=True, null=True)  # Field name made lowercase.
    sf = models.IntegerField(db_column='SF', blank=True, null=True)  # Field name made lowercase.
    gidp = models.IntegerField(db_column='GIDP', blank=True, null=True)  # Field name made lowercase.
    g_old = models.IntegerField(db_column='G_old', blank=True, null=True)  # Field name made lowercase.
    djangoid = models.IntegerField(db_column='djangoid', primary_key=True)
    
    
    def teamlogo(self):
    	t = TeamLogos.objects.get(teamid=self.teamid, startyear__lte=self.yearid,endyear__gte=self.yearid)
    	return t.image
    	
    #build out SABRmetrics here (best practice to build in DB?)
    def netsteals(self):
    	return self.sb - self.cs
    	
    def ba(self):
    	if self.ab != 0 and self.ab is not None: 
    		return "{:.3f}".format(self.h / float(self.ab))
    		#return self.ab
    	else:
    		return "{:.3f}".format(.000)
    			
    		
    def obp(self):
        #OBP = (H + BB + HBP) / (AB + BB + HBP + SF)
        # some legacy stats dont have SF 
        
        if self.ab != 0 and self.ab is not None:
            if not self.sf:
                self.sf = 0
    	    return "{:.3f}".format((self.h + self.bb + self.hbp) / (float(self.ab) + self.bb + self.hbp + self.sf))	
    	else:
    		return "{:.3f}".format(.000)    
    
    def slg(self):	
    	
    	if self.ab != 0 and self.ab is not None:
    	    singles = self.h - self.number_2b - self.number_3b - self.hr
    	    return  "{:.3f}".format((singles + 2 * self.number_2b + 3 * self.number_3b + 4 * self.hr) / float(self.ab))
    	else:
    	    return "{:.3f}".format(.000)
    	    
    def ops(self):
        if self.ab != 0 and self.ab is not None:
            if not self.sf:
                self.sf = 0
    	
            obp =  (self.h + self.bb + self.hbp) / (float(self.ab) + self.bb + self.hbp + self.sf)
    	
            singles = self.h - self.number_2b - self.number_3b - self.hr
            slg =  (singles + 2 * self.number_2b + 3 * self.number_3b + 4 * self.hr) / float(self.ab)
    	
            return "{:.3f}".format(obp + slg)
    	else:
    	    return "{:.3f}".format(.000)

    def __str__(self):              
        return self.playerid
        
    class Meta:
        #managed = False
        db_table = 'Batting'
        
class Pitching(models.Model):
    playerid = models.ForeignKey(Master)   # Field name made lowercase.
    yearid = models.IntegerField(db_column='yearID')  # Field name made lowercase.
    stint = models.IntegerField()
    teamid = models.CharField(db_column='teamID', max_length=3, blank=True)  # Field name made lowercase.
    lgid = models.CharField(db_column='lgID', max_length=2, blank=True)  # Field name made lowercase.
    w = models.IntegerField(db_column='W', blank=True, null=True)  # Field name made lowercase.
    l = models.IntegerField(db_column='L', blank=True, null=True)  # Field name made lowercase.
    g = models.IntegerField(db_column='G', blank=True, null=True)  # Field name made lowercase.
    gs = models.IntegerField(db_column='GS', blank=True, null=True)  # Field name made lowercase.
    cg = models.IntegerField(db_column='CG', blank=True, null=True)  # Field name made lowercase.
    sho = models.IntegerField(db_column='SHO', blank=True, null=True)  # Field name made lowercase.
    sv = models.IntegerField(db_column='SV', blank=True, null=True)  # Field name made lowercase.
    ipouts = models.IntegerField(db_column='IPouts', blank=True, null=True)  # Field name made lowercase.
    h = models.IntegerField(db_column='H', blank=True, null=True)  # Field name made lowercase.
    er = models.IntegerField(db_column='ER', blank=True, null=True)  # Field name made lowercase.
    hr = models.IntegerField(db_column='HR', blank=True, null=True)  # Field name made lowercase.
    bb = models.IntegerField(db_column='BB', blank=True, null=True)  # Field name made lowercase.
    so = models.IntegerField(db_column='SO', blank=True, null=True)  # Field name made lowercase.
    baopp = models.FloatField(db_column='BAOpp', blank=True, null=True)  # Field name made lowercase.
    era = models.FloatField(db_column='ERA', blank=True, null=True)  # Field name made lowercase.
    ibb = models.IntegerField(db_column='IBB', blank=True, null=True)  # Field name made lowercase.
    wp = models.IntegerField(db_column='WP', blank=True, null=True)  # Field name made lowercase.
    hbp = models.IntegerField(db_column='HBP', blank=True, null=True)  # Field name made lowercase.
    bk = models.IntegerField(db_column='BK', blank=True, null=True)  # Field name made lowercase.
    bfp = models.IntegerField(db_column='BFP', blank=True, null=True)  # Field name made lowercase.
    gf = models.IntegerField(db_column='GF', blank=True, null=True)  # Field name made lowercase.
    r = models.IntegerField(db_column='R', blank=True, null=True)  # Field name made lowercase.
    sh = models.IntegerField(db_column='SH', blank=True, null=True)  # Field name made lowercase.
    sf = models.IntegerField(db_column='SF', blank=True, null=True)  # Field name made lowercase.
    gidp = models.IntegerField(db_column='GIDP', blank=True, null=True)  # Field name made lowercase.
    djangoid = models.IntegerField(db_column='djangoid', primary_key=True)

    def teamlogo(self):
    	t = TeamLogos.objects.get(teamid=self.teamid, startyear__lte=self.yearid,endyear__gte=self.yearid)
    	return t.image
    
    class Meta:
        managed = False
        db_table = 'Pitching'
        
class Fielding(models.Model):
    playerid = models.ForeignKey(Master)  # Field name made lowercase.
    yearid = models.IntegerField(db_column='yearID')  # Field name made lowercase.
    stint = models.IntegerField()
    teamid = models.CharField(db_column='teamID', max_length=3, blank=True)  # Field name made lowercase.
    lgid = models.CharField(db_column='lgID', max_length=2, blank=True)  # Field name made lowercase.
    pos = models.CharField(db_column='POS', max_length=2)  # Field name made lowercase.
    g = models.IntegerField(db_column='G', blank=True, null=True)  # Field name made lowercase.
    gs = models.IntegerField(db_column='GS', blank=True, null=True)  # Field name made lowercase.
    innouts = models.IntegerField(db_column='InnOuts', blank=True, null=True)  # Field name made lowercase.
    po = models.IntegerField(db_column='PO', blank=True, null=True)  # Field name made lowercase.
    a = models.IntegerField(db_column='A', blank=True, null=True)  # Field name made lowercase.
    e = models.IntegerField(db_column='E', blank=True, null=True)  # Field name made lowercase.
    dp = models.IntegerField(db_column='DP', blank=True, null=True)  # Field name made lowercase.
    pb = models.IntegerField(db_column='PB', blank=True, null=True)  # Field name made lowercase.
    wp = models.IntegerField(db_column='WP', blank=True, null=True)  # Field name made lowercase.
    sb = models.IntegerField(db_column='SB', blank=True, null=True)  # Field name made lowercase.
    cs = models.IntegerField(db_column='CS', blank=True, null=True)  # Field name made lowercase.
    zr = models.FloatField(db_column='ZR', blank=True, null=True)  # Field name made lowercase.
    djangoid = models.IntegerField(db_column='djangoid', primary_key=True)
    
    def teamlogo(self):
    	t = TeamLogos.objects.get(teamid=self.teamid, startyear__lte=self.yearid,endyear__gte=self.yearid)
    	return t.image

    class Meta:
        managed = False
        db_table = 'Fielding'
        
class Battingpost(models.Model):
    yearid = models.IntegerField(db_column='yearID')  # Field name made lowercase.
    round = models.CharField(max_length=10)
    playerid = models.ForeignKey(Master)  # Field name made lowercase.
    teamid = models.CharField(db_column='teamID', max_length=3, blank=True)  # Field name made lowercase.
    lgid = models.CharField(db_column='lgID', max_length=2, blank=True)  # Field name made lowercase.
    g = models.IntegerField(db_column='G', blank=True, null=True)  # Field name made lowercase.
    ab = models.IntegerField(db_column='AB', blank=True, null=True)  # Field name made lowercase.
    r = models.IntegerField(db_column='R', blank=True, null=True)  # Field name made lowercase.
    h = models.IntegerField(db_column='H', blank=True, null=True)  # Field name made lowercase.
    number_2b = models.IntegerField(db_column='2B', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3b = models.IntegerField(db_column='3B', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    hr = models.IntegerField(db_column='HR', blank=True, null=True)  # Field name made lowercase.
    rbi = models.IntegerField(db_column='RBI', blank=True, null=True)  # Field name made lowercase.
    sb = models.IntegerField(db_column='SB', blank=True, null=True)  # Field name made lowercase.
    cs = models.IntegerField(db_column='CS', blank=True, null=True)  # Field name made lowercase.
    bb = models.IntegerField(db_column='BB', blank=True, null=True)  # Field name made lowercase.
    so = models.IntegerField(db_column='SO', blank=True, null=True)  # Field name made lowercase.
    ibb = models.IntegerField(db_column='IBB', blank=True, null=True)  # Field name made lowercase.
    hbp = models.IntegerField(db_column='HBP', blank=True, null=True)  # Field name made lowercase.
    sh = models.IntegerField(db_column='SH', blank=True, null=True)  # Field name made lowercase.
    sf = models.IntegerField(db_column='SF', blank=True, null=True)  # Field name made lowercase.
    gidp = models.IntegerField(db_column='GIDP', blank=True, null=True)  # Field name made lowercase.
    djangoid = models.IntegerField(db_column='djangoid', primary_key=True)
    
    def teamlogo(self):
    	t = TeamLogos.objects.get(teamid=self.teamid, startyear__lte=self.yearid,endyear__gte=self.yearid)
    	return t.image
    
    def netsteals(self):
    	return self.sb - self.cs
    	
    def ba(self):
    	return "{:.3f}".format(self.h / float(self.ab))
    		
    def obp(self):
        #OBP = (H + BB + HBP) / (AB + BB + HBP + SF)
        # some legacy stats dont have SF 
        if not self.sf:
        	self.sf = 0
        if not self.hbp:
        	self.hbp = 0	
        	
    	return "{:.3f}".format((self.h + self.bb + self.hbp) / (float(self.ab) + self.bb + self.hbp + self.sf))	
    
    def slg(self):	
    	singles = self.h - self.number_2b - self.number_3b - self.hr
    	return  "{:.3f}".format((singles + 2 * self.number_2b + 3 * self.number_3b + 4 * self.hr) / float(self.ab))
    	
    def ops(self):
        if not self.sf:
            self.sf = 0
    	
        obp =  (self.h + self.bb + self.hbp) / (float(self.ab) + self.bb + self.hbp + self.sf)
    	
        singles = self.h - self.number_2b - self.number_3b - self.hr
        slg =  (singles + 2 * self.number_2b + 3 * self.number_3b + 4 * self.hr) / float(self.ab)
    	
        return "{:.3f}".format(obp + slg)

    class Meta:
        managed = False
        db_table = 'BattingPost'
        
class Fieldingpost(models.Model):
    playerid = models.ForeignKey(Master)  # Field name made lowercase..
    yearid = models.IntegerField(db_column='yearID')  # Field name made lowercase.
    teamid = models.CharField(db_column='teamID', max_length=3, blank=True)  # Field name made lowercase.
    lgid = models.CharField(db_column='lgID', max_length=2, blank=True)  # Field name made lowercase.
    round = models.CharField(max_length=10)
    pos = models.CharField(db_column='POS', max_length=2)  # Field name made lowercase.
    g = models.IntegerField(db_column='G', blank=True, null=True)  # Field name made lowercase.
    gs = models.IntegerField(db_column='GS', blank=True, null=True)  # Field name made lowercase.
    innouts = models.IntegerField(db_column='InnOuts', blank=True, null=True)  # Field name made lowercase.
    po = models.IntegerField(db_column='PO', blank=True, null=True)  # Field name made lowercase.
    a = models.IntegerField(db_column='A', blank=True, null=True)  # Field name made lowercase.
    e = models.IntegerField(db_column='E', blank=True, null=True)  # Field name made lowercase.
    dp = models.IntegerField(db_column='DP', blank=True, null=True)  # Field name made lowercase.
    tp = models.IntegerField(db_column='TP', blank=True, null=True)  # Field name made lowercase.
    pb = models.IntegerField(db_column='PB', blank=True, null=True)  # Field name made lowercase.
    sb = models.IntegerField(db_column='SB', blank=True, null=True)  # Field name made lowercase.
    cs = models.IntegerField(db_column='CS', blank=True, null=True)  # Field name made lowercase.
    djangoid = models.IntegerField(db_column='djangoid', primary_key=True)
    
    def teamlogo(self):
    	t = TeamLogos.objects.get(teamid=self.teamid, startyear__lte=self.yearid,endyear__gte=self.yearid)
    	return t.image

    class Meta:
        managed = False
        db_table = 'FieldingPost'
        
        
class Pitchingpost(models.Model):
    playerid = models.ForeignKey(Master)  # Field name made lowercase.
    yearid = models.IntegerField(db_column='yearID')  # Field name made lowercase.
    round = models.CharField(max_length=10)
    teamid = models.CharField(db_column='teamID', max_length=3, blank=True)  # Field name made lowercase.
    lgid = models.CharField(db_column='lgID', max_length=2, blank=True)  # Field name made lowercase.
    w = models.IntegerField(db_column='W', blank=True, null=True)  # Field name made lowercase.
    l = models.IntegerField(db_column='L', blank=True, null=True)  # Field name made lowercase.
    g = models.IntegerField(db_column='G', blank=True, null=True)  # Field name made lowercase.
    gs = models.IntegerField(db_column='GS', blank=True, null=True)  # Field name made lowercase.
    cg = models.IntegerField(db_column='CG', blank=True, null=True)  # Field name made lowercase.
    sho = models.IntegerField(db_column='SHO', blank=True, null=True)  # Field name made lowercase.
    sv = models.IntegerField(db_column='SV', blank=True, null=True)  # Field name made lowercase.
    ipouts = models.IntegerField(db_column='IPouts', blank=True, null=True)  # Field name made lowercase.
    h = models.IntegerField(db_column='H', blank=True, null=True)  # Field name made lowercase.
    er = models.IntegerField(db_column='ER', blank=True, null=True)  # Field name made lowercase.
    hr = models.IntegerField(db_column='HR', blank=True, null=True)  # Field name made lowercase.
    bb = models.IntegerField(db_column='BB', blank=True, null=True)  # Field name made lowercase.
    so = models.IntegerField(db_column='SO', blank=True, null=True)  # Field name made lowercase.
    baopp = models.FloatField(db_column='BAOpp', blank=True, null=True)  # Field name made lowercase.
    era = models.FloatField(db_column='ERA', blank=True, null=True)  # Field name made lowercase.
    ibb = models.IntegerField(db_column='IBB', blank=True, null=True)  # Field name made lowercase.
    wp = models.IntegerField(db_column='WP', blank=True, null=True)  # Field name made lowercase.
    hbp = models.IntegerField(db_column='HBP', blank=True, null=True)  # Field name made lowercase.
    bk = models.IntegerField(db_column='BK', blank=True, null=True)  # Field name made lowercase.
    bfp = models.IntegerField(db_column='BFP', blank=True, null=True)  # Field name made lowercase.
    gf = models.IntegerField(db_column='GF', blank=True, null=True)  # Field name made lowercase.
    r = models.IntegerField(db_column='R', blank=True, null=True)  # Field name made lowercase.
    sh = models.IntegerField(db_column='SH', blank=True, null=True)  # Field name made lowercase.
    sf = models.IntegerField(db_column='SF', blank=True, null=True)  # Field name made lowercase.
    gidp = models.IntegerField(db_column='GIDP', blank=True, null=True)  # Field name made lowercase.
    djangoid = models.IntegerField(db_column='djangoid', primary_key=True)
    
    def teamlogo(self):
    	t = TeamLogos.objects.get(teamid=self.teamid, startyear__lte=self.yearid,endyear__gte=self.yearid)
    	return t.image

    class Meta:
        managed = False
        db_table = 'PitchingPost'
        
             
                
class Technologies(models.Model):
	name = models.CharField(max_length=50)
	image = models.ImageField(upload_to='tech')
	description = models.CharField(max_length=255)
	url = models.URLField(max_length=200,blank=True, null=True)
	
