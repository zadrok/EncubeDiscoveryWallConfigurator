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

        # JsonHandler().exportFile(self,"newConfig.json")

    def inOptions(self,item):
        for key,value in self.options.items():
            if key == item:
                return True
        return False
