#!/usr/bin/python


class plus():

	def parse(self, request, rest):
		try:
			operation = rest.split("/")
			if len(operation) !=2:
				return "Intruduce 2 valores a sumar"
			first= int(operation[0])
			second= int(operation[1])
		except ValueError:
			return None
		return (first, second)

	def process(self, parsedRequest):
		if parsedRequest:
			try:
				result = int(parsedRequest[0]) + int(parsedRequest[1])
				return ("200 OK", "<html><body><h1>" +
						str(result) + "</h1></body></html>")
			except ValueError:
				return "Enter two numbers"
		else:
			return ("400 Error", "<html>" +
					"<body><h1>Error</h1>" +
					"</body></html>")


