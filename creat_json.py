import os
import json
import sys
file=""
_path_=""
def create_json(_path_):
    dictionary = '{ }'
    thisdir = os.getcwd()
    for path, subdirs, files in os.walk(thisdir+"/"+_path_+"/"):
        for name in files:
            _f_=os.path.join(path, name)
            with open(_f_, 'r') as reader:
               outp=reader.readline(10)
               outp_f=_f_.split(_path_+"/")[1]
               json_ndex_constructor = {outp_f:""+str(outp).strip()}
               json_ndex= json.loads(dictionary)
               json_ndex.update(json_ndex_constructor)
               dictionary = json.dumps(json_ndex, indent = 4)
    return dictionary
for x in sys.argv:
    if x[0:5] == 'file=':
        file = x[5::]
        print(file)
    if x[0:7] == '_path_=':
        _path_ = x[7::]
        print(_path_)
print(create_json(_path_))
with open(file, "w") as outfile:
    outfile.write(create_json(_path_))

