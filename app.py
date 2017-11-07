def get_user():
	return { "name" : "Sam" }

def run():
	user = get_user()
	print user["firstName"]