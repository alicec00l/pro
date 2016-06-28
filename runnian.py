#!/usr/bin/python


while True:
	year = int(raw_input("plz a yesr:").strip())
	if year%400 == 0:
		print year,"is runnian"
	elif year%4 == 0:
		print year,"is runnian"
	else:
		print "This is not runnian"
	
