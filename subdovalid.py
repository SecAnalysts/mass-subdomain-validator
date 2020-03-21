#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#Coded BY pelandok
#secanalyst 2014

from urllib2 import Request, urlopen, URLError, HTTPError

def Space(j):
	i = 0
	while i<=j:
		print " ",
		i+=1


def grabfile():
	f = open("web.txt","r");
	print "\n\nRequest 200 OK : \n"
	while True:
		link = f.readline()
		if not link:
			break
		req_link = "https://"+link+""
		req = Request(req_link)
		try:
			response = urlopen(req)
		except HTTPError as e:
			continue
		except URLError as e:
			continue
		else:
			print req_link

	print "\n\nSave Result to result.txt \n"


def Credit():
	Space(9); print "##########################################"
	Space(9); print "#    +++Mass Subdomain Validator +++     #"
	Space(9); print "#      Script Coded By SecAnalysts       #"
	Space(9); print "#          Satam Cyber Team              #"
	Space(9); print "##########################################"

Credit()
grabfile()

