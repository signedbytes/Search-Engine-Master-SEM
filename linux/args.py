import argparse

def bannerx():
	banner = """ _______   _______   \033[1;34m___ ___\033[0m                   \033[36m__\033[0m                  
 |   _   | |   _   | \033[1;34m|   Y   |\033[0m \033[1;31m.---.-.\033[0m \033[1;33m.-----.\033[0m \033[1;34m|  |_\033[0m  .-----. \033[1;31m.-.--.\033[0m
 |   1___| |.  1___| \033[1;34m|.      |\033[0m \033[1;31m|  _  |\033[0m \033[1;33m|__ --|\033[0m \033[1;34m|   _|\033[0m |  -__| \033[1;31m|   _|\033[0m
 |____   | |.  __)_  \033[1;34m|. \\\033[1;31m_\033[1;34m/  |\033[0m \033[1;31m|___._|\033[0m \033[1;33m|_____|\033[0m \033[1;34m|____|\033[0m |_____| \033[1;31m|__|\033[0m  
 |:  1   | |:  1   | \033[1;34m|:  \033[5m\033[1;31m|\033[1;34m   |\033[0m                                      
 |\033[1;31mSearch\033[0m | |\033[1;31mEngine\033[0m | \033[1;34m|\033[1;31mMas|\033[1;31mer\033[1;34m |\033[0m           \033[1mCoded by @\033[1;31m3\033[3;96mTurr \033[0m
 `-------' `-------' \033[1;34m`--- ---'\033[0m                                      
"""
	return banner

def argsload():
	parser = argparse.ArgumentParser(description='SEMaster is a very efective and helpful tool for exploring search engins for BlackHat, SEO, exploiting, crwoling... etc. This tool uses Google, Bing, Yahoo, Ask, Aol, Dogpile, Ixquick, Entirewebs...', epilog="\033[1mCoded by @\033[1;31m3\033[1;36mTurr \033[0m")

	parser.add_argument( '-d', '--dork', required=True, default=None, help='dork, query to search')
	parser.add_argument( '-p', required=False, type=int, default=None , help='number of pages to search, defualt is 1')
	parser.add_argument( '-o', required=False, default=False, help='file to save results')
	parser.add_argument( '-wp', required=False, default=None, help='webapp paths (form,blog,etc), uses with -do')
	parser.add_argument( '-do', required=False, default=False, help='get/filter the Domains only (http://site.com/)', action='store_true')
	parser.add_argument( '-ho', required=False, default=False, help='get/filter the Hosts only (site.com)', action='store_true')
	parser.add_argument( '-nor', required=False, default=True, help='No repeat , Defualt True', action='store_true')

	args = vars(parser.parse_args())
	
	if args['wp'] == None:
		args['wp'] = ["wp-content", "components", "drupal", "vb", "form", "/"]
	if args['p'] != None:
		args['p'] = [0,args['p']]
	else:
		args['p'] = [0,1]

	return args
