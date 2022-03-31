import os
import json
def create_json():
    dictionary = '{ }'
    thisdir = os.getcwd()
    for path, subdirs, files in os.walk(thisdir+"/config/"):
        for name in files:
            _f_=os.path.join(path, name)
            with open(_f_, 'r') as reader:
               outp=reader.readline(10)
               outp_f=_f_.split("config/")[1]
               slack_data = {outp_f:""+str(outp).strip()}
               bob= json.loads(dictionary)
               bob.update(slack_data)
               dictionary = json.dumps(bob, indent = 4)
    return dictionary

print(create_json())
with open("Robert.json", "w") as outfile:
    outfile.write(create_json())

