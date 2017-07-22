# grep 'pass' /home/anna/test*_folder/log*.txt
# Search for all files which have word "pass"
#
# /home/test/test_folder/log1.txt
# /home/test/test1_folder/log2.txt
# /home/test/test2_folder
# /home/test/test3_folder

import glob

def check(fname, str):
    """
    :param fname:file path
    :param str:string to serarch in the file
    :return:bool: True if str found, False otherwise.
    """
    with open(fname) as dataf:
        return any(str in line for line in dataf)

for name in glob.glob('C:/test/test*_folder/log[0-9].txt'):
    if check(name, 'pass'):
        print name, 'Found "pass"'
    else:
        print name, 'No "pass"'


# output:
# C:/test\test1_folder\log3.txt Found "pass"
# C:/test\test1_folder\log4.txt Found "pass"
# C:/test\test_folder\log1.txt Found "pass"
# C:/test\test_folder\log2.txt No "pass"
