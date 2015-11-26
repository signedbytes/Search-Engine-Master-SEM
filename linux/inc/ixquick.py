import urllib, req, re, sout

def ixquick(query, start=0):
	sout.write("Exteracting 62.5% Ixquick ...        ")
	p = urllib.urlencode({'cmd':'process_search', 'language':'english', 'query':query, 'cat':'web', 'page_num':start})
	s = req.curllib("https://s3-us2.ixquick.com/do/search", p)
	if s != "Error" :
		s = re.findall("<h3 class='clk'><a href='(.*?)' id='title",s)
	
		return s
	else:
		sout.write("\033[1;31mError connecting to Ixquick!	\033[0m")
		return []
