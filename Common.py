import os

def print_in_color(string,color_or_format=None):
    string=str(string)
    class bcolors:
        HEADER = '\033[95m'
        OKBLUE = '\033[94m'
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'
    if color_or_format == 'green':
        print(bcolors.OKGREEN + string + bcolors.ENDC)
    elif color_or_format =='red':
        print(bcolors.FAIL + string + bcolors.ENDC)
    elif color_or_format =='yellow':
        print(bcolors.WARNING + string + bcolors.ENDC)
    elif color_or_format =='blue':
        print(bcolors.OKBLUE + string + bcolors.ENDC)
    elif color_or_format =='bold':
        print(bcolors.BOLD + string + bcolors.ENDC)
    else:
        print(string)

def collect_script_paths(path):
    scripts=[]
    for root, dirs, files in os.walk(path):
        for name in files:
            if name.startswith('test_') and name.endswith('.py'):
                file_abs_path=os.path.join(os.path.abspath(root), name)
                if os.path.islink(file_abs_path):
                    continue
                if os.path.getsize(file_abs_path)==0:
                    continue

                scripts.append(file_abs_path)
    return sorted(scripts)

def pair_list_elements(lis):
    return list(zip(lis, lis[1:] + lis[:1]))

def print_tests(dic):
    number_of_tests=0
    for k in list(dic.keys()):
        print_in_color(k, 'yellow')
        for val in dic[k]:
            print_in_color(val, 'green')
            number_of_tests+=1
    print_in_color('Total Number of tests is: '+str(number_of_tests), 'bold')
    return(number_of_tests)

def pair_list(list):
    list_length = len(list)
    list.append(-1)
    return [(list[i], list[i+1]) for i in range(0, list_length, 1)]
