import urllib, req, re, sout, time


def googsearch(query,start=0,rnum=8):
	sout.write("Exteracting 12.5% Google ...        ")
	result = []
	p = urllib.urlencode({'callback':'google.search.WebSearch.RawCompletion', 'rsz' : rnum,'hl':'en','source':'gsc','gss':'.com','sig':'432dd570d1a386253361f581254f9ca1', 'q':query,'start':start,'gl':'www.google.com','oq':query, 'gs_l':'partner.12...0.0.1.7160.0.0.0.0.0.0.0.0..0.0.gsnos%2Cn%3D13...0.0..1ac..25.partner..0.0.0.', 'qid':'1506e6c76391e584b', 'context':1,'key':'notsupplied', 'v':'1.0', 'nocache':'1444961600505'})
	s = req.curllib("http://www.google.com/uds/GwebSearch?", p)	

	if s != "Error":
		if "Suspected Terms" in s:

			sout.stopwatch("\033[31m"+"[+]:"+"\033[0m"+" Banded!, Bypassing... ",30)
			s = req.curllib("http://www.google.com/uds/GwebSearch?", p)
		if "Suspected Terms" in s:
			return []

		s = re.findall('","url":"(.*?)"', s)

		return result
	else:
		sout.write("\033[31mError connecting to Google!	\033[0m")
		return []
