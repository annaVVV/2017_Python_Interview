import sys, os, subprocess

class Node:
    def __init__(self, command, pid ,parent=None):
        self.name = command
        self.pid = pid
        self.parent = parent
        self.children = []
        if parent:
            self.parent.children.append(self)

    def count_children(self):
        return len(self.children)

    def print_node(self):
        print "{: >5} ".format(self.pid), self.name

    def get_children_pid(self):
        pids = []
        for c in self.children:
            pids.append(c.pid)
        return sorted(pids)


def walk(node, pref):
    count_chilren = node.count_children()
    if count_chilren==0:
        return

    #if count_chilren > 1:
    for c in node.children:
        print "{: >5} ".format(c.pid), pref + '\_', c.name
        walk(c, '   ' + pref)

def cmd_exec(cmd):
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    output, err = p.communicate()
    p_status = p.wait()
    #print("Executed command: {}, status: {}".format(cmd, p_status))
    if p_status > 0:
        print("ERROR: Not able to execute:" + cmd)
        exit()
    return p_status, output

#  file_name: file with output of "ps -e l" command
#  return: dictionary with keys as PID , value as Node
def get_dict(file_name):
    file = open(file_name)
    # str = file.read()
    # data = str.split('\n')
    data, rows = [], []
    for row in file:
        data.append(row)
    header =  data[0]
    keys = header.split()
    output = [o.strip('\n') for o in data[1:]]
    ind_command = header.find(keys[-1])
    for o in output:
        o1 = o[0:ind_command].split()
        row = {keys[2]: o1[2], keys[3]: o1[3], keys[-1]: o[ind_command:]}
        rows.append(row)

    # Sort by parent
    rows.sort(key=lambda x: int(x[keys[3]]))

    # Create hierarchy
    nodes = {}
    nodes['0'] = Node('root', '0')

    for r in rows:
        nodes[r['PID']] = Node(r['COMMAND'], r['PID'], nodes[r['PPID']] )

    return nodes

def main():

    # Execute command: "ps -e l" put output into file "ps_table"
    command = "ps -e l"
    #command = "dir"  # test on windows cmd_exec
    command_out_file = 'in_file'
    cmd_exec( command + " > " + command_out_file)

    # Parse the command output columns (PID, PPID, COMMAND) and return a dictionary with keys as PID , value as Node
    #nodes = get_dict('input') # to test on Windows
    nodes = get_dict(command_out_file)

    # Display the hierarchy of processes on a Linux computer
    print "  PID  COMMAND"
    # display root children
    for pid in nodes['0'].get_children_pid():
        nodes[pid].print_node()
        walk(nodes[pid], '')

if __name__ == "__main__":
    main()