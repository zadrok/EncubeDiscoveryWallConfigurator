from jsonHandler import JsonHandler

class Model:
    def __init__(self):
        self.screens = []
        self.panels = []

        # options
        self.defaultConfigFile = 'defaultConfig.json'
        self.options = JsonHandler().importFile(self.defaultConfigFile)

        # print( self.options['platform'] )
        # self.options['platform'] = "test"
        # print( self.options['platform'] )

        JsonHandler().exportFile(self,"newConfig.json")
