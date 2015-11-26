import re

def d(results=[], webappdir=[]):
	for x in range(0,len(results)):
		m = re.findall("|".join(webappdir), results[x])
		if m:	
			results[x] = results[x].split(m[0])
			results[x] = results[x][0]+"//"+results[x][2]+"/"
		else:
			m = False
	return results

def h(results=[], webappdir=[]):
	for x in range(0,len(results)):
		m = re.findall("|".join(webappdir), results[x])
		if m:	
			results[x] = results[x].split(m[0])
			results[x] = results[x][2]
		else:
			m = False
	return results
