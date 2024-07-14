from src.Countdown import Countdown
from src.Task import Task


class Pomodoro:
	def __init__(self) -> None:
		self.countdown:Countdown = Countdown(100)
		self.tasks = [Task(100, "COOOO"), Task(200, "HASUDHUAS")]
		self.activeTask = self.tasks[0]
		self.menu()
	
	def changeTask(self):
		op = int(input("Escolha a task(0 ou 1): "))
		if op >= 0 and op < len(self.tasks):
			self.activeTask = self.tasks[op]
			self.countdown.changeTime(self.activeTask.duration)
	
	def menu(self):
		while True:
			print("Menu:")
			print("1-Iniciar cronometro\n2-Pausar cronometro\n3-Trocar task\n0-Finalizar")
			try:
				op = int(input())
				if op == 1:
					self.countdown.play()
				elif op == 2:
					self.countdown.pause()
				elif op == 3:
					self.changeTask()
				elif op == 0:
					self.countdown.destroy()
					break
				else:
					raise Exception()
			except:
				input("Comando não conhecido\n\n")
