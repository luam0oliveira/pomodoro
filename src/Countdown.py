from threading import Thread
import time

class Countdown:
	def __init__(self, initial):
		self.initial = initial
		self.actual = initial
		self.active = False
		self.running = True
		self.thread = Thread(target=self.tic)
		self.thread.start()

	def tic(self):
		while self.running:
			while self.actual >= 0 and self.running:
				if self.active:
					time.sleep(0.1)
					self.actual -= 1
			if self.running:
				print("Finished")
				self.reset()
				self.pause()
		return
	
	def destroy(self):
		self.running = False
		self.actual = -1

	def reset(self):
		self.actual = self.initial

	def pause(self):
		self.active = False

	def play(self):
		self.active = True
	
	def changeTime(self, newTime):
		self.initial = newTime
		self.actual = newTime
