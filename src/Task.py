class Task:
	def __init__(self, duration, name) -> None:
		self.name = name
		self.duration = duration
		self.completed = 0
		self.finished = False
	