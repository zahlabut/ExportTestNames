from Common import *
from Conf import *

result = []
for path in paths:
    classes=[]
    for sc in collect_script_paths(path):
        script_data = open(sc, 'r').read()
        for line in script_data.splitlines():
            if line.replace(' ','').startswith('class') and line.endswith(':'):
                classes.append(line)

        class_tests = {}
        blocks = pair_list_elements(classes)
        for class_block in blocks:
            if blocks.index(class_block) == len(blocks)-1:
                class_data = script_data[script_data.find(class_block[0]):]
            else:
                class_data = script_data[script_data.find(class_block[0]):script_data.find(class_block[1])]
            test_cases=[]
            for line in class_data.splitlines():
                if 'def test_' in line:
                    test_cases.append(line)
            if len(test_cases)>0:
                class_tests[class_block[0]]=test_cases
        result.append([sc,class_tests])

    for item in result:
        print_in_color('#'*150,'bold')
        print_in_color(item[0], 'blue')
        print_dic(item[1])
