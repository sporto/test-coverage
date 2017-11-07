class GetUser:
	def run(self):
		return { "name" : "Sam" }

def run():
	user = get_user()
	print user["firstName"]
