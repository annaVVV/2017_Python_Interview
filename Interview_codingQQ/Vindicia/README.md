# OVERVIEW 
-------- 
Create a Perl program that displays the hierarchy of processes on a Linux 
computer. 

Its output should look like: 
```
1       init 
2       \_ keventd 
3       \_ kapmd 
908     \_ /usr/sbin/sshd 
6133       \_ sshd 
6137          \_ bash 
6196             \_ ps -axf 
```

DATA GATHERING 
-------------- 
This exercise is to test your knowledge of procedural programming and Perl 
data structures.  It is *not* to test your ability to grab a module off of 
CPAN that can do this, already.  There are two approved mechanisms for 
gathering this data; either the output of "ps -e l" (note that this is "ps -e <space> l" 
not "ps -el", which presents the PID parent/child relationship in a flat fashion) or
by browsing the "/proc" filesystem hierarchy.  Any other methods for gathering
data must be discussed, first. 

Just to make things easier, I'm enclosing a sample of the ps -e l output for you to
work from, in case you don't have a Linux box handy.  I'm also enclosing a sample
of what the output should look like, as the example above doesn't cover all the
cases it should...

IMPLEMENTED
------------
* Run from cmd:
```
$ python ps_hierarchy.py > output     
```

* Script **ps_hierarchy.py.py**  executs command *"ps -e l"* and saves output into file **"in_file"**
* **nodes**: a dictionary with **PID** as **keys** and **value** as a **Node** instance created for each command (see *class* **Node**)
* Method **walk(node, pref)** recursively prints all commands hierarchy 
* Result file: **output**

**Note**: vertical lines will be implemented later
