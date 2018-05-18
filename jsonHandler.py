import json
import io

class JsonHandler:
  ''' used to import and export json files '''
  def importFile(self,file):
    ''' returns a json object '''
    conifg = None
    try:
      conifg = json.load( open(file) )
    except FileNotFoundError:
      print( "Could not find/open " + str(file) )
    return conifg

  def exportFile(self,model,fileName):
    ''' takes in model and file name, creates file and writes model data to it '''
    with io.open(fileName, 'w', encoding='utf-8') as f:
      f.write( model.toJson() )
