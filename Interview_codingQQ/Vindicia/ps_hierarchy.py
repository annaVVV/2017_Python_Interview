import subprocess

class Node:
    def __init__(self, command, pid, ppid):
        self.name = command
        self.pid = pid
        self.ppid = ppid
        self.children = []
        # if parent:
        #     self.parent.children.append(self)
    def add_child(self, child):
        self.children.append(child)

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
    line = 0
    if count_chilren > 1:
        line = 1
    for c in node.children[:-1]:
        print "{: >5} ".format(c.pid), pref + '\_', c.name
        walk(c, pref + '|'*line + '   ' )
    c = node.children[-1]
    print "{: >5} ".format(c.pid), pref + '\_', c.name
    walk(c, pref + '   ' )


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

    # Create hierarchy
    nodes = {}
    nodes['0'] = Node('root', '0', ppid = None)
    # Create nodes
    for r in rows:
        nodes[r['PID']] = Node(r['COMMAND'], r['PID'], r['PPID'] )
    # Add children to parents
    for r in rows:
        node = nodes[r['PID']]
        nodes[node.ppid].add_child(node)

    return nodes

def main():

    # Execute command "ps -e l" save output into file "in_file"
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
