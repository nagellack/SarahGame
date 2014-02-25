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
	pygameView = PygameView.PygameView( evManager )
	game = Game.Game( evManager )
	
	spinner.Run()