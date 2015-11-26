import urllib, req, re, sout

def asksearche(query,start=0):
	sout.write("Exteracting 50% Ask ...        ")
	p = urllib.urlencode({'q':query, 'qsrc':0, 'o':0, 'l':'dir', 'page':start})
	s = req.curllib("http://www.ask.com/web?", p)

	if s != "Error" :
		asks = re.findall('<a class="web-result-title-link" href="(.*?)"( target="_blank"| onmousedown=")',s)
		s = []
		for i in asks:
			s.append(i[0])
	
		return s
	else:
		sout.write("\033[31mError connecting to Ask!	\033[0m")
		return []
