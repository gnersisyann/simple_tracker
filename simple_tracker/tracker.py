class Tracker:
	count = 0
	def increment(self):
		self.count += 1
	def save_to_file(self):
		f = open("data.txt","a")
		f.write(str(self.count))
	def __str__(self):
		return (f"Current count: {self.count}")
	def reset(self):
		self.count = 0