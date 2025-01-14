def censor(inp):
	inp=inp.split(" ")
	ans= ""
	for i in inp:
		if len(i) > 4 :
			ans = ans + len(i)*"*" + " "
		else :
			ans = ans + i + " " 
	return ans
