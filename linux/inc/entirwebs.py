import urllib, req, re, time, sout


def entirewebs(query, start=0):
	sout.write("Exteracting 87.5% Entireweb ...        ")
	p = urllib.urlencode({'q':query, 'of':start, 'ts':time.time(),'md':'web', 'gs':'6YgT4Egb8uJkH'})
	s = req.curllib("http://www.entireweb.com/web/", p)
	if 'did not match' in s:
		p = urllib.urlencode({'q':query, 'of':start, 'ts':time.time(),'md':'web', 'gs':'6YgT4Egb8uJkH'})
		s = req.curllib("http://www.entireweb.com/web/", p)
	if s != "Error":
		p = re.compile('container"><a href="(.*?)">', re.UNICODE | re.IGNORECASE)
		s = re.findall(p, s)
	
		return s
	else:
		sout.write("\033[1;31mError connecting to Entireweb!	\033[0m")
		return []
