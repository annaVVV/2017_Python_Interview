import os
import subprocess

def verifyFileExists(file):
    print("Current directory is: '{}' ".format(os.path.abspath(os.curdir)))
    print("Verifying if a file '{}' exists: ".format(file))
    if os.path.isfile(file):
        print("Verified: File '{}' exists".format(file))
        return True
    else:
        print("ERROR: File '{}' does not exist".format(file))
        return False

def verifyFolderExists(folder):
    if os.path.isdir(folder):
        print("Verified: Folder '{}' exists".format(folder))
        return True
    else:
        print("ERROR: Folder '{}' does not exist".format(folder))
        return False

def cmd_exec(cmd):
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    output, err = p.communicate()
    p_status = p.wait()
    print("Executed command: {}, status: {}".format(cmd, p_status))
    print('Output: ' + str(output))
    if p_status > 0:
        print("ERROR: Not able to execute:" + cmd)
    return p_status, output

verifyFileExists("data.txt")
verifyFolderExists("TestFolder")
# Output:
# Current directory is: 'C:\Users\Anna\PycharmProjects\InterviewTests\Advance'
# Verifying if a file 'data.txt' exists:
# Verified: File 'data.txt' exists
# Verified: Folder 'TestFolder' exists

cmd_exec("echo %PATH%")
# Executed command: echo %PATH%, status: 0
# Output: C:\Program Files\Java\jre1.8.0_101\bin;C:\ProgramData\Oracle\Java\javapath;C:\WINDOWS\system32;
