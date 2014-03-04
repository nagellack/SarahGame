import EventManager
import PygameView
import Game
import KeyboardController
import CPUSpinnerController


def main():
    evManager = EventManager.EventManager()
    game = Game.Game( evManager )
    keybd = KeyboardController.KeyboardController( evManager )
    spinner = CPUSpinnerController.CPUSpinnerController( evManager )
    pygameView = PygameView.PygameView( evManager,game )
    
    spinner.Run()    



if __name__ == "__main__":
    main()
