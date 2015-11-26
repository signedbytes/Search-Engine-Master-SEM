import sys
import os
import time

import aol, ask, bing, dogp, entirwebs, google, ixquick, req, yahoo, sout


def search( q, start=0, p=0):
	try:
		seout = google.googsearch(q,start*8)
		seout = seout + bing.bingsearch(q,start*8)
		seout = seout + yahoo.yahoosearc(q,start+1)
		seout = seout + ask.asksearche(q,start+1)
		seout = seout + ixquick.ixquick(q,start+1)
		seout = seout + dogp.dogpsearch(q,start*10)
		seout = seout + entirwebs.entirewebs(q,start*20+1)
		seout = seout + aol.aolsearche(q,start+1)
	except (KeyboardInterrupt, SystemExit):
		print("\r\n\033[31mExited... bye!")
		exit()

	if len(seout) != 0 :
		sout.done("\r\033[92m[+]:\033[0m Exteracting \033[92m #%s \033[32mPage Done!\033[0m         " %str(start+1) )
	return seout;
