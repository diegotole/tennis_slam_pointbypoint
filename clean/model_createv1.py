#model create

#schema


# server, p1 set, p2set,  p1 game, p2 game, p1 point, p2 point,   1st in-out ,   1st location, 2nd in-out, 2nd location,
# ace , dev dentro? ,quem terminou? (player id),forced, unforced, winner ,rede ou fundo?, direita ou esquerda?

fname = "sample1.csv"

model = {}

model["p1"] = ""
model["p2"] = ""
model["data"] = []


def pointWinner(obj):
	
	#return player id of point winner.  
	pass

def parseSet(obj):
	pass

def gameEnded(cols):
	
	#who won game
	#update set count
	#update game count
	pass

def skipLine(col):
	
	flag = False
	
	if(col[0] == ""):
		flag = True
		#print "game ended"
	
	elif(col[0] == "Server"):
		flag = True
		#print "header"
	
	
	
	return flag



def extractData(cols):
	
	global model
	#init p1
	name = cols[0].strip()
	if(model["p1"] == ""):
		model["p1"] = name
	
	player_id = 0
	
	if(model["p1"] ==  name  ):
		player_id = 1
	else:
		player_id = 2
		
		


with open(fname) as f:
	for line in f:
		
		rows = line.split("\r")
		print "row size: %s" % len(rows)
		for column in rows:
		
		
			col = column.split(",")
		
			if(skipLine(col)):
				continue
			
			
			