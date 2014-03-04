import EventManager
import pygame
import main
import gc

class CPUSpinnerController:
	"""..."""
	def __init__(self, evManager):
		self.evManager = evManager
		self.evManager.registerListener( self )

		self.keepGoing = 1

	#----------------------------------------------------------------------
	def Run(self):
		clock = pygame.time.Clock()
		while self.keepGoing:
			event = "TickEvent"
			self.evManager.post( event )
			clock.tick(30)

	#----------------------------------------------------------------------
	def Notify(self, event):
	   if event == "PlayAgain":
	       self.keepGoing = False
	       gc.collect()
	       main.main()
	   elif event == "QuitEvent":
	       self.keepGoing = False