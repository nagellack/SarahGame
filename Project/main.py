import EventManager
import PygameView
import Game
import KeyboardController
import CPUSpinnerController




if __name__ == "__main__":
	"""..."""
	evManager = EventManager.EventManager()

	keybd = KeyboardController.KeyboardController( evManager )
	spinner = CPUSpinnerController.CPUSpinnerController( evManager )
	game = Game.Game( evManager )
	pygameView = PygameView.PygameView( evManager,game )
	
	
	spinner.Run()