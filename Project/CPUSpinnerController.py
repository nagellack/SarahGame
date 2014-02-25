import EventManager
class CPUSpinnerController:
	"""..."""
	def __init__(self, evManager):
		self.evManager = evManager
		self.evManager.registerListener( self )

		self.keepGoing = 1

	#----------------------------------------------------------------------
	def Run(self):
		while self.keepGoing:
			event = "TickEvent"
			self.evManager.post( event )

	#----------------------------------------------------------------------
	def Notify(self, event):
		if event == "QuitEvent":
			#this will stop the while loop from running
			self.keepGoing = False