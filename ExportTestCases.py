from Common import *
from Conf import *
import re

rbac_indication_string = "expected_allowed"
result = []
for path in paths:
    classes=[]
    for sc in collect_script_paths(path):
        script_data = open(sc, 'r').read()
        for line in script_data.splitlines():
            if re.match(r'^class ', line):
                classes.append(line)
        class_tests = {}
        blocks = pair_list_elements(classes)

        for class_block in blocks:
            if blocks.index(class_block) == len(blocks)-1:
                class_data = script_data[script_data.find(class_block[0]):]
            else:
                class_data = script_data[script_data.find(class_block[0]):script_data.find(class_block[1])]
            test_lines=[]
            class_lines=class_data.splitlines()

            # Get def blocks as start stop indexes, for example [(1,3),(3,10)]
            defs=[]
            for line in class_lines:
                if re.match(r'^\s+def ', line):# and line.endswith(':'):
                    defs.append(class_lines.index(line))
            defs_blocks=pair_list(defs)

            # Get functions with RBAC string
            rback_functions=[]
            for def_block in defs_blocks:
                 if rbac_indication_string in str(class_lines[def_block[0]:def_block[1]]):
                    func_name=class_lines[def_block[0]].split('(')[0].split('def ')[1]
                    rback_functions.append(func_name)

            # Get test names and check for RBAC support
            test_cases=[]
            for block in defs_blocks:
                if block!=[]:
                    for line in class_lines[block[0]:block[1]]:
                        if re.match(r'^\s+def test_', line):
                            test_name=line
                            if rbac_indication_string in str(class_lines[block[0]:block[1]]):
                                test_name+=' Supports RBAC'
                            else:
                                for func in rback_functions:
                                    if func in str(class_lines[block[0]:block[1]]):
                                        test_name += ' Supports RBAC'
                                        break
                            test_cases.append(test_name)
                            break

            if len(test_cases)>0:
                class_tests[class_block[0]]=test_cases
        result.append([sc,class_tests])

    total_test_number=0
    for item in result:
        print_in_color('#'*150,'bold')
        print_in_color(item[0], 'blue')
        total_test_number+=print_tests(item[1])

print_in_color('The total number of all tests is:'+str(total_test_number), 'blue')




# from Common import *
# from Conf import *
#
# result = []
# for path in paths:
#     classes=[]
#     for sc in collect_script_paths(path):
#         script_data = open(sc, 'r').read()
#         for line in script_data.splitlines():
#             if line.replace(' ','').startswith('class') and line.endswith(':'):
#                 classes.append(line)
#
#         class_tests = {}
#         blocks = pair_list_elements(classes)
#         for class_block in blocks:
#             if blocks.index(class_block) == len(blocks)-1:
#                 class_data = script_data[script_data.find(class_block[0]):]
#             else:
#                 class_data = script_data[script_data.find(class_block[0]):script_data.find(class_block[1])]
#             test_cases=[]
#             for line in class_data.splitlines():
#                 if 'def test_' in line:
#                     test_cases.append(line)
#             if len(test_cases)>0:
#                 class_tests[class_block[0]]=test_cases
#         result.append([sc,class_tests])
#
#     total_test_number=0
#     for item in result:
#         print_in_color('#'*150,'bold')
#         print_in_color(item[0], 'blue')
#         total_test_number+=print_tests(item[1])
#
# print_in_color('The total number of all tests is:'+str(total_test_number), 'blue')