import json

class JsonHandler:
    def importFile(self,file):
        conifg = None
        try:
            conifg = json.load( open(file) )
        except FileNotFoundError:
            print( "Could not find/open " + str(file) )
        return conifg

    def exportFile(self,model,fileName):
        with open(fileName, 'w') as outfile:
            json.dump(model.options, outfile)
