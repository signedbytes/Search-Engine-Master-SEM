import sys, time

def uniq(lst):
    last = object()
    for item in lst:
        if item == last:
            continue
        yield item
        last = item

def sort_and_deduplicate(l):
    return list(uniq(sorted(l, reverse=False)))

def stopwatch( text, seconds ):
    start = time.time()
    time.clock()
    elapsed = 0
    while elapsed < seconds:
        elapsed = time.time() - start
        write(text+str(int(elapsed))+"s       ")
        
j = 0
def write(s):
	if "Exteracting" in s or "connecting" in s and ("Banded" in s) == False :
		global j
		e = ["/", '|', '\\', '|']

		pr = "\r\033[92m\033[1m["+e[j]+"]:\033[0m\033[0m "+s+""
		sys.stdout.write(pr)
		sys.stdout.flush()
		
		if j < 3:
			j = j+1
		else:
			j = 0
	else:
		if "Banded" in s:
			sys.stdout.write("\r"+s)
			sys.stdout.flush()
		else:
			sys.stdout.write("\r\033[92m\033[1m[+]:\033[0m\033[0m "+s+"")
			sys.stdout.flush()

def done(s):
	sys.stdout.write(s+"\r\n")
	sys.stdout.flush()
