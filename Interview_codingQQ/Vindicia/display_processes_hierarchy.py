import sys, os

def print_tree(current_node, indent="", last='updown'):

    nb_children = lambda node: sum(nb_children(child) for child in node.children) + 1
    size_branch = {child: nb_children(child) for child in current_node.children}

    """ Creation of balanced lists for "up" branch and "down" branch. """
    up = sorted(current_node.children, key=lambda node: nb_children(node))
    down = []
    while up and sum(size_branch[node] for node in down) < sum(size_branch[node] for node in up):
        down.append(up.pop())

    """ Printing of "up" branch. """
    for child in up:
        next_last = 'up' if up.index(child) is 0 else ''
        next_indent = '{0}{1}{2}'.format(indent, ' ' if 'up' in last else '|', " " * len(current_node.name))
        print_tree(child, indent=next_indent, last=next_last)

    """ Printing of current node. """
    if last == 'up': start_shape = '-'
    elif last == 'down': start_shape = '_'
    elif last == 'updown': start_shape = ' '
    else: start_shape = '|'

    if up: end_shape = '|'
    elif down: end_shape = '-'
    else: end_shape = ''

    print '{0}{1}{2}{3}'.format(indent, start_shape, current_node.name, end_shape)

    """ Printing of "down" branch. """
    for child in down:
        next_last = 'down' if down.index(child) is len(down) - 1 else ''
        next_indent = '{0}{1}{2}'.format(indent, ' ' if 'down' in last else '|', " " * len(current_node.name))
        print_tree(child, indent=next_indent, last=next_last)

class Node:
    def __init__(self, name, pid ,parent=None):
        self.name = name
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

    def get_branch(self):
        if len(self.children)==0: return None
        for c in self.children:
            pass

def walk(node, pref):
    count_chilren = node.count_children()
    if count_chilren==0:
        return

    #if count_chilren > 1:

    for c in node.children:
        print "{: >5} ".format(c.pid), pref + '\_', c.name
        walk(c, '   ' + pref)

# read data file
file = open('input', 'r')

data, rows, nodes = [], [], {}
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
nodes['0'] = Node('root', '0')
# Create hierarchy
for r in rows:
    nodes[r['PID']] = Node(r['COMMAND'], r['PID'], nodes[r['PPID']] )
print "  " + keys[2] + "  " + keys[-1]
# display root children
for pid in nodes['0'].get_children_pid():
    nodes[pid].print_node()
    #print "{: >5} ".format(pid), nodes[pid].name
    walk(nodes[pid], '')
