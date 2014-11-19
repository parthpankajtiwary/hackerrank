

def checkEnergy(botEnergy, buildingsHeight):
	building = 0
	for x in buildingsheight:
		if botEnergy < 0:
			return botEnergy
		if int(x) > building:
			botEnergy -= (int(x) - botEnergy)
			building = int(x)
		else:
			botEnergy += (botEnergy - int(x))
			building = int(x)
	return botEnergy		
      

n = int(raw_input())
buildingsheight = raw_input().split()
botEnergy = 0
while(checkEnergy(botEnergy, buildingsheight) < 0):
	botEnergy += 1
print botEnergy	
	
					
