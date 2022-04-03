#Run Comandline exmple
#creat_json.py file=Robert.json _path_=config
#Get two varibals
## One name of file we want stream output
## Second what Subpath we want scan for create json
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
               # Get contnet from file
               outp=reader.readline(10)
               # Get Path of file
               outp_f=_f_.split(_path_+"/")[1]
               # Create json index
               json_ndex_constructor = {outp_f:""+str(outp).strip()}
               # Load Template dictionary for jsod
               json_ndex= json.loads(dictionary)
               # Add new index update template dictionary
               json_ndex.update(json_ndex_constructor)
               # Load New dictionary After all index be added
               dictionary = json.dumps(json_ndex, indent = 4)
    return dictionary
for x in sys.argv:
    if x[0:5] == 'file=':
        file = x[5::]
        print(file)
    if x[0:7] == '_path_=':
        _path_ = x[7::]
        print(_path_)
#Get Sume output of end json
print(create_json(_path_))
#Create Json File with output stream
with open(file, "w") as outfile:
    outfile.write(create_json(_path_))

