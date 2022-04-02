import os
import json
import sys
def create_json():
    dictionary = '{ }'
    thisdir = os.getcwd()
    for path, subdirs, files in os.walk(thisdir+"/config/"):
        for name in files:
            _f_=os.path.join(path, name)
            with open(_f_, 'r') as reader:
               outp=reader.readline(10)
               outp_f=_f_.split("config/")[1]
               json_ndex_constructor = {outp_f:""+str(outp).strip()}
               json_ndex= json.loads(dictionary)
               json_ndex.update(json_ndex_constructor)
               dictionary = json.dumps(json_ndex, indent = 4)
    return dictionary
for x in sys.argv:
    if x[0:6] == 'file=':
        file = x[6::]
        print (file)
print(create_json())
with open(file, "w") as outfile:
    outfile.write(create_json())

