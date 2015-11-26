import urllib, req, re, sout

def dogpsearch(query, start=0):
	sout.write("Exteracting 75% Dogpile ...        ")
	p = urllib.urlencode({'qsi':start, 'q':query})
	s = req.curllib('http://www.dogpile.com/info.dogpl/search/web', p);
	
	if s != "Error" :
		s = re.findall(';ru=(.*?)&amp;ap=',s)
	
		for x in range(0,len(s)):
			s[x] = urllib.unquote(s[x])
	
		return s
	else:
		sout.write("\033[31mError connecting to Dogpile!	\033[0m")
		return []
