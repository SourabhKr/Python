import json
count = 0
with open('/home/sourabh/Studies/Code/Python/DataProcessing/miniInputData.json') as file_handler:
    for each_line in file_handler.readlines():
        print(json.loads(each_line[:-2]))