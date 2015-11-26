import argparse

def bannerx():
	banner = """ _______   _______   \033[94m___ ___\033[0m                   \033[34m__\033[0m                  
 \033[92m|\033[32m   _   | \033[92m|\033[32m   _   | \033[94m|   Y   |\033[0m \033[91m.---.-.\033[0m \033[33m.-----.\033[0m \033[94m|  |_\033[0m  \033[92m.-----. \033[91m.-.--.\033[0m
 \033[92m|\033[32m   1\033[92m___\033[32m| \033[92m|\033[32m.  1___| \033[94m|.      |\033[0m \033[91m|  _  |\033[0m \033[33m|__ --|\033[0m \033[94m|   _|\033[0m \033[92m|  -__| \033[91m|   _|\033[0m
 \033[92m|____\033[32m   | \033[92m|.\033[32m  \033[92m__)_\033[32m  \033[94m|. \_\033[94m/  |\033[0m \033[91m|___._|\033[0m \033[33m|_____|\033[0m \033[94m|____|\033[92m |_____| \033[91m|\033[91m__|\033[0m  
 \033[92m|:\033[32m  1   | \033[92m|:\033[32m  1   | \033[94m|:  \033[33m\033[94m|\033[94m   |\033[0m                                      
 \033[92m|\033[32m\033[31mSearch\033[32m | \033[92m|\033[31mEngine\033[32m | \033[94m|\033[31mMasT\033[31mer\033[94m |\033[0m           \033[0m Coded by @\033[31m3\033[96mTurr \033[0m
 \033[92m`-\033[32m------' \033[92m`-\033[32m------' \033[94m`--- ---'\033[0m                                      
"""
	return banner

def argsload():
	parser = argparse.ArgumentParser(description='\033[32mSEMaster is a very efective and helpful tool for exploring search engins for BlackHat, SEO, exploiting, crwoling... etc. This tool uses Google, Bing, Yahoo, Ask, Aol, Dogpile, Ixquick, Entirewebs...', epilog=" \033[0m Coded by @\033[31m3\033[96mTurr ")

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
