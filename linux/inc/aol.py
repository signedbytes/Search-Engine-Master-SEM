import urllib, req, re, sout

def aolsearche(query, start=0):
	sout.write("Exteracting 100% Aol ...        ")

	p = urllib.urlencode({'s_it':'searchbox.webhome', 'v_t':'na', 'q':query, 'page': start})
	s = req.aolvurl("http://search.aol.com/aol/search", p)

	if s != "Error" :
		s = re.findall('    href="(.*?)" property="f:title"', s)
		
		return s
	else:
		sout.write("\033[1;31mError connecting to Aol!	\033[0m")
		return []
