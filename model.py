from jsonHandler import JsonHandler

class Model:
    def __init__(self):
        self.screens = []
        self.panels = []

        # options
        self.defaultConfigFile = 'defaultConfig.json'
        self.options = JsonHandler().importFile(self.defaultConfigFile)

    def addOption(self,key,value):
        self.options.update( {key:value} )

    def inOptions(self,item):
        for key,value in self.options.items():
            if key == item:
                return True
        return False

    def toJson(self):
        data = '{\n'

        for key,value in self.options.items():
            d = self.processVar( str(value) )
            data += '  "' + str(key) + '": ' + d + ',\n'

        data = data[:-2] + '\n}'
        data = data.replace("'",'"')
        return data

    def processVar(self,d):
        if d == '': return '""'
        if d.startswith('['): return d
        if d.startswith('{'): return d

        if self.check_int(d): return str(d)

        return '"' + str(d) + '"'

    def check_int(self,s):
        if s[0] in ('-', '+'):
            return s[1:].isdigit()
        return s.isdigit()
