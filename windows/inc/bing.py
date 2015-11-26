import urllib, req, re, sout

def bingsearch(query, start=0):
	sout.write("Exteracting 25% Bing ...        ")
	p = urllib.urlencode({'q' : query, 'first' : start })
	s = req.curllib("http://www.bing.com/search", p)

	if s != "Error":
		s = re.findall('<li class="b_algo"><h2><a href="(.*?)" ',s)
	
		return s
	else:
		sout.write("\033[31mError connecting to Bing!	\033[0m")
		return []
