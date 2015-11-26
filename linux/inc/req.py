import urllib2


def curllib(req, params=None,postdata=None):
	headers = { 'User-agent': 'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36' }
	req = urllib2.Request(req+"?%s" % params, postdata, headers)
	try:
		req = urllib2.urlopen(req).read()
	except:
		req = "Error"
	return req

def aolvurl(req, params=None,postdata=None):
	headers = { 'User-agent': 'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36', 'Cookie': 'clickstreamid=-8575527164706151835; s_guid=\"2ccc223aa1814ab9bbbbe5e9cbe48215:041115\"; MVT_TBP=f1|669|20151104|20151104; MVT_TBV=f1|354; rs_timezone=-28800000; s_sess=%20s_cc%3Dtrue%3B%20s_sq%3D%3B; s_vi=[CS]v1|2B1CDCDC0530D65A-4000030480034A2A[CE]; UNAUTHID=1.7baed75cd11c466fab344328a71a8882.9906; CUNAUTHID=1.7baed75cd11c466fab344328a71a8882.9906; s_pers=%20s_fid%3D2B87641D76680375-16D221884D066511%7C1509778513595%3B%20s_getnr%3D1446623713602-New%7C1509695713602%3B%20s_nrgvo%3DNew%7C1509695713604%3B', 'Referer': 'http://search.aol.com/aol/search?s_it=topsearchbox.search&v_t=na&q=wp-content', 'Upgrade-Insecure-Requests': 1}
	req = urllib2.Request(req+"?%s" % params, postdata, headers)
	
	try:
		req = urllib2.urlopen(req).read()
	except:
		req = "Error"
	
	return req
