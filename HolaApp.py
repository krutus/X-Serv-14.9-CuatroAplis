#!/usr/bin/python

class holaApp():
	
	def parse(self, request, rest):
		word = request.split()[1][1:]
		return word


	def process(self,parsedRequest):
		Answer = ("<html><h2>" + str(parsedRequest) + "</h2></html>")
		return("200 OK", Answer)
