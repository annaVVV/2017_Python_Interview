#!/usr/bin/python
import threading
import time


def timer(name, delay, repeat):
    print
    "Timer: " + name + " Started"
    while repeat > 0:
        time.sleep(delay)
        print( name + ": " + str(time.ctime(time.time())))
        repeat -= 1
    print("Timer: " + name + " Completed")
    print(">> Timer: " + name, "active treads:", threading.active_count())


def Main():
    print("active treads:", threading.active_count())
    t1 = threading.Thread(target=timer, args=("Timer1", 1, 5))
    t2 = threading.Thread(target=timer, args=("Timer2", 2, 5))
    print("active treads:", threading.active_count())
    t1.start()
    t2.start()
    print ("Main complete")
    print("active treads:", threading.active_count())

if __name__ == '__main__':
    Main()
    
    # Output:
# ('active treads:', 1)
# ('active treads:', 1)

# Main complete
# ('active treads:', 3)
# Timer1: Thu Aug 24 16:38:13 2017
# Timer2: Thu Aug 24 16:38:14 2017
# Timer1: Thu Aug 24 16:38:14 2017
# Timer1: Thu Aug 24 16:38:15 2017
# Timer2: Thu Aug 24 16:38:16 2017
# Timer1: Thu Aug 24 16:38:16 2017
# Timer1: Thu Aug 24 16:38:17 2017
# Timer: Timer1 Completed
# ('>> Timer: Timer1', 'active treads:', 3)
# Timer2: Thu Aug 24 16:38:18 2017
# Timer2: Thu Aug 24 16:38:20 2017
# Timer2: Thu Aug 24 16:38:22 2017
# Timer: Timer2 Completed
# ('>> Timer: Timer2', 'active treads:', 2)
