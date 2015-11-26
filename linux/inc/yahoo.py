import urllib, req, re, sout

def yahoosearc(query,start=0):
	sout.write("Exteracting 37.5% Yahoo ...        ")
	p = urllib.urlencode({'p':query,'fr':'sfp', 'fr2':'sb-top-search', 'iscqry':'','b':3})
	s = req.curllib("https://search.yahoo.com/search?", p)	

	if s != "Error" and ("We did not find results" in s) == False:
		s = re.findall('" href="(https?:\/\/(?:www\.|(?!.*?\.yahoo\.com))[^\s\.]+\.[^\s]{2,}|www\.[^\s]+\.[^\s]{2,})" referrerpolicy=',s)
	
		return s
	else:
		if "We did not find results" in s:
			sout.write("\033[1;31mNo result from Yahoo!	\033[0m")
		else:
			sout.write("\033[1;31mError connecting to Yahoo!	\033[0m")
		return []
