class PygameView:
    def __init__(self, evManager):
        self.evManager = evManager
        self.evManager.registerListener( self )
		
    def Notify(self, event):
        if event == 'MoveEvent':
            print 'im mooving mooving'