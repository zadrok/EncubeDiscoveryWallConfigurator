import json
import io

class JsonHandler:
    def importFile(self,file):
        conifg = None
        try:
            conifg = json.load( open(file) )
        except FileNotFoundError:
            print( "Could not find/open " + str(file) )
        return conifg

    def exportFile(self,model,fileName):
        with io.open(fileName, 'w', encoding='utf-8') as f:
            f.write( model.toJson() )
