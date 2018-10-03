from _ctypes import PyObj_FromPtr
import json
import re
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






# this entire next part is to allow arrays to be printed on the same line when saving (json.dumps()) options to file
# needed for panel dimensions
# without this each element of the array would be on a new line making it harder to use is c
# saving with this here make it easier

# this was also copied from a stackoverflow thread

# see https://stackoverflow.com/questions/13249415
class NoIndent(object):
  """ Value wrapper. """
  def __init__(self, value):
    self.value = value


# see https://stackoverflow.com/questions/13249415
class MyEncoder(json.JSONEncoder):
  FORMAT_SPEC = '@@{}@@'
  regex = re.compile(FORMAT_SPEC.format(r'(\d+)'))

  def __init__(self, **kwargs):
    # Save copy of any keyword argument values needed for use here.
    self.__sort_keys = kwargs.get('sort_keys', None)
    super(MyEncoder, self).__init__(**kwargs)

  def default(self, obj):
    return (self.FORMAT_SPEC.format(id(obj)) if isinstance(obj, NoIndent) else super(MyEncoder, self).default(obj))

  def encode(self, obj):
    format_spec = self.FORMAT_SPEC  # Local var to expedite access.
    json_repr = super(MyEncoder, self).encode(obj)  # Default JSON.

    # Replace any marked-up object ids in the JSON repr with the
    # value returned from the json.dumps() of the corresponding
    # wrapped Python object.
    for match in self.regex.finditer(json_repr):
      # see https://stackoverflow.com/a/15012814/355230
      id = int(match.group(1))
      no_indent = PyObj_FromPtr(id)
      json_obj_repr = json.dumps(no_indent.value, sort_keys=self.__sort_keys)

      # Replace the matched id string with json formatted representation
      # of the corresponding Python object.
      json_repr = json_repr.replace('"{}"'.format(format_spec.format(id)), json_obj_repr)

    return json_repr
