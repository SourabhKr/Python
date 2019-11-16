import json


count = 1
input_object_format = []

def check_object_structure(new_object_structure):
    flag = 0
    if len(input_object_format) < 1:
        input_object_format.append(new_object_structure)
    else:
        for each_object in input_object_format:
            if new_object_structure == each_object:
                flag = 1
                break
        if flag == 1:
            input_object_format.append(new_object_structure)

def file_data_streamer():
    with open('/home/sourabh/Studies/Code/Python/DataProcessing/inputData.json') as file_handler:
        for each_line in file_handler.readlines():
            yield each_line[:-2]

            
for each_line in file_data_streamer():
    check_object_structure(list(dict(json.loads(each_line)).keys()))

print(input_object_format)
    