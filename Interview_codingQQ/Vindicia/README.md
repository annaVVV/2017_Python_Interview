
TODO
------------
* Run from terminal:
```
$ python ps_hierarchy.py > output     
```

* Script **ps_hierarchy.py.py**  executs command *"ps -e l"* and saves output into file **"in_file"**
* **nodes**: a dictionary with **PID** as **keys** and **value** as a **Node** instance created for each command (see *class* **Node**)
* Method **walk(node, pref)** recursively prints all commands hierarchy 
* Result file: **output**
